#!/usr/bin/env python3
"""Generates the 15-page RafGodwin Engineering static site. Run: python3 build.py"""
import os, json

OUT = os.path.dirname(os.path.abspath(__file__))
PHONE_DISPLAY = "024 711 7982"
PHONE_TEL = "+233247117982"
WA = "233551120109"
EMAIL = "info@rafgodwin.com"
PLACE_ID = ""   # optional: paste the Google Place ID to open the direct review box
MAPS_URL = "https://www.google.com/maps/search/?api=1&query=RafGodwin+Engineering+Kwashieman+Ofankor+Road+Sowutuom+Accra"
REVIEW_URL = ("https://search.google.com/local/writereview?placeid=" + PLACE_ID) if PLACE_ID else MAPS_URL
ADDRESS = "JP9F+Q85, Kwashieman Ofankor Road, Sowutoum, Accra"
INSTAGRAM = "https://www.instagram.com/rafgodwin.engineering/"
TIKTOK = "https://www.tiktok.com/@rafgodwinengineering"
MAP = "https://www.google.com/maps?q=JP9F%2BQ85%20Kwashieman%20Ofankor%20Road%20Sowutuom%20Accra&output=embed"
BRAND = "RafGodwin Engineering"

I = {
 "bulb": '<path d="M9 18h6M10 22h4M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.3h6c0-1 .4-1.8 1-2.3A7 7 0 0 0 12 2z"/>',
 "shield": '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5l8-3z"/><path d="M9 12l2 2 4-4"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5L19 19M5 19l1.5-1.5M17.5 6.5L19 5"/>',
 "cam": '<path d="M3 7h12a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H3z"/><path d="M17 11l4-2v6l-4-2"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 "panel": '<path d="M3 16l3-10h12l3 10z"/><path d="M12 6v10M7 11h10M12 16v4M8 20h8"/>',
 "build": '<path d="M3 21h18M5 21V7l7-4 7 4v14M9 21v-6h6v6"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 "wifi": '<path d="M2 9a15 15 0 0 1 20 0M5 13a10 10 0 0 1 14 0M8.5 16.5a5 5 0 0 1 7 0"/><circle cx="12" cy="20" r="1"/>',
 "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-5 3 3 5-7"/>',
 "gate": '<path d="M3 21V7M21 21V7M3 10h18M3 15h18M8 10v11M13 10v11M17 10v11"/>',
 "wrench": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-.5-.5-2.5z"/>',
 "check": '<path d="M5 12l5 5 9-10"/>',
}
def ic(n): return '<span class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg></span>' % I[n]

NAV_SERVICES = [
 ("smart-home.html", "Smart Home & Automation"),
 ("security.html", "Security & Access Control"),
 ("solar.html", "Solar & Renewable Energy"),
 ("cctv.html", "CCTV & Surveillance"),
 ("electric-fencing.html", "Electric Fencing & Perimeters"),
 ("smart-locks.html", "Smart Locks & Gate Automation"),
 ("residential-solar.html", "Residential Solar Packages"),
 ("commercial-energy.html", "Commercial Energy Engineering"),
]
NAV = [("index.html","Home"),("about.html","About"),("SERVICES","Services"),("portfolio.html","Portfolio"),("testimonials.html","Reviews"),("faq.html","FAQs"),("contact.html","Contact")]

LOGO = '<img class="logo-img" src="assets/img/logo-mark-light.png" alt="" width="54" height="25">'

def header(cur):
    li = ""
    for href, label in NAV:
        if href == "SERVICES":
            act = " active" if cur in [h for h, _ in NAV_SERVICES] else ""
            sub = "".join('<li><a href="%s">%s</a></li>' % (h, l) for h, l in NAV_SERVICES)
            li += '<li><a class="l%s" href="smart-home.html" aria-haspopup="true">%s &#9662;</a><ul class="drop">%s</ul></li>' % (act, label, sub)
        else:
            li += '<li><a class="l%s" href="%s">%s</a></li>' % (" active" if href == cur else "", href, label)
    li += '<li><a class="l%s" href="shop.html">Shop</a></li>' % (" active" if cur == "shop.html" else "")
    li += '<li class="mob-cta"><a class="btn btn-primary" href="quote.html">Get a Free Quote</a></li>'
    return ('<a class="skip" href="#main" style="position:absolute;left:-999px">Skip to content</a>'
      '<div class="topbar"><div class="wrap"><span>Accra, Ghana &middot; Smart Home &middot; Security &middot; Solar</span>'
      '<span>Call us: <a href="tel:%s">%s</a></span></div></div>'
      '<header class="site"><div class="wrap nav"><a class="logo" href="index.html" aria-label="%s home">%s<span>Raf<b>Godwin</b> Engineering</span></a>'
      '<a class="cart-btn" href="cart.html" aria-label="Cart"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/><path d="M2 3h3l2.6 12.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 7H6"/></svg><span class="cart-badge" hidden>0</span></a><button class="burger" aria-label="Menu" aria-expanded="false">&#9776;</button><ul class="menu">%s</ul>'
      '<a class="btn btn-primary" href="quote.html">Get a Free Quote</a></div></header>') % (PHONE_TEL, PHONE_DISPLAY, BRAND, LOGO, li)

