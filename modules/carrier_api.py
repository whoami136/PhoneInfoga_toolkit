import os
import requests
from dotenv import load_dotenv

# Force load .env from the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(project_root, '.env'))

API_KEY = os.getenv("NUMVERIFY_API_KEY")

def execute(number):
    if not API_KEY:
        return "Error: API_KEY missing in .env"
    
    url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if "error" in data:
            return f"API Error: {data['error'].get('info', 'Unknown')}"
        
        return f"Carrier: {data.get('carrier')}\nStatus: {'Valid' if data.get('valid') else 'Invalid'}\nLocation: {data.get('location')}"
    except Exception as e:
        return f"Connection Failed: {e}"
