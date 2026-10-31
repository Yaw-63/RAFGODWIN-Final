# RafGodwin Shop – Setup (about 15 minutes)

Your existing pages are unchanged except for a **Shop** menu link and a cart icon in the header. Everything else is new files.

## 1. Create the Supabase project
1. Go to supabase.com, create a free account and click **New project**.
2. Open **SQL Editor → New query**, paste all of `supabase.sql`, click **Run**. This creates the tables, security rules, stock function, the public `products-images` bucket and 20 demo products.

## 2. Paste your URL and key
Open `js/supabase.js`. In Supabase go to **Project Settings → API** and copy:
- **Project URL** → replace `https://YOUR_SUPABASE_URL.supabase.co`
- **anon public key** → replace `YOUR_ANON_KEY`

Until you do this, the shop shows the built-in demo products and admin says "not configured".

## 3. Create your admin user
Supabase → **Authentication → Users → Add user → Create new user**. Enter your email and a strong password, tick **Auto Confirm User**. Then sign in at `/admin-login.html`.
Also turn OFF public sign-ups (**Authentication → Providers → Email → disable "Allow new users to sign up"**), because any signed-in user can edit the shop.

## 4. Paystack
1. Create an account at paystack.com and copy your **Test public key** (Settings → API Keys).
2. In `js/supabase.js` replace `pk_test_xxxx` with it.
3. Test: add a product to the cart, checkout, press **Pay**. Test MoMo numbers and test cards are listed at paystack.com/docs/payments/test-payments. Check **Transactions** in the Paystack dashboard and **Orders** in `/admin.html`.
4. Going live: swap in your `pk_live_...` key once Paystack approves your business.

## 5. Adding products
`/admin.html` → Products → **+ Add Product**, upload an image and Save. It appears on `shop.html` straight away, with no redeploy.

## 6. Deploy
Upload the whole folder to Netlify as before. New files: `shop.html product.html cart.html checkout.html order-success.html admin-login.html admin.html`, `js/`, `assets/css/shop.css`, `supabase.sql`.

## Good to know
- Orders are now confirmed on the server (see GO-LIVE.md). Delivery fees are in three places that must match: `js/paystack.js`, `assets/js/main.js` (RAF) and `netlify/functions/_shared.js`.
- Delivery fees by region are in `js/paystack.js` (`REGIONS`).
- `build.py` was updated so rebuilding the site keeps the Shop link and cart icon.