def footer():
    svc = "".join('<li><a href="%s">%s</a></li>' % (h, l) for h, l in NAV_SERVICES[:5])
    return ('<footer class="site"><div class="wrap"><div class="fgrid">'
     '<div><a class="logo" href="index.html">%s<span>Raf<b>Godwin</b> Engineering</span></a>'
     '<p style="margin-top:14px;color:#aab6cf">Premium smart home automation, security and solar engineering for homes and businesses across Ghana.</p>'
     '<div class="social social-icons"><a class="soc-ico" href="%s" target="_blank" rel="noopener noreferrer" aria-label="RafGodwin Engineering on Instagram"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5.500"/><circle cx="12" cy="12" r="4.200"/><circle cx="17.300" cy="6.700" r="1" fill="#fff" stroke="none"/></svg></a>'
     '<a class="soc-ico" href="%s" target="_blank" rel="noopener noreferrer" aria-label="RafGodwin Engineering on TikTok"><svg viewBox="0 0 24 24" width="26" height="26" fill="#fff" aria-hidden="true"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg></a></div></div>'
     '<div><h4>Services</h4><ul>%s</ul></div>'
     '<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="portfolio.html">Project Portfolio</a></li><li><a href="testimonials.html">Client Reviews</a></li><li><a href="faq.html">Smart Home FAQs</a></li><li><a href="quote.html">Request a Quote</a></li><li><a href="contact.html">Contact Us</a></li></ul></div>'
     '<div><h4>Visit &amp; Call</h4><ul><li>%s</li><li><a href="tel:%s">%s</a></li><li><a href="https://wa.me/%s">WhatsApp us</a></li></ul></div>'
     '</div></div><div class="copy"><div class="wrap"><span>&copy; 2026 %s. All rights reserved.</span>'
     '<span class="credit">Designed &amp; Developed by Clemence (<a href="tel:+233558677511">+233558677511</a>)</span></div></div></footer>'
     '<div class="fab"><a class="wa" href="https://wa.me/%s" aria-label="WhatsApp"><svg viewBox="0 0 60 60" aria-hidden="true"><defs><linearGradient id="rgw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#61fd7d"/><stop offset="1" stop-color="#25cf43"/></linearGradient></defs><rect width="60" height="60" rx="30" fill="url(#rgw)"/><g transform="translate(10 10) scale(1.67)" fill="#fff"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm0 1.8a8.2 8.2 0 1 1-4.2 15.3l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 0 1 12 3.800z" fill-rule="evenodd"/><path d="M17.800 16.200c-.2.700-1.400 1.300-1.900 1.400-.5.100-1.100.100-1.800-.1-.4-.1-1-.3-1.700-.6-3-1.300-4.900-4.300-5.100-4.500-.1-.2-1.200-1.600-1.200-3s.8-2.100 1-2.400c.3-.3.600-.3.800-.3h.6c.2 0 .4 0 .6.500l.8 2c.1.200.1.300 0 .5l-.3.500-.4.400c-.1.200-.3.300-.1.600.2.300.8 1.300 1.700 2.100 1.100 1 2.100 1.300 2.400 1.500.3.100.5.100.6-.1l.9-1.100c.2-.3.400-.2.700-.1l1.900.9c.3.100.5.200.5.300.1.200.1.700-.1 1.400z"/></g></svg></a>'
     '<a class="ph" href="tel:%s" aria-label="Call us"><svg viewBox="0 0 60 60" aria-hidden="true"><defs><linearGradient id="rgp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#67ee7a"/><stop offset="1" stop-color="#2bc840"/></linearGradient></defs><rect width="60" height="60" rx="30" fill="url(#rgp)"/><path transform="translate(12 12) scale(1.5)" fill="#fff" d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1.02z"/></svg></a></div>'
    ) % (LOGO, INSTAGRAM, TIKTOK, svc, ADDRESS, PHONE_TEL, PHONE_DISPLAY, WA, BRAND, WA, PHONE_TEL)

LD = {"@context":"https://schema.org","@type":"LocalBusiness","name":BRAND,"telephone":PHONE_TEL,
 "address":{"@type":"PostalAddress","streetAddress":"Kwashieman Ofankor Road, Sowutoum (JP9F+Q85)","addressLocality":"Accra","addressCountry":"GH"},
 "description":"Smart home automation, security and access control, and solar engineering in Accra, Ghana."}


import re
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Anton&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet"><link rel="stylesheet" href="assets/css/premium.css"><link rel="stylesheet" href="assets/css/shop.css">'
LOCK = "<script>(function(){var r=document.documentElement;try{if(localStorage.getItem('rg_tos')!=='accepted')r.className+=' tos-lock'}catch(e){r.className+=' tos-lock'}})();</script>"
TERMS_TXT = ('<ol><li><b>Use of this site.</b> The content is for general information about our smart home, security and solar services in Ghana.</li>'
 '<li><b>Quotes.</b> Quotes and estimates are non-binding until confirmed in writing after a site survey.</li>'
 '<li><b>Your details.</b> When you send an enquiry we use your details only to respond to you by WhatsApp, phone or email. We do not sell your data.</li>'
 '<li><b>Messaging.</b> Sending an enquiry through WhatsApp or email means you agree to be contacted back on that channel.</li>'
 '<li><b>Content.</b> Text, images and branding belong to RafGodwin Engineering and may not be copied without permission.</li>'
 '<li><b>Liability.</b> Information is provided in good faith. Final specifications, prices and timelines are agreed in your signed quotation.</li></ol>')
GATE = ('<div class="gate" id="tos-gate" role="dialog" aria-modal="true" aria-labelledby="tos-t" hidden><div class="gate-card"><img class="gate-logo" src="assets/img/logo.png" alt="RafGodwin Engineering - Smart Home Experts">'
 '<span class="eyebrow">Before you continue</span><h2 id="tos-t">Terms of Service</h2><p class="gate-sub">Please read and accept to enter RafGodwin Engineering.</p>'
 '<div class="gate-scroll">' + TERMS_TXT + '</div>'
 '<div class="gate-actions"><button class="btn btn-primary" id="tos-accept" type="button">Accept &amp; enter</button><button class="btn btn-outline" id="tos-decline" type="button">Decline</button><button class="btn btn-outline" id="tos-close" type="button" hidden>Close</button></div></div></div>'
 '<div class="gate" id="tos-blocked" hidden><div class="gate-card"><span class="eyebrow">Access declined</span><h2>You need to accept to continue</h2>'
 '<p class="gate-sub">We can only open the site once the Terms of Service are accepted. If you changed your mind you can review them again.</p>'
 '<div class="gate-actions"><button class="btn btn-primary" id="tos-again" type="button">Review terms again</button></div></div></div>')
HERO_BG = ('<section class="hero hero-video"><div class="hero-bg" aria-hidden="true"><video muted loop playsinline preload="auto" poster="assets/img/hero-solar.jpg">'
 '<source src="assets/video/hero.mp4" type="video/mp4"></video><canvas id="solarfx"></canvas></div>')
