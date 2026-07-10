import requests

def get_live_carrier_data(number):
    # This is a real API that checks the live MNP registry
    api_key = "YOUR_ABSTRACT_API_KEY" # Get this from their site
    url = f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={number}"
    
    response = requests.get(url)
    data = response.json()
    
    # This returns the REAL carrier, even if they switched via MNP
    return data.get("carrier", "Unknown")
