#!/usr/bin/env python3
"""SEO pass: canonical + social tags, noindex for private pages, richer LocalBusiness schema, robots.txt, sitemap.xml.
Safe to re-run (replaces its own block). Run it after build.py, and whenever you change domain:
    python3 seo.py https://yourdomain.com
"""
import glob, json, os, re, sys
DOMAIN = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SITE_DOMAIN", "https://rafgodwin.com")).rstrip("/")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PRIVATE = {"admin.html", "admin-login.html", "cart.html", "checkout.html", "order-success.html", "product.html"}
NOINDEX = PRIVATE - {"product.html"}          # product.html sets its own canonical per product (js/shop.js)
IMG = DOMAIN + "/assets/img/hero-solar.jpg"
pages = []
for f in sorted(glob.glob("*.html")):
    h = open(f, encoding="utf-8").read()
    h = re.sub(r"<!--seo-->.*?<!--/seo-->", "", h, flags=re.S)
    title = re.search(r"<title>(.*?)</title>", h, re.S).group(1)
    m = re.search(r'<meta name="description" content="(.*?)"', h)
    desc = m.group(1) if m else ""
    url = DOMAIN + "/" + ("" if f == "index.html" else f)
    b = ["<!--seo-->"]
    if f in NOINDEX:
        b.append('<meta name="robots" content="noindex,nofollow">')
    else:
        if f != "product.html":
            b.append('<link rel="canonical" href="%s">' % url)
            b.append('<meta property="og:url" content="%s">' % url)
            pages.append(f)
        if 'property="og:title"' not in h: b.append('<meta property="og:title" content="%s">' % title)
        if 'property="og:description"' not in h and desc: b.append('<meta property="og:description" content="%s">' % desc)
        if 'property="og:type"' not in h: b.append('<meta property="og:type" content="website">')
        b += ['<meta property="og:site_name" content="RafGodwin Engineering">', '<meta property="og:locale" content="en_GH">',
              '<meta property="og:image" content="%s">' % IMG, '<meta name="twitter:card" content="summary_large_image">']
    b.append("<!--/seo-->")
    h = h.replace("</head>", "".join(b) + "</head>", 1)
    # richer LocalBusiness schema on the home page
    def fix(mo):
        d = json.loads(mo.group(2))
        if d.get("@type") == "LocalBusiness":
            d.update({"url": DOMAIN + "/", "image": IMG, "logo": DOMAIN + "/assets/img/logo.png", "areaServed": "Ghana",
                      "email": "info@rafgodwin.com",
                      "openingHoursSpecification": [
                          {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"},
                          {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "16:00"}]})
        return mo.group(1) + json.dumps(d) + mo.group(3)
    h = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', fix, h, flags=re.S)
    open(f, "w", encoding="utf-8").write(h)

# robots.txt
open("robots.txt", "w").write("User-agent: *\nAllow: /\nDisallow: /admin\nDisallow: /admin-login.html\nDisallow: /cart.html\nDisallow: /checkout.html\nDisallow: /order-success.html\n\nSitemap: %s/sitemap.xml\nSitemap: %s/sitemap-products.xml\n" % (DOMAIN, DOMAIN))
# sitemap.xml (static pages; products are in /sitemap-products.xml, served live by a Netlify function)
prio = {"index.html": "1.0", "shop.html": "0.9", "quote.html": "0.9"}
x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for f in pages:
    x += "<url><loc>%s/%s</loc><priority>%s</priority></url>\n" % (DOMAIN, "" if f == "index.html" else f, prio.get(f, "0.7"))
open("sitemap.xml", "w").write(x + "</urlset>\n")
print("SEO applied for", DOMAIN, "-", len(pages), "pages in sitemap")