def post_head(h):
    return h.replace('</head><body>', FONTS + LOCK + '</head><body>' + GATE, 1)
def post_body(h, fname):
    h = h.replace('window.RG_PHONE=', 'window.RG_EMAIL="%s";window.RG_PHONE=' % EMAIL, 1)
    h = h.replace('<span>Call us: ', '<span><a href="mailto:%s">%s</a> &middot; Call: ' % (EMAIL, EMAIL), 1)
    h = h.replace('>WhatsApp us</a></li>', '>WhatsApp us</a></li><li><a href="mailto:%s">%s</a></li><li><a href="%s" target="_blank" rel="noopener">Review us on Google</a></li>' % (EMAIL, EMAIL, REVIEW_URL), 1)
    h = h.replace('<span class="credit">', '<span><a href="#terms" class="tos-open">Terms of Service</a></span><span class="credit">', 1)
    if fname == "index.html":
        h = h.replace('<section class="hero">', HERO_BG, 1)
        h = re.sub(r'<div class="video-box">.*?</video><div class="video-ph"[^>]*></div></div>', '', h, flags=re.S)
    if fname == "contact.html":
        h = h.replace('<div class="social">', '<div class="card" style="margin-top:16px"><h3>Email</h3><p><a href="mailto:%s" style="font-weight:700">%s</a></p><p style="margin-top:6px">WhatsApp: <a href="https://wa.me/%s">+233 55 112 0109</a></p></div><div class="social" style="margin-top:16px">' % (EMAIL, EMAIL, WA), 1)
        h = h.replace('</iframe></div>', '</iframe></div><p class="maplinks"><a class="btn btn-outline" href="%s" target="_blank" rel="noopener">Open in Google Maps</a></p>' % MAPS_URL, 1)
        h = h.replace('<section class="band">', '<section><div class="wrap" style="max-width:820px">' + reviews_cta() + '</div></section><section class="band">', 1)
    if fname == "about.html":
        h = re.sub(r'<section><div class="wrap"><div class="sec-head[^"]*"><span class="eyebrow">Our team</span>.*?</section>', '', h, flags=re.S)
    h = re.sub(r'<p style="font-size:\.8rem;margin-top:8px">Edit hours[^<]*</p>', '', h)
    h = h.replace('<div class="fab"><a class="wa"', '<div class="fab"><button class="raf-btn" id="raf-open" type="button" aria-label="Chat with RAF"><img src="assets/img/logo-mark.png" alt=""><span>RAF</span></button><a class="wa"', 1)
    if fname == "index.html":
        h = h.replace('Trusted by homes and businesses', 'Worked with us? Tell Google', 1).replace('Read all reviews', 'How reviewing works', 1)
    return h

def page(fname, title, desc, body, schema=False):
    h = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
      '<title>%s</title><meta name="description" content="%s"><meta name="theme-color" content="#101418">'
      '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="website">'
      '<link rel="icon" href="assets/img/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png"><link rel="icon" type="image/png" sizes="512x512" href="assets/img/favicon-512.png"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png"><link rel="stylesheet" href="assets/css/style.css">%s</head><body>'
      ) % (title, desc, title, desc, ('<script type="application/ld+json">%s</script>' % json.dumps(LD)) if schema else "")
    h = post_head(h)
    h += header(fname) + '<main id="main">' + body + '</main>' + footer()
    h += '<script>window.RG_WA="%s";window.RG_PHONE="%s";</script><script src="assets/js/main.js" defer></script><script src="js/cart.js" defer></script></body></html>' % (WA, PHONE_DISPLAY)
    h = post_body(h, fname)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(h)

def hero(crumb, h1, sub, cta=True):
    c = '<div class="cta"><a class="btn btn-primary" href="quote.html">Get a Free Quote</a><a class="btn btn-ghost" href="tel:%s">Call %s</a></div>' % (PHONE_TEL, PHONE_DISPLAY) if cta else ""
    return ('<section class="hero page-hero"><div class="wrap"><div><div class="crumbs"><a href="index.html">Home</a> / %s</div><h1>%s</h1><p>%s</p>%s</div></div></section>') % (crumb, h1, sub, c)

def band(t="Ready to protect and power your property?", s="Get a free site survey and a clear, itemised quote from our engineers."):
    return '<section class="band"><div class="wrap"><div><h2>%s</h2><p>%s</p></div><a class="btn btn-primary" href="quote.html">Request a Free Quote</a></div></section>' % (t, s)

def head(eyebrow, h, lead="", center=True):
    return '<div class="sec-head %s reveal"><span class="eyebrow">%s</span><h2>%s</h2>%s</div>' % ("center" if center else "", eyebrow, h, ('<p class="lead">%s</p>' % lead) if lead else "")

def cards(items, cols="g3", link=True):
    o = '<div class="grid %s">' % cols
    for it in items:
        icon, t, d = it[0], it[1], it[2]
        if link and len(it) > 3:
            o += '<a class="card reveal" href="%s">%s<h3>%s</h3><p>%s</p><span class="more">Learn more &rarr;</span></a>' % (it[3], ic(icon), t, d)
        else:
            o += '<div class="card hover reveal">%s<h3>%s</h3><p>%s</p></div>' % (ic(icon), t, d)
    return o + '</div>'

def ticks(items): return '<ul class="ticks">' + "".join("<li>%s</li>" % i for i in items) + "</ul>"

def media(img, cap):
    return '<div class="media reveal"><img src="assets/img/%s" alt="%s" loading="lazy" width="760" height="570"></div>' % (img, "RafGodwin Engineering installation")

def split(eyebrow, h, p, tk, img, cap, flip=False):
    txt = '<div class="reveal"><span class="eyebrow">%s</span><h2>%s</h2><p class="lead">%s</p>%s<p style="margin-top:22px"><a class="btn btn-primary" href="quote.html">Get a Quote</a></p></div>' % (eyebrow, h, p, ticks(tk))
    m = media(img, cap)
    return '<section><div class="wrap split">%s</div></section>' % ((m + txt) if flip else (txt + m))

