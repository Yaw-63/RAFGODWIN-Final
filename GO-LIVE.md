# Go-live checklist (domain, Netlify, Paystack, Google)

## 1. Deploy so the functions run
Netlify Functions need a Git or CLI deploy (drag-and-drop of a plain folder may skip them).
Easiest: put this folder in a GitHub repo, then Netlify > Add new site > Import from Git. `netlify.toml` already sets everything.

## 2. Environment variables (Netlify > Site configuration > Environment variables)
| Name | Where to get it |
|---|---|
| `PAYSTACK_SECRET_KEY` | Paystack > Settings > API Keys (`sk_live_...` when live). Never put this in the site files. |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase > Project Settings > API > `service_role` secret. Never put this in the site files. |
| `SUPABASE_URL` (optional) | Only if different from the one in `js/supabase.js` |
Redeploy after adding them.

## 3. Paystack
1. In `js/supabase.js` set `PAYSTACK_PUBLIC_KEY` to your `pk_live_...` key.
2. Paystack > Settings > API Keys & Webhooks > set **Live Webhook URL** to `https://YOURDOMAIN/.netlify/functions/paystack-webhook`.
3. Make a real GHS 1 test purchase. It should appear in Paystack, in `admin.html` > Orders as **paid**, and stock should drop.
   An order marked **review** means the amount paid did not match the real price: check it by hand.

## 4. Lock down orders (after step 3 works)
Run `supabase-secure-orders.sql` in the Supabase SQL Editor. Do not run it before the functions work, or checkout will fail.
Supabase > Authentication > URL Configuration: set Site URL to your domain.

## 5. Domain
Netlify > Domain management > Add domain. Use Netlify DNS (change nameservers at your registrar) and enable HTTPS.
If the domain is not rafgodwin.com run: `python3 seo.py https://yourdomain.com` and redeploy.

## 6. Google
- Search Console > Add property > Domain > add the TXT record in DNS > Verify.
- Sitemaps > submit `sitemap.xml` and `sitemap-products.xml`.
- URL Inspection > Request indexing for the home, shop and service pages.
- Create a Google Business Profile for the Sowutoum office.
