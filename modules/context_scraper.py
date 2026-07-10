import requests
from bs4 import BeautifulSoup

def execute(number):
    search_url = f"https://www.google.com/search?q={number}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        snippets = [s.get_text() for s in soup.select('div.VwiC3b')[:2]]
        return "\n\n".join([f"- {s[:120]}..." for s in snippets]) if snippets else "No results."
    except Exception as e:
        return f"Scraper failed: {e}"