TERMS = ('<div class="terms"><input type="checkbox" id="%s" name="terms" required><label for="%s">I accept the <a href="contact.html" target="_blank">Terms of Service</a> and consent to RafGodwin Engineering using my details to contact me about my enquiry.</label></div>')
def badge():
    return '<span class="badge" role="status"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">%s</svg>Terms Accepted &middot; Secured Compliance</span>' % I["shield"]
def submit(label, uid):
    return TERMS % (uid, uid) + '<div class="submit-row"><button class="btn btn-primary" type="submit" disabled>%s</button>%s</div><div class="msg" role="status"></div>' % (label, badge())

def fld(label, name, typ="text", req=True, ph="", extra=""):
    return '<div class="fld"><label for="%s_%s">%s%s</label><input id="%s_%s" name="%s" type="%s" %s placeholder="%s" %s><span class="err">Please check this field.</span></div>' % (extra or "f", name, label, " *" if req else "", extra or "f", name, label, typ, "required" if req else "", ph, 'autocomplete="%s"' % ("tel" if typ == "tel" else "name" if name == "Name" else "email" if typ == "email" else "off"))

def select(label, name, opts, req=True, uid="f"):
    o = '<option value="">Select...</option>' + "".join('<option>%s</option>' % x for x in opts)
    return '<div class="fld"><label for="%s_%s">%s%s</label><select id="%s_%s" name="%s" %s>%s</select><span class="err">Please choose an option.</span></div>' % (uid, name, label, " *" if req else "", uid, name, label, "required" if req else "", o)

SERVICES = ["Smart Home & Automation", "CCTV & Surveillance", "Electric Fencing", "Smart Locks & Gate Automation", "Residential Solar", "Commercial Energy / Solar", "Access Control", "Not sure yet"]
AREAS = ["Sowutuom / Kwashieman", "Ofankor / Achimota", "Accra Central", "East Legon / Airport", "Tema / Spintex", "Madina / Adenta", "Kasoa / Weija", "Kumasi", "Other region in Ghana"]

def home_form():
    return ('<form class="f" novalidate><h3 style="margin-bottom:6px">Book a Free Consultation</h3><p style="margin-bottom:18px;font-size:.92rem">Tell us what you need. We reply fast.</p>'
      + fld("Full name", "Name", "text", True, "", "h") + fld("Phone / WhatsApp", "Phone", "tel", True, "024 000 0000", "h")
      + select("Service needed", "Service", SERVICES, True, "h") + select("Location", "Location", AREAS, True, "h")
      + submit("Request Consultation", "terms_home") + '</form>')

def uid_x(x): return "text"

def sample_note(): return '<p style="text-align:center;font-size:.8rem;margin-top:14px">Sample wording shown &mdash; replace with approved client reviews before publishing.</p>'

SAMPLE_T = [
 ("Sample testimonial: add a real review from a homeowner about their smart home or CCTV installation.", "Client name", "Residential client, Accra"),
 ("Sample testimonial: add a real review about how solar kept the lights on during outages.", "Client name", "Solar client, Accra"),
 ("Sample testimonial: add a real review about gate automation, electric fencing or smart locks.", "Client name", "Security client, Accra"),
]
def slider():
    s = ""
    for q, n, r in SAMPLE_T:
        s += '<div class="slide"><div class="quote"><div class="stars" aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>%s</p><div class="by">%s<small>%s</small></div></div></div>' % (q, n, r)
    return '<div class="slider"><div class="track">%s</div><div class="dots"></div></div>' % s

# ---------------------------------------------------------------- PAGES
def p_home():
    b = ('<section class="hero"><div class="wrap"><div><span class="eyebrow" style="color:#5cc8ff">Smart Home &middot; Security &middot; Solar</span>'
      '<h1>Engineering the <em>smarter, safer, always-on</em> home in Ghana.</h1>'
      '<p>RafGodwin Engineering designs and installs smart automation, elite security and solar power systems that keep your property protected and powered, even when the grid is not.</p>'
      '<div class="cta"><a class="btn btn-primary" href="quote.html">Get a Free Quote</a><a class="btn btn-ghost" href="tel:%s">Call %s</a></div></div>'
      '<div class="video-box"><video autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-solar.jpg"><source src="assets/video/hero.mp4" type="video/mp4"></video>'
      '<div class="video-ph" style="background:none;pointer-events:none"></div></div></div></section>'
      '<div class="wrap"><div class="stats"><div class="stat"><b>900+</b><span>Clients served</span></div><div class="stat"><b>3</b><span>Core service lines</span></div><div class="stat"><b>Free</b><span>Site survey &amp; quote</span></div><div class="stat"><b>Ghana</b><span>Wide installations</span></div></div></div>'
      ) % (PHONE_TEL, PHONE_DISPLAY)
    b += '<section><div class="wrap">' + head("What we do", "Complete engineering for modern Ghanaian properties", "Three pillars, one accountable team, from survey and design to installation and support.") + cards([
      ("bulb", "Smart Home & Automation", "Lighting, appliances and climate controlled from one app or by voice.", "smart-home.html"),
      ("shield", "Security & Access Control", "CCTV, electric fencing, smart locks and gates working as one system.", "security.html"),
      ("sun", "Solar & Renewable Energy", "Hybrid and off-grid solar built for local grid instability.", "solar.html"),
      ("cam", "CCTV & Surveillance", "HD cameras, remote phone viewing and cloud storage.", "cctv.html"),
      ("lock", "Smart Locks & Gates", "Biometric keyless entry and motorised gate automation.", "smart-locks.html"),
      ("build", "Commercial Energy", "Large-scale solar and energy audits that cut business costs.", "commercial-energy.html")]) + '</div></section>'
    b += '<section class="alt"><div class="wrap split"><div class="reveal"><span class="eyebrow">Why RafGodwin</span><h2>Built to last. Backed by 900+ clients.</h2><p class="lead">We engineer around Ghana&rsquo;s real conditions: power cuts, heat, dust and tight budgets.</p>' + ticks(["Free site survey and itemised quotation", "Quality, certified equipment and tidy cabling", "Systems that keep working during blackouts", "Training and after-installation support"]) + '</div>' + media("hero-solar.jpg", "Solar array installed on an Accra rooftop") + '</div></section>'
    b += '<section><div class="wrap">' + head("Client voices", "Trusted by homes and businesses") + slider() + sample_note() + '<p class="center" style="margin-top:20px"><a class="btn btn-outline" href="testimonials.html">Read all reviews</a></p></div></section>'
    b += '<section class="dark"><div class="wrap split"><div class="reveal"><span class="eyebrow" style="color:#5cc8ff">Quick consultation</span><h2>Talk to an engineer today</h2><p class="lead">Share a few details and our team will call or WhatsApp you to plan a free site visit.</p>' + ticks(["No obligation", "Response within one working day", "Clear pricing, no hidden costs"]) + '</div><div style="color:var(--text)">' + home_form() + '</div></div></section>'
    page("index.html", "RafGodwin Engineering | Smart Home, Security & Solar in Accra, Ghana", "Premium smart home automation, CCTV, electric fencing, smart locks and solar engineering in Accra. 900+ clients. Get a free quote.", b, True)

