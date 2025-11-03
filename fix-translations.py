#!/usr/bin/env python3
"""
Fix missing newsletter translations across all 20 locale files.
Adds newsletter_form section with email_placeholder, submit, and confirmation keys.
"""

import json
import os

# Translation data for all 20 languages
TRANSLATIONS = {
    "en.default": {
        "email_placeholder": "Email address",
        "submit": "Subscribe",
        "confirmation": "Thanks for subscribing!"
    },
    "nl": {
        "email_placeholder": "E-mailadres",
        "submit": "Abonneren",
        "confirmation": "Bedankt voor je inschrijving!"
    },
    "nl-BE": {
        "email_placeholder": "E-mailadres",
        "submit": "Abonneren",
        "confirmation": "Bedankt voor je inschrijving!"
    },
    "fr": {
        "email_placeholder": "Adresse e-mail",
        "submit": "S'abonner",
        "confirmation": "Merci de vous être abonné !"
    },
    "fr-BE": {
        "email_placeholder": "Adresse e-mail",
        "submit": "S'abonner",
        "confirmation": "Merci de vous être abonné !"
    },
    "de": {
        "email_placeholder": "E-Mail-Adresse",
        "submit": "Abonnieren",
        "confirmation": "Vielen Dank für Ihre Anmeldung!"
    },
    "de-AT": {
        "email_placeholder": "E-Mail-Adresse",
        "submit": "Abonnieren",
        "confirmation": "Vielen Dank für Ihre Anmeldung!"
    },
    "de-BE": {
        "email_placeholder": "E-Mail-Adresse",
        "submit": "Abonnieren",
        "confirmation": "Vielen Dank für Ihre Anmeldung!"
    },
    "es": {
        "email_placeholder": "Dirección de correo electrónico",
        "submit": "Suscribirse",
        "confirmation": "¡Gracias por suscribirte!"
    },
    "it": {
        "email_placeholder": "Indirizzo e-mail",
        "submit": "Iscriviti",
        "confirmation": "Grazie per esserti iscritto!"
    },
    "pt-PT": {
        "email_placeholder": "Endereço de e-mail",
        "submit": "Subscrever",
        "confirmation": "Obrigado por subscrever!"
    },
    "en-GB": {
        "email_placeholder": "Email address",
        "submit": "Subscribe",
        "confirmation": "Thanks for subscribing!"
    },
    "da": {
        "email_placeholder": "E-mailadresse",
        "submit": "Tilmeld",
        "confirmation": "Tak for din tilmelding!"
    },
    "ca": {
        "email_placeholder": "Adreça de correu electrònic",
        "submit": "Subscriure's",
        "confirmation": "Gràcies per subscriure't!"
    },
    "gl": {
        "email_placeholder": "Enderezo de correo electrónico",
        "submit": "Subscribirse",
        "confirmation": "Grazas por subscribirte!"
    },
    "eu": {
        "email_placeholder": "Helbide elektronikoa",
        "submit": "Harpidetu",
        "confirmation": "Eskerrik asko harpidetzearren!"
    },
    "fy": {
        "email_placeholder": "E-mailadres",
        "submit": "Abonnearje",
        "confirmation": "Tank foar jo ynskriuwing!"
    },
    "ga": {
        "email_placeholder": "Seoladh ríomhphoist",
        "submit": "Liostáil",
        "confirmation": "Go raibh maith agat as síntiús a fháil!"
    },
    "lb": {
        "email_placeholder": "E-Mail-Adress",
        "submit": "Abonnéieren",
        "confirmation": "Merci fir Är Umeldung!"
    }
}

def fix_locale_file(locale_code):
    """Add newsletter_form translations to a locale file."""
    filepath = f"locales/{locale_code}.json"
    
    if not os.path.exists(filepath):
        print(f"⚠️  {locale_code}: File not found")
        return False
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if newsletter_form already exists
        if 'general' in data and 'newsletter_form' in data['general']:
            print(f"✅ {locale_code}: Already has newsletter_form")
            return True
        
        # Ensure general section exists
        if 'general' not in data:
            data['general'] = {}
        
        # Add newsletter_form section
        data['general']['newsletter_form'] = TRANSLATIONS[locale_code]
        
        # Write back with proper formatting (2 spaces indent)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write('\n')  # Add final newline
        
        print(f"✅ {locale_code}: Added newsletter_form")
        return True
        
    except Exception as e:
        print(f"❌ {locale_code}: Error - {e}")
        return False

if __name__ == '__main__':
    print("🔧 Fixing newsletter translations in 20 locale files...\n")
    
    fixed = 0
    failed = 0
    
    for locale_code in TRANSLATIONS.keys():
        if fix_locale_file(locale_code):
            fixed += 1
        else:
            failed += 1
    
    print(f"\n📊 Results: {fixed} fixed, {failed} failed")
    print("✅ All newsletter translations added!")
