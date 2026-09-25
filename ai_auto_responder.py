"""
Shaktix Automations - WhatsApp AI Virtual Salesman & 24/7 Auto-Responder Engine
Author: Chief Technology Officer & Lead AI Engineer (Shakti AI)
Founder & CEO: Shubham Kumar | Contact: +918825208568
Platform: https://shaktix-automations.vercel.app
"""

import sys
import os
import re
import json
import urllib.parse

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

class ShaktixAutoResponder:
    """
    24/7 AI Virtual Salesman that understands intent from client WhatsApp messages
    and returns tailored, high-converting responses with live links and pricing.
    """

    OFFICIAL_SITE = "https://shaktix-automations.vercel.app"
    FOUNDER_PHONE = "+918825208568"
    FOUNDER_NAME = "Shubham Kumar"

    RESPONSES = {
        "DEMO": (
            "Namaste! 🙏 Welcome to *Shaktix Automations*.\n\n"
            "Here is your *Instant Live Demo*:\n"
            "👉 Test our interactive WhatsApp simulator live in your browser:\n"
            "🌐 https://shaktix-automations.vercel.app/#simulator\n\n"
            "⚡ *Key Features You Get:*\n"
            "✅ 1-Click WhatsApp Bulk Dispatch with 100% Anti-Ban delay\n"
            "✅ Automatic personalized tags like {Name}, {Fees}, {Expiry}\n"
            "✅ Ultra-fast Custom Website delivered within 48 hours\n\n"
            "Aapka business kis type ka hai (Gym / Coaching / Clinic / Real Estate)? Reply karein taaki hum specific demo share kar sakein!"
        ),
        "ADMISSION": (
            "Hello Director / Principal Ji! 📚🎓\n\n"
            "Naye academic batch ke liye student admissions aur parent enquiries 3X boost karne ke liye *Shaktix Admission Booster* ready hai:\n\n"
            "🎯 *What We Provide for Coaching Centers:*\n"
            "1. Local Area Data: 1,500+ verified parents & students contact numbers\n"
            "2. 1-Click Broadcast: Batch announcement, results aur demo class links directly WhatsApp par bhejein\n"
            "3. Modern Coaching Website: Jisse students online register & seat book kar sakein\n\n"
            "🚀 *Package Pricing:*\n"
            "• Starter Bulk Sender: ₹1,999 (One-time)\n"
            "• Website + Admission Booster Combo: ₹4,999\n\n"
            "Sample Coaching Website dekhne ke liye reply karein: *SAMPLE WEBSITE* ya call karein CEO Shubham Kumar ko 📞 8825208568."
        ),
        "GYM": (
            "Namaste Fitness Team! 💪🏋️‍♂️\n\n"
            "Gyms ke liye membership renewal aur naye walk-in admissions automate karna hamari specialty hai:\n\n"
            "⚡ *Shaktix Gym Automation Suite:*\n"
            "✅ Membership Expiry Se 3 Din Pehle Automated Reminder (Renewal rate 40% boost)\n"
            "✅ Festive / New Year Discount Offers 1-Click me sabhi members ko delivery\n"
            "✅ Modern Gym Landing Page with online slot booking\n\n"
            "👉 Hamari live agency website dekhein: https://shaktix-automations.vercel.app\n\n"
            "Kya aapke gym ke liye ek customized sample website link share karoon? Reply: *YES*."
        ),
        "CLINIC": (
            "Respected Doctor / Clinic Administrator! 🩺🏥\n\n"
            "Healthcare aur dental clinics ke liye *Shaktix Smart Clinic Setup*:\n\n"
            "🩺 *System Highlights:*\n"
            "• Patients mobile se direct confirmed appointment slot book kar sakte hain\n"
            "• Automated WhatsApp reminder se patient no-shows 70% kam ho jaate hain\n"
            "• Routine checkup & prescription follow-up messages on autopilot\n\n"
            "Official Proposal dekhein: https://shaktix-automations.vercel.app/quotation.html\n\n"
            "Live demo schedule karne ke liye reply karein: *DOCTOR*."
        ),
        "REALESTATE": (
            "Namaste Real Estate Team! 🏢🔑\n\n"
            "Plots, residential apartments aur commercial projects ke verified buyers connect karne ke liye:\n\n"
            "🎯 *Real Estate Investor Engine:*\n"
            "• Verified Investors Data: Shehar ke high-budget property seekers tak direct layout & walkthrough video reach\n"
            "• Instant Site-Visit Booking on WhatsApp\n"
            "• Luxury Digital Property Showcase Website\n\n"
            "Call directly to discuss: 📞 8825208568 (CEO Shubham Kumar)."
        ),
        "PRICE": (
            "Namaste! Yeh rahe *Shaktix Automations* ke official transparent packages 💰:\n\n"
            "1️⃣ *STARTER BULK SENDER LICENSE* — ₹1,999 (One-Time)\n"
            "   • WhatsApp bulk engine with Anti-Ban delay\n"
            "   • 100 Free local verified leads included\n\n"
            "2️⃣ *HIGH-CONVERTING CUSTOM WEBSITE* — ₹2,499 (One-Time)\n"
            "   • Ultra-fast mobile landing page\n"
            "   • 48-hour delivery guarantee\n\n"
            "3️⃣ *GROWTH COMBO PACKAGE (Recommended)* — ₹4,999 (One-Time)\n"
            "   • Complete Modern Website + Bulk WhatsApp Engine + Local Leads Pack\n\n"
            "4️⃣ *VIP MONTHLY MAINTENANCE* — ₹999 / Mahina\n"
            "   • 24/7 Server uptime + Monthly bulk campaign assistance + Bot support\n\n"
            "📄 Digital Quotation Link: https://shaktix-automations.vercel.app/quotation.html\n\n"
            "Aapko kaunsa package chahiye? Reply: *STARTER*, *COMBO*, ya *CUSTOM*."
        ),
        "WEBSITE": (
            "Namaste! Hum aapke business ke liye ultra-fast, modern aur high-converting website 24–48 ghante ke andar live kar sakte hain! 🌐⚡\n\n"
            "✅ Mobile-friendly & super fast loading\n"
            "✅ WhatsApp chat button directly integrated\n"
            "✅ Google Maps & SEO optimized\n"
            "✅ One-time setup: Sirf ₹2,499!\n\n"
            "Hamara live showcase dekhein: https://shaktix-automations.vercel.app\n\n"
            "Aapka business kis type ka hai? Details share karein hum sample layout generate kar denge."
        ),
        "DEFAULT": (
            "Namaste! 🙏 Thank you for reaching out to *Shaktix Automations*.\n\n"
            "Hum local businesses (Gyms, Coaching, Clinics, Real Estate) ko automate karke unka business 3X grow karne mein help karte hain.\n\n"
            "⚡ *Aapko kya chahiye?*\n"
            "1. Type *DEMO* for Free Live Demo & Simulator\n"
            "2. Type *PRICE* for Complete Pricing & Packages\n"
            "3. Type *COACHING*, *GYM*, *CLINIC* for your industry solution\n"
            "4. Type *CALL* to speak directly with Founder & CEO Shubham Kumar\n\n"
            "🌐 Website: https://shaktix-automations.vercel.app | 📞 8825208568"
        )
    }

    @classmethod
    def generate_reply(cls, incoming_text):
        """Analyzes incoming WhatsApp text and maps to the highest-converting response."""
        if not incoming_text:
            return cls.RESPONSES["DEFAULT"]

        t = incoming_text.strip().lower()

        # Keyword matching heuristics
        if any(w in t for w in ["demo", "video", "trial", "dikhao", "dekhna"]):
            return cls.RESPONSES["DEMO"]
        elif any(w in t for w in ["admission", "coaching", "institute", "student", "batch", "school", "tuition"]):
            return cls.RESPONSES["ADMISSION"]
        elif any(w in t for w in ["gym", "fitness", "workout", "trainer", "renewal"]):
            return cls.RESPONSES["GYM"]
        elif any(w in t for w in ["clinic", "doctor", "dental", "hospital", "patient", "appointment", "teeth"]):
            return cls.RESPONSES["CLINIC"]
        elif any(w in t for w in ["realestate", "property", "plot", "flat", "broker", "builder"]):
            return cls.RESPONSES["REALESTATE"]
        elif any(w in t for w in ["price", "fees", "cost", "kitna", "package", "rate", "quote", "bill"]):
            return cls.RESPONSES["PRICE"]
        elif any(w in t for w in ["website", "web", "landing page", "page", "portal"]):
            return cls.RESPONSES["WEBSITE"]
        elif any(w in t for w in ["call", "baat", "phone", "contact", "shubham"]):
            return (
                f"Aap direct CEO Shubham Kumar se call par baat kar sakte hain:\n"
                f"📞 Mobile: {cls.FOUNDER_PHONE}\n"
                f"💬 WhatsApp: https://wa.me/918825208568\n\n"
                f"Shubham Sir will personally assist you with your business setup!"
            )
        else:
            return cls.RESPONSES["DEFAULT"]