def p_about():
    b = hero("About", "Modernising and protecting Ghanaian homes", "RafGodwin Engineering is an Accra-based engineering firm delivering automation, security and solar systems with precision and care.")
    b += split("Our mission", "Engineering peace of mind", "Our mission is to modernise and protect Ghanaian homes and businesses by making intelligent, secure and energy-independent living accessible. With 900+ clients served, we combine technical rigour with honest, local service.", ["Design around your property and budget", "Install with neat, safe, standards-based work", "Support you long after handover"], "hero-solar.jpg", "Our engineers at work in Accra")
    b += '<section class="alt"><div class="wrap">' + head("Our values", "What we stand for") + cards([("shield", "Integrity", "Honest advice and transparent pricing, always."), ("wrench", "Craftsmanship", "Clean installations engineered to last in our climate."), ("bolt", "Reliability", "Systems designed to keep working when the grid fails."), ("phone", "Service", "Responsive support before, during and after install.")], "g4", False) + '</div></section>'
    b += '<section><div class="wrap">' + head("Our team", "The engineers behind your system", "Replace the placeholders below with your real team photos and names.")
    b += '<div class="grid g3">' + "".join('<div class="card hover reveal center"><div class="media" style="aspect-ratio:1;max-width:160px;margin:0 auto;border-radius:50%%"></div><h3>Team member name</h3><p>%s</p></div>' % r for r in ["Founder & Lead Engineer", "Security Systems Engineer", "Solar & Energy Engineer"]) + '</div></div></section>'
    b += band()
    page("about.html", "About Us | RafGodwin Engineering", "Our mission to modernise and protect Ghanaian homes with smart automation, security and solar engineering.", b)

def p_l1(fname, crumb, h1, sub, intro_h, intro_p, tk, img, cap, tiles, title):
    b = hero(crumb, h1, sub) + split("Overview", intro_h, intro_p, tk, img, cap)
    b += '<section class="alt"><div class="wrap">' + head("Explore", "Solutions in this category") + cards(tiles) + '</div></section>' + band()
    page(fname, title, sub, b)

def p_smart():
    p_l1("smart-home.html", "Smart Home & Automation", "One unified, intelligent home", "Automated lighting, smart appliances and climate integration, controlled from your phone or by voice.",
      "Unified smart residential living", "We connect lighting, appliances, air-conditioning, curtains, gates and security into a single platform so your home responds to you, saves energy and stays safe.",
      ["Scene-based lighting and dimming", "Smart appliance and socket control", "Climate and AC scheduling to cut power bills", "Voice and app control, with local backup when internet drops"], "smart-lock.jpg", "Smart entry hardware we install",
      [("bulb", "Automated Lighting", "Schedules, motion and scenes for every room."), ("bolt", "Smart Appliances", "Control geysers, pumps and sockets remotely."), ("wifi", "Climate Integration", "Smart AC control that reduces energy waste."), ("lock", "Smart Locks & Gates", "Entry that fits your automation.", "smart-locks.html")], "Smart Home Automation in Accra | RafGodwin Engineering")

def p_security():
    p_l1("security.html", "Security & Access Control", "Full-scale perimeter and entry protection", "Layered security frameworks from the fence line to the front door.",
      "Protection in layers", "Strong security works in layers: deter at the perimeter, detect on approach, verify with cameras and control every entry. We design and integrate all layers to work together.",
      ["Perimeter deterrence with electric fencing", "HD CCTV with remote viewing", "Biometric locks and access control", "Automated gates and intercoms"], "smart-lock.jpg", "Biometric smart lock installation",
      [("cam", "CCTV & Surveillance", "Cameras, remote viewing and cloud storage.", "cctv.html"), ("gate", "Electric Fencing", "Professional perimeter protection and monitoring.", "electric-fencing.html"), ("lock", "Smart Locks & Gates", "Keyless biometric entry and motorised gates.", "smart-locks.html")], "Security & Access Control in Accra | RafGodwin Engineering")

def p_solar():
    p_l1("solar.html", "Solar & Renewable Energy", "Power that does not depend on the grid", "Custom solar configurations built to handle Ghana's grid instability.",
      "Custom solar for real-world conditions", "Outages and voltage swings are part of daily life. We size and engineer hybrid and off-grid systems around your actual load so essentials stay on and bills come down.",
      ["Load analysis and honest system sizing", "Hybrid, off-grid and grid-tied options", "Quality panels, inverters and batteries", "Neat roof mounting and safe cabling"], "hero-solar.jpg", "Rooftop solar array in Accra",
      [("panel", "Residential Solar Packages", "Complete home systems for Ghanaian households.", "residential-solar.html"), ("build", "Commercial Energy Engineering", "Large deployments and energy audits.", "commercial-energy.html"), ("bolt", "Backup Power", "Keep security and essentials running in blackouts.", "quote.html")], "Solar & Renewable Energy in Ghana | RafGodwin Engineering")

