-- Run once in Supabase > SQL Editor, AFTER the Netlify functions are deployed and PAYSTACK_SECRET_KEY / SUPABASE_SERVICE_ROLE_KEY are set.
-- Orders are now created only by the server (after Paystack confirms the payment), so the public can no longer insert orders or change stock.

drop policy if exists "orders public insert" on public.orders;
revoke execute on function public.decrement_stock(jsonb) from anon, authenticated;

-- One order per Paystack payment (stops duplicates when the browser and the webhook both report the same payment)
create unique index if not exists orders_paystack_reference_key on public.orders (paystack_reference) where paystack_reference is not null;
