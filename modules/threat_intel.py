def execute(number):
    if number.startswith("+1800") or number.startswith("+1855"):
        return "[red]WARNING: Potential Toll-Free Scam Pattern.[/red]"
    else:
        return "[green]No specific threat patterns found.[/green]"
