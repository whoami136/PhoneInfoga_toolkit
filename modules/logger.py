import json, datetime

def execute(number):
    data = {"timestamp": str(datetime.datetime.now()), "target": number}
    with open("case_archive.json", "a") as f:
        f.write(json.dumps(data) + "\n")
    return "" # Return empty so main.py doesn't try to render a panel
