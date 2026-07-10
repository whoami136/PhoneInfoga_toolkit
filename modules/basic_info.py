# modules/real_basic_info.py
import phonenumbers
from phonenumbers import carrier, geocoder

def get_real_data(number_str):
    try:
        # Convert to international format if not already
        if not number_str.startswith('+'):
            number_str = '+' + number_str
            
        parsed = phonenumbers.parse(number_str)
        
        if not phonenumbers.is_valid_number(parsed):
            return {"valid": False, "carrier": "N/A", "location": "N/A"}

        return {
            "valid": True,
            "carrier": carrier.name_for_number(parsed, "en"),
            "location": geocoder.description_for_number(parsed, "en")
        }
    except:
        return {"valid": False, "carrier": "Unknown", "location": "Unknown"}
