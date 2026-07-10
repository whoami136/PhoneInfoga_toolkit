import os
import requests
from dotenv import load_dotenv

# Path to .env in the root project directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base_dir, '.env'))

def execute(number):
    """
    Validates phone number via Numverify API.
    Returns formatted string or error message.
    """
    api_key = os.getenv("NUMVERIFY_API_KEY")
    
    if not api_key:
        return "Error: API Key missing in .env"
        
    url = "http://apilayer.net/api/validate"
    params = {
        'access_key': api_key, 
        'number': number.replace("+", ""), 
        'format': 1
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        # Handle API-specific error responses
        if data.get("success") is False:
            error_info = data.get("error", {}).get("info", "Unknown API error")
            return f"API Error: {error_info}"
            
        # Extract data with fallbacks
        line_type = data.get("line_type") or "N/A"
        carrier = data.get("carrier") or "N/A"
        
        # Location fallback logic:
        # Use location if available, otherwise use country_name
        location = data.get("location")
        if not location or location.strip() == "":
            location = data.get("country_name") or "Unknown Region"
            
        return (f"Line Type : {line_type}\n"
                f"Carrier   : {carrier}\n"
                f"Location  : {location}")
                
    except Exception as e:
        return f"Connection Failed: {e}"