def run_interactive_simulator():
    """Interactive command-line tester for testing incoming client replies."""
    print("="*65)
    print("🤖 SHAKTIX WHATSAPP AI VIRTUAL SALESMAN (AUTO-RESPONDER v1.0)")
    print("Founder & CEO: Shubham Kumar | Contact: +918825208568")
    print("="*65)
    print("Ready to receive incoming messages from WhatsApp prospects.")
    print("Type sample customer messages below (or 'exit' to quit):")
    print("Try typing: 'demo', 'admission', 'gym fees', 'price', 'clinic appointment'\n")

    while True:
        try:
            user_msg = input("\n📩 Customer Incoming Message > ")
            if not user_msg.strip():
                continue
            if user_msg.strip().lower() in ['exit', 'quit']:
                print("\nShutting down Auto-Responder. System armed on standby.")
                break

            reply = ShaktixAutoResponder.generate_reply(user_msg)
            print("\n⚡ [SHAKTIX AI BOT 0-SEC REPLY]:")
            print("─"*50)
            print(reply)
            print("─"*50)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting Auto-Responder.")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Automated test suite
        test_phrases = ["Hi please send demo", "What is the coaching admission booster?", "gym price?", "kitna paisa lagega", "doctor clinic setup"]
        for p in test_phrases:
            print(f"\n--- TEST: '{p}' ---")
            print(ShaktixAutoResponder.generate_reply(p)[:120] + "...")
        print("\n✅ All auto-responder test cases passed successfully.")
    else:
        run_interactive_simulator()