def p_cctv():
    p_l1("cctv.html", "CCTV & Surveillance", "See your property from anywhere", "Advanced HD security camera networks with remote mobile viewing and cloud storage.",
      "High-definition surveillance engineered end to end", "We plan camera positions for real coverage, cable cleanly, and set up secure remote viewing so you can check in from your phone in seconds.",
      ["HD and night-vision cameras", "Live and playback on iOS and Android", "Cloud and local recorder storage", "Motion alerts and smart detection", "UPS or solar backup so cameras stay on"], "hero-solar.jpg", "Professional camera installation",
      [("cam", "Camera Networks", "IP and analogue HD systems for homes and sites."), ("phone", "Remote Viewing", "Secure app access from anywhere."), ("chart", "Cloud Storage", "Offsite footage retention and backup."), ("shield", "Maintenance", "Cleaning, checks and upgrades.")], "CCTV & Surveillance Systems Accra | RafGodwin Engineering")

def p_fence():
    p_l1("electric-fencing.html", "Electric Fencing & Perimeters", "A visible, powerful first line of defence", "Professional-grade electric fence installations with physical perimeter monitoring.",
      "Deter before they reach your door", "Our electric fences are installed to safety standards with proper earthing, warning signage and energiser sizing, and can be linked to alarms and cameras for monitoring.",
      ["Wall-top and freestanding fence systems", "Alarm-linked energisers with alerts", "Safe earthing and warning signage", "Solar or battery backup for continuous protection"], "smart-lock.jpg", "Perimeter security hardware",
      [("gate", "Wall-top Fencing", "Fast deterrence on existing walls."), ("shield", "Alarm Integration", "Alerts when the fence is tampered with."), ("cam", "Camera Pairing", "Verify intrusions visually."), ("wrench", "Servicing", "Regular testing and repairs.")], "Electric Fencing Installation Accra | RafGodwin Engineering")

def p_locks():
    p_l1("smart-locks.html", "Smart Locks & Gate Automation", "Keyless entry. Total control.", "Biometric entry, remote lock tracking and automated motorised gates.",
      "Entry that knows who is at the door", "Fingerprint, PIN, card and app access with activity logs, plus motorised gates that open for you and stay shut for everyone else.",
      ["Fingerprint, PIN, card and app unlock", "Remote lock status and access history", "Temporary codes for guests and staff", "Sliding and swing gate motors with remote and app control"], "smart-lock.jpg", "Smart lock with fingerprint, keypad and camera",
      [("lock", "Biometric Smart Locks", "Keyless entry with fingerprint and PIN."), ("phone", "Remote Tracking", "See who came and went from your phone."), ("gate", "Gate Automation", "Motorised sliding and swing gates."), ("shield", "Access Control", "Multi-user permissions for estates and offices.")], "Smart Locks & Gate Automation Accra | RafGodwin Engineering")

def p_resolar():
    p_l1("residential-solar.html", "Residential Solar Packages", "Home solar built for Ghana", "Hybrid and off-grid solar infrastructure tailored to Ghanaian homes.",
      "Choose the package that fits your home", "Every home is different, so we survey your appliances and roof, then recommend a package and show the expected backup time before you commit.",
      ["Essentials package: lights, TV, fans, Wi-Fi", "Comfort package: adds fridge, pump, selected AC", "Whole-home hybrid with battery storage", "Off-grid systems for remote properties"], "hero-solar.jpg", "Residential rooftop solar installation",
      [("panel", "Essentials Backup", "Keep lights, fans, TV and internet running."), ("bolt", "Comfort Hybrid", "Add fridge, water pump and more."), ("sun", "Whole-Home Hybrid", "Maximum independence with battery storage."), ("wrench", "Care Plans", "Inspection, cleaning and battery checks.")], "Residential Solar Packages Ghana | RafGodwin Engineering")

def p_comm():
    p_l1("commercial-energy.html", "Commercial Energy Engineering", "Cut energy costs. Protect operations.", "Large-scale solar deployments and energy optimisation audits for local businesses.",
      "Energy engineering for business", "From shops and offices to schools and factories, we analyse your consumption, design the right solar and storage system, and show the payback before you invest.",
      ["Energy audit and load profiling", "Large rooftop and ground-mount solar", "Hybrid systems with generator integration", "Monitoring dashboards and maintenance contracts"], "hero-solar.jpg", "Large-scale rooftop solar",
      [("chart", "Energy Audits", "Find waste and quantify savings."), ("build", "Commercial Solar", "Sized to your tariff and load."), ("bolt", "Backup & Hybrid", "Protect uptime during outages."), ("wrench", "O&M Contracts", "Scheduled maintenance and support.")], "Commercial Solar & Energy Engineering Ghana | RafGodwin Engineering")

def p_portfolio():
    items = [
      ("solar", "Rooftop solar array", "Accra", "hero-solar.jpg"),
      ("security", "Smart lock installation", "Accra", "smart-lock.jpg"),
      ("shop", "Our shopfront", "Sowutuom, Accra", "gallery-01.jpg"),
      ("shop", "Security showroom", "Cameras, recorders and locks in stock", "gallery-05.jpg"),
      ("cctv", "Solar PTZ cameras", "Ausno 4G solar cameras", "gallery-08.jpg"),
      ("cctv", "Solar &amp; dual-lens cameras", "Wireless, solar-powered CCTV", "gallery-12.jpg"),
      ("cctv", "Wi-Fi and dome cameras", "Panorama and Dahua dome cameras", "gallery-04.jpg"),
      ("security", "Intelligent fingerprint locks", "Smart locks for homes and offices", "gallery-03.jpg"),
      ("security", "Automatic smart locks", "Waterproof and fingerprint models", "gallery-06.jpg"),
      ("fence", "Fencing accessories", "Insulators and fittings", "gallery-02.jpg"),
      ("fence", "Tension springs", "Gate and fence hardware", "gallery-10.jpg"),
      ("fence", "Fence and gate fittings", "Ready for installation", "gallery-11.jpg"),
      ("fence", "Wire stock", "Perimeter and fencing wire", "gallery-07.jpg"),
      ("shop", "Equipment in stock", "Housings and fittings", "gallery-09.jpg"),
    ]
    cats = [("solar", "Solar"), ("security", "Smart locks"), ("cctv", "CCTV"), ("fence", "Fencing & Gates"), ("shop", "Our Shop")]
    shots = ""
    for c, t, loc, img in items:
        shots += '<div class="shot reveal" data-c="%s"><img src="assets/img/%s" alt="%s" loading="lazy"><div><b>%s</b><small>%s</small></div></div>' % (c, img, t.replace("&amp;", "and"), t, loc)
    fl = '<div class="filters"><button class="on" data-f="all">All</button>' + "".join('<button data-f="%s">%s</button>' % c for c in cats) + '</div>'
    b = hero("Gallery", "Our work and our shop", "A look at our installations, products and showroom in Sowutuom, Accra.", False)
    b += '<section><div class="wrap">%s<div class="grid g3">%s</div></div></section>' % (fl, shots) + band()
    page("portfolio.html", "Gallery | RafGodwin Engineering", "Browse photos of RafGodwin Engineering's smart locks, CCTV, solar cameras, fencing materials and showroom in Accra.", b)

