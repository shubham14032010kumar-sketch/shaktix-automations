/**
 * Shaktix Automations - Supabase Live Client
 * Directly synchronizes Web Portal, Lead Dispatcher & Cloud Database
 */

const SUPABASE_CONFIG = {
  url: "https://dcbpqapojfxacpvjobyp.supabase.co",
  anonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRjYnBxYXBvamZ4YWNwdmpvYnlwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk4MDM4MjAsImV4cCI6MjEwNTM3OTgyMH0.RSt2lJxaPh_JwcpORuBozkUSIYaRrVt1_y9eEPj3YwM"
};

const ShaktixDB = {
  // Fetch live leads from Supabase
  async getLeads(limit = 50) {
    try {
      const response = await fetch(`${SUPABASE_CONFIG.url}/rest/v1/leads?select=*&limit=${limit}`, {
        headers: {
          'apikey': SUPABASE_CONFIG.anonKey,
          'Authorization': `Bearer ${SUPABASE_CONFIG.anonKey}`
        }
      });
      if (!response.ok) return [];
      return await response.json();
    } catch (e) {
      console.warn("Supabase fetch fallback to local:", e);
      return [];
    }
  },

  // Record an inbound demo / contact inquiry directly into leads table
  async submitInquiry(data) {
    try {
      const leadPayload = [{
        name: `${data.name} (${data.business_name || 'Business'})`,
        phone: data.phone,
        location: data.city || 'Patna',
        category: data.category || 'General Business',
        address: `Inbound Web Lead: ${data.business_name || ''}, ${data.city || ''}`,
        pitch_message: data.message || 'Requested Free Custom Demo & Sample Website',
        status: 'inbound_lead'
      }];

      const response = await fetch(`${SUPABASE_CONFIG.url}/rest/v1/leads`, {
        method: 'POST',
        headers: {
          'apikey': SUPABASE_CONFIG.anonKey,
          'Authorization': `Bearer ${SUPABASE_CONFIG.anonKey}`,
          'Content-Type': 'application/json',
          'Prefer': 'return=representation'
        },
        body: JSON.stringify(leadPayload)
      });
      return response.ok;
    } catch (e) {
      console.error("Error submitting inbound lead to Supabase:", e);
      return false;
    }
  }
};

if (typeof window !== 'undefined') {
  window.ShaktixDB = ShaktixDB;
}
if (typeof module !== 'undefined') {
  module.exports = { ShaktixDB, SUPABASE_CONFIG };
}
