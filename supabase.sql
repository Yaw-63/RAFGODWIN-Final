-- RafGodwin Shop: run this whole file in Supabase > SQL Editor > New query > Run

create table if not exists public.products (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  slug text unique,
  category text check (category in ('Smart Home','Security','Solar')),
  price numeric not null default 0,
  old_price numeric,
  stock int not null default 0,
  description text,
  image_url text,
  badge text,
  featured boolean default false,
  created_at timestamptz default now()
);

create table if not exists public.orders (
  id uuid primary key default gen_random_uuid(),
  order_number text unique not null,
  customer_name text, customer_phone text, customer_email text,
  region text, city text, address text,
  items jsonb not null default '[]',
  subtotal numeric, delivery_fee numeric, total numeric,
  payment_method text, payment_status text default 'pending', order_status text default 'pending',
  paystack_reference text,
  created_at timestamptz default now()
);

alter table public.products enable row level security;
alter table public.orders   enable row level security;

drop policy if exists "products public read"  on public.products;
drop policy if exists "products auth write"   on public.products;
drop policy if exists "orders public insert"  on public.orders;
drop policy if exists "orders auth read"      on public.orders;
drop policy if exists "orders auth update"    on public.orders;
drop policy if exists "orders auth delete"    on public.orders;

create policy "products public read" on public.products for select using (true);
create policy "products auth write"  on public.products for all to authenticated using (true) with check (true);
create policy "orders public insert" on public.orders for insert to anon, authenticated with check (true);
create policy "orders auth read"     on public.orders for select to authenticated using (true);
create policy "orders auth update"   on public.orders for update to authenticated using (true) with check (true);
create policy "orders auth delete"   on public.orders for delete to authenticated using (true);

-- Lets the checkout reduce stock without giving the public write access to products
create or replace function public.decrement_stock(items jsonb)
returns void language plpgsql security definer set search_path = public as $$
declare i jsonb;
begin
  for i in select * from jsonb_array_elements(items) loop
    update public.products set stock = greatest(stock - (i->>'qty')::int, 0) where id = (i->>'id')::uuid;
  end loop;
end $$;
grant execute on function public.decrement_stock(jsonb) to anon, authenticated;

-- Public image bucket
insert into storage.buckets (id, name, public) values ('products-images','products-images',true) on conflict (id) do nothing;
drop policy if exists "images public read"  on storage.objects;
drop policy if exists "images auth write"   on storage.objects;
drop policy if exists "images auth update"  on storage.objects;
drop policy if exists "images auth delete"  on storage.objects;
create policy "images public read" on storage.objects for select using (bucket_id='products-images');
create policy "images auth write"  on storage.objects for insert to authenticated with check (bucket_id='products-images');
create policy "images auth update" on storage.objects for update to authenticated using (bucket_id='products-images');
create policy "images auth delete" on storage.objects for delete to authenticated using (bucket_id='products-images');