def p_testi():
    b = hero("Reviews", "What our 900+ clients say", "Real feedback from homeowners and businesses across Ghana.", False)
    b += '<section><div class="wrap">' + head("Written reviews", "Client testimonials") + '<div class="grid g3">'
    for q, n, r in SAMPLE_T * 2:
        b += '<div class="card hover reveal"><div class="stars" style="color:#f5b301">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p style="color:var(--text)">%s</p><p style="margin-top:12px"><b style="color:var(--navy)">%s</b><br><small>%s</small></p></div>' % (q, n, r)
    b += '</div>' + sample_note() + '</div></section>'
    b += '<section class="alt"><div class="wrap">' + head("Video case studies", "See it in the client&rsquo;s own words") + '<div class="grid g3">'
    for i in range(3):
        b += '<div class="video-box reveal" style="border-color:var(--line)"><div class="video-ph"><div><div class="play"><svg width="26" height="26" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></div><b>Video case study %d</b>Embed YouTube / TikTok / MP4</div></div></div>' % (i + 1)
    b += '</div></div></section>' + band()
    page("testimonials.html", "Client Testimonials | RafGodwin Engineering", "Read reviews and video case studies from RafGodwin Engineering's 900+ clients.", b)

FAQS = [
 ("How often does my system need maintenance?", "Cameras, locks and fences should be inspected about every 6 months; solar panels cleaned every 3-6 months (more often in harmattan dust); and batteries checked yearly. We offer care plans."),
 ("Do I need good internet for smart home and CCTV?", "Remote viewing needs a stable connection. A typical home needs 5-10 Mbps upload for a few cameras. Local control and recording continue even when the internet is down."),
 ("Will my security and smart devices work during a blackout?", "Yes, if designed for it. We add UPS or solar-battery backup for cameras, routers, locks, gate motors and energisers so protection continues during outages."),
 ("How long will solar and batteries last?", "Quality panels last 20+ years; lithium batteries typically 8-12 years depending on use; inverters 8-10 years. Proper sizing and care extend life."),
 ("Is electric fencing safe?", "Yes, when installed to standard. Energisers deliver short, high-voltage, low-current pulses, with correct earthing, warning signs and clearances."),
 ("Can I control everything from my phone?", "Yes. Lighting, locks, gates, cameras and solar monitoring can be viewed and controlled by app, and many by voice."),
 ("How do I get a quote?", "Use our Request a Quote page or call %s. We offer a free site survey and send an itemised quotation." % PHONE_DISPLAY),
]
def p_faq():
    b = hero("FAQs", "Smart home FAQs", "Straight answers on maintenance, internet needs and backup power.", False)
    b += '<section><div class="wrap" style="max-width:860px"><div class="faq">' + "".join('<details class="reveal"><summary>%s</summary><p>%s</p></details>' % f for f in FAQS) + '</div><p class="center" style="margin-top:28px">Still have a question? <a href="contact.html">Contact us</a></p></div></section>' + band()
    page("faq.html", "Smart Home FAQs | RafGodwin Engineering", "Answers about smart home maintenance, internet requirements and backup power during blackouts in Ghana.", b)
    return

def p_quote():
    chips = lambda name, opts: '<div class="chips">' + "".join('<label><input type="checkbox" name="%s" value="%s"><span>%s</span></label>' % (name, o, o) for o in opts) + '</div>'
    f = ('<form class="f" novalidate><div class="progress" aria-hidden="true"><i></i></div><h3 style="margin-bottom:18px">Tell us about your project</h3><div class="row">'
      + fld("Full name", "Name", "text", True, "", "q") + fld("Phone / WhatsApp", "Phone", "tel", True, "024 000 0000", "q") + '</div>'
      + fld("Email (optional)", "Email", "email", False, "", "q")
      + '<div class="row">' + select("Location", "Location", AREAS, True, "q") + select("Property type", "Property", ["Home / Apartment", "Estate / Gated community", "Shop / Office", "School / Church", "Factory / Warehouse"], True, "q") + '</div>'
      + '<div class="fld"><label>Services needed (select all that apply)</label>' + chips("Services", SERVICES[:7]) + '</div>'
      + '<div class="row">' + select("Budget range", "Budget", ["Under GH₵5,000", "GH₵5,000 - 15,000", "GH₵15,000 - 50,000", "GH₵50,000 - 150,000", "Above GH₵150,000", "Not sure"], True, "q") + select("Timeline", "Timeline", ["Urgent (this week)", "Within a month", "1-3 months", "Just planning"], True, "q") + '</div>'
      + '<div class="fld"><label for="q_Details">Project details (optional)</label><textarea id="q_Details" name="Details" rows="4" placeholder="e.g. 3-bedroom house, want CCTV and backup power for essentials"></textarea></div>'
      + submit("Submit Quote Request", "terms_quote") + '</form>')
    b = hero("Request a Quote", "Request your free quote", "Answer a few questions so we can match you with the right engineer and an accurate estimate.", False)
    b += '<section><div class="wrap split" style="align-items:start"><div class="reveal"><span class="eyebrow">How it works</span><h2>From enquiry to installation</h2><div class="grid steps" style="margin-top:22px">'
    for t, d in [("Submit", "Complete the short form."), ("Survey", "We visit and measure, free."), ("Quote", "Receive an itemised proposal."), ("Install", "Our engineers deliver and train you.")]:
        b += '<div class="card"><h3 style="margin-top:0">%s</h3><p>%s</p></div>' % (t, d)
    b += '</div></div><div>%s</div></div></section>' % f
    page("quote.html", "Request a Free Quote | RafGodwin Engineering", "Request a free quote for smart home, security or solar installation in Ghana. Filter by budget, location and requirements.", b)

