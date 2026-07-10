import requests

def execute(number):
    platforms = {
        "Telegram": f"https://t.me/{number}",
        "Signal": f"https://signal.me/#p/{number}"
    }
    status = ""
    for name, url in platforms.items():
        try:
            response = requests.head(url, timeout=3)
            status += f"{name}: {'[bold green]Active[/bold green]' if response.status_code == 200 else '[bold red]Not Found[/bold red]'}\n"
        except:
            status += f"{name}: [bold yellow]Unknown[/bold yellow]\n"
    return status.strip()