-- 20 demo products (delete them in the admin panel when you add your own)
insert into public.products (name,slug,category,price,old_price,stock,description,image_url,badge,featured) values
('Smart WiFi Wall Switch 1-Gang','smart-wifi-wall-switch-1-gang','Smart Home',250,300,40,'Touch WiFi switch, works with Alexa & Google, app control.','https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=700&q=70','New',true),
('Smart WiFi Wall Switch 2-Gang','smart-wifi-wall-switch-2-gang','Smart Home',320,380,35,'Two-gang touch switch with timers and scenes.','https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=700&q=70',null,false),
('Smart WiFi Wall Switch 3-Gang','smart-wifi-wall-switch-3-gang','Smart Home',380,null,30,'Three-gang smart switch, neutral wire required.','https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=700&q=70','Popular',false),
('Smart Plug 16A with Energy Monitor','smart-plug-16a-with-energy-monitor','Smart Home',180,220,60,'Control and track power use of any appliance.','https://images.unsplash.com/photo-1585771724684-38269d6639fd?auto=format&fit=crop&w=700&q=70',null,false),
('Smart Video Doorbell','smart-video-doorbell','Smart Home',650,800,20,'1080p doorbell with two-way audio and motion alerts.','https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=700&q=70','Sale',true),
('Smart Home Hub Gateway','smart-home-hub-gateway','Smart Home',420,null,25,'Zigbee/Bluetooth gateway connecting all your devices.','https://images.unsplash.com/photo-1558089687-f282ffcbc126?auto=format&fit=crop&w=700&q=70',null,false),
('4-Camera CCTV Kit (1080p)','4-camera-cctv-kit-1080p-','Security',2500,2900,12,'4 cameras, 4-channel DVR, 1TB HDD and cables.','https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?auto=format&fit=crop&w=700&q=70','Best Seller',false),
('8-Camera CCTV Kit (2MP)','8-camera-cctv-kit-2mp-','Security',3600,4000,8,'8 cameras, 8-channel DVR, 2TB HDD, night vision.','https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?auto=format&fit=crop&w=700&q=70',null,false),
('8-Camera Colour Night CCTV Kit','8-camera-colour-night-cctv-kit','Security',4200,null,6,'Full-colour night vision, remote phone viewing.','https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?auto=format&fit=crop&w=700&q=70','Premium',true),
('Solar WiFi Security Camera','solar-wifi-security-camera','Security',780,950,22,'Wire-free outdoor camera with solar panel.','https://images.unsplash.com/photo-1580894732444-8ecded7900cd?auto=format&fit=crop&w=700&q=70',null,false),
('Fingerprint Smart Door Lock','fingerprint-smart-door-lock','Security',1450,1700,15,'Fingerprint, PIN, card and key access.','https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=700&q=70','Popular',false),
('Electric Fence Energizer 10km','electric-fence-energizer-10km','Security',1900,null,10,'Perimeter energizer with alarm output and keypad.','https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=700&q=70',null,false),
('Solar Panel 200W Mono','solar-panel-200w-mono','Solar',1100,1250,30,'High-efficiency monocrystalline panel.','https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=700&q=70',null,true),
('Solar Panel 450W Mono','solar-panel-450w-mono','Solar',1800,2000,18,'Heavy-duty 450W panel for home systems.','https://images.unsplash.com/photo-1509391366360-2e959784a276?auto=format&fit=crop&w=700&q=70','Best Seller',false),
('Hybrid Inverter 3.5kVA','hybrid-inverter-3-5kva','Solar',2200,2500,10,'3.5kVA hybrid inverter with built-in MPPT.','https://images.unsplash.com/photo-1558449028-b53a39d100fc?auto=format&fit=crop&w=700&q=70',null,false),
('Hybrid Inverter 5kVA','hybrid-inverter-5kva','Solar',3900,4300,8,'5kVA hybrid, WiFi monitoring, 48V.','https://images.unsplash.com/photo-1558449028-b53a39d100fc?auto=format&fit=crop&w=700&q=70','Popular',false),
('Hybrid Inverter 10kVA','hybrid-inverter-10kva','Solar',6500,null,4,'10kVA three-phase ready hybrid inverter.','https://images.unsplash.com/photo-1558449028-b53a39d100fc?auto=format&fit=crop&w=700&q=70','Premium',true),
('Lithium Battery 5kWh 48V','lithium-battery-5kwh-48v','Solar',5800,6400,7,'LiFePO4 rack battery, 6000+ cycles.','https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?auto=format&fit=crop&w=700&q=70',null,false),
('Gel Battery 200Ah 12V','gel-battery-200ah-12v','Solar',2100,2400,14,'Deep-cycle gel battery for solar storage.','https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?auto=format&fit=crop&w=700&q=70',null,false),
('MPPT Solar Charge Controller 60A','mppt-solar-charge-controller-60a','Solar',650,780,25,'60A MPPT controller with LCD display.','https://images.unsplash.com/photo-1558449028-b53a39d100fc?auto=format&fit=crop&w=700&q=70',null,false)
on conflict (slug) do nothing;
