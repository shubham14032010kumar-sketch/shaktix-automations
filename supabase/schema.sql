-- ==========================================================
-- SHAKTIX AUTOMATIONS - SUPABASE COMPLETE DATABASE SCHEMA
-- Project ID: dcbpqapojfxacpvjobyp
-- Host: db.dcbpqapojfxacpvjobyp.supabase.co
-- ==========================================================

-- 1. Leads Table (Extracted Google Maps / Local Businesses)
CREATE TABLE IF NOT EXISTS public.leads (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    location TEXT,
    category TEXT,
    address TEXT,
    pitch_message TEXT,
    status TEXT DEFAULT 'Ready',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for fast phone and status queries
CREATE INDEX IF NOT EXISTS idx_leads_phone ON public.leads(phone);
CREATE INDEX IF NOT EXISTS idx_leads_status ON public.leads(status);

-- 2. Customer Inquiries & Free Demo Bookings
CREATE TABLE IF NOT EXISTS public.customer_queries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_name TEXT NOT NULL,
    customer_phone TEXT NOT NULL,
    business_type TEXT,
    city TEXT,
    message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Software Orders & Package Purchases
CREATE TABLE IF NOT EXISTS public.orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_name TEXT NOT NULL,
    customer_email TEXT,
    customer_phone TEXT NOT NULL,
    plan_tier TEXT NOT NULL,
    amount_inr NUMERIC(10,2) NOT NULL,
    payment_status TEXT DEFAULT 'Pending',
    payment_gateway TEXT,
    payment_id TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Software License Keys
CREATE TABLE IF NOT EXISTS public.licenses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    license_key TEXT UNIQUE NOT NULL,
    customer_phone TEXT,
    device_id TEXT,
    max_devices INT DEFAULT 1,
    status TEXT DEFAULT 'Active',
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Machine Logs (Campaign Auditing & Anti-Ban Telemetry)
CREATE TABLE IF NOT EXISTS public.machine_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    device_id TEXT,
    action_type TEXT,
    log_level TEXT DEFAULT 'INFO',
    payload JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
