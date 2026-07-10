# modules/real_analysis.py
def calculate_real_score(results):
    # results is a dictionary of found services
    score = 0
    # +25 for each verified presence
    if results.get('whatsapp'): score += 25
    if results.get('telegram'): score += 25
    if results.get('signal'): score += 25
    
    classification = "Low-Visibility"
    if score > 50: classification = "High-Visibility/Personal"
    
    return f"{score}/75 ({classification})"
