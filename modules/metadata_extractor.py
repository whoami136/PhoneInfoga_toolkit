def execute(target):
    clean_num = "".join(filter(str.isdigit, target))
    # Generates targeted search strings for public leak or code repositories
    links = [
        f"GitHub: https://github.com/search?q={clean_num}",
        f"Pastebin: https://www.google.com/search?q=site:pastebin.com+{clean_num}"
    ]
    return "\n".join(links)