def p_contact():
    b = hero("Contact", "Let&rsquo;s talk about your project", "Visit us, call, or message on WhatsApp. We respond quickly.", False)
    b += ('<section><div class="wrap split" style="align-items:start"><div class="reveal"><span class="eyebrow">Get in touch</span><h2>RafGodwin Engineering</h2>'
      '<div class="grid" style="margin-top:20px"><div class="card">%s<h3>Call us</h3><p><a href="tel:%s" style="font-size:1.2rem;font-weight:700">%s</a></p></div>'
      '<div class="card">%s<h3>Visit our office</h3><p>%s</p></div>'
      '<div class="card"><h3>Operating hours</h3><table class="hours"><tr><td>Monday - Friday</td><td>8:00 am - 6:00 pm</td></tr><tr><td>Saturday</td><td>9:00 am - 4:00 pm</td></tr><tr><td>Sunday</td><td>Closed</td></tr></table><p style="font-size:.8rem;margin-top:8px">Edit hours to match your schedule.</p></div></div>'
      '<div class="social"><a class="btn btn-primary" href="%s" target="_blank" rel="noopener">Instagram</a><a class="btn btn-primary" href="%s" target="_blank" rel="noopener">TikTok</a><a class="btn btn-outline" href="https://wa.me/%s">WhatsApp</a></div></div>'
      '<div class="reveal"><div class="mapbox"><iframe title="RafGodwin Engineering location map" src="%s" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></div></div></section>'
      ) % (ic("phone"), PHONE_TEL, PHONE_DISPLAY, ic("build"), ADDRESS, INSTAGRAM, TIKTOK, WA, MAP)
    b += band()
    page("contact.html", "Contact Us | RafGodwin Engineering", "Contact RafGodwin Engineering in Sowutuom, Accra. Call 024 711 7982 or message on WhatsApp.", b)


# ================= PREMIUM OVERRIDES =================
GSVG = '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="#fff" d="M21.6 12.2c0-.7-.1-1.3-.2-1.9H12v3.7h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.300 3-7.300z"/><path fill="#fff" d="M12 22c2.700 0 5-.9 6.600-2.500l-3.200-2.500c-.9.600-2 1-3.400 1-2.600 0-4.800-1.800-5.600-4.100H3.100v2.600A10 10 0 0 0 12 22z" opacity=".85"/><path fill="#fff" d="M6.400 14c-.2-.6-.3-1.300-.3-2s.1-1.400.3-2V7.400H3.100a10 10 0 0 0 0 9.200z" opacity=".7"/><path fill="#fff" d="M12 5.900c1.500 0 2.800.5 3.800 1.500l2.900-2.900A10 10 0 0 0 3.100 7.400L6.400 10c.8-2.300 3-4.100 5.600-4.100z" opacity=".95"/></svg>'
STARS_O = '<span class="stars-o" aria-hidden="true">' + '<svg viewBox="0 0 24 24"><path d="M12 3.500l2.600 5.400 5.900.8-4.300 4.100 1 5.900L12 16.900 6.800 19.700l1-5.900L3.500 9.700l5.900-.8z"/></svg>'*5 + '</span>'

def reviews_cta():
    return ('<div class="review-card reveal">%s<h3>Review us on Google</h3>'
      '<p>Worked with RafGodwin Engineering? A short review on Google Maps helps other families and businesses in Ghana find a team they can trust.</p>'
      '<div class="cta"><a class="btn btn-primary" href="%s" target="_blank" rel="noopener">%s Leave a Google review</a>'
      '<a class="btn btn-outline" href="%s" target="_blank" rel="noopener">View us on Google Maps</a></div>'
      '<small>Opens Google Maps. Tap &ldquo;Write a review&rdquo; on our listing.</small></div>') % (STARS_O, REVIEW_URL, GSVG, MAPS_URL)

def slider(): return reviews_cta()
def sample_note(): return ''

def submit(label, uid):
    return ('<div class="submit-row"><button class="btn btn-primary" type="submit" data-via="wa">Send on WhatsApp</button>'
            '<button class="btn btn-outline" type="submit" data-via="mail">Email a copy instead</button></div>'
            '<p class="fine">Your request goes to our team on WhatsApp or to %s. Whichever you choose, we reply within one working day.</p>'
            '<div class="msg" role="status" aria-live="polite"></div>') % EMAIL

def p_testi():
    b = hero("Reviews", "Tell us how we did", "Your Google review helps other homes and businesses in Ghana find a team they can trust.", False)
    b += '<section><div class="wrap" style="max-width:820px">' + reviews_cta() + '</div></section>'
    b += '<section class="alt"><div class="wrap">' + head("How it works", "Reviewing takes under a minute") + '<div class="grid g3">'
    for n, t, d in [("1", "Open our listing", "Tap the review button. Google Maps opens on our business page."), ("2", "Pick your rating", "Choose the stars that reflect your experience."), ("3", "Share a few words", "Mention the service we did for you and post it.")]:
        b += '<div class="card"><span class="num">%s</span><h3>%s</h3><p>%s</p></div>' % (n, t, d)
    b += '</div></div></section>' + band()
    page("testimonials.html", "Reviews | RafGodwin Engineering", "Review RafGodwin Engineering on Google Maps.", b)


for fn in [p_home, p_about, p_smart, p_security, p_solar, p_cctv, p_fence, p_locks, p_resolar, p_comm, p_portfolio, p_testi, p_faq, p_quote, p_contact]:
    fn()

print("Built", len([f for f in os.listdir(OUT) if f.endswith(".html")]), "pages")
