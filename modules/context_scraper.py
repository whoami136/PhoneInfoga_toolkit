import requests
from bs4 import BeautifulSoup

def execute(target):
    # Enclose target in quotes to force exact matches on public web pages
    search_url = f"https://html.duckduckgo.com/html/?q=%22{target}%22"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.select('a.result__snippet')
        
        snippets = []
        clean_target = "".join(filter(str.isdigit, target))
        
        for r in results:
            text = r.get_text().strip()
            # Only accept the snippet if the target number digits actually appear inside the text
            if clean_target in text or target in text:
                if len(text) > 15:
                    snippets.append(f"• {text}")
            
            if len(snippets) >= 2:
                break

        # If no page actually references this exact number, return None 
        # (Thanks to your main.py, this will completely hide the useless panel)
        if not snippets:
            return None
            
        return "\n\n".join(snippets)
        
    except Exception:
        return None
