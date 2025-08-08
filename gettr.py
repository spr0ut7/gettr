from newspaper import Article
from urllib.parse import urlparse
import os
import sys
import re

def get_domain_folder(url):
    parsed = urlparse(url)
    hostname = parsed.hostname or 'unknown'
    base = hostname.replace('www.', '').split('.')[0]
    return base.lower()

def clean_text(raw_text):
    lines = raw_text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        # Remove lines that are only "Advertisement"
        if re.fullmatch(r'advertisement', line, re.IGNORECASE):
            continue
        # Remove excessive empty lines
        if line == '' and (not cleaned_lines or cleaned_lines[-1] == ''):
            continue
        cleaned_lines.append(line)

    return '\n'.join(cleaned_lines).strip()

def save_article(url, base_dir='articles'):
    article = Article(url)
    article.download()
    article.parse()

    domain_folder = get_domain_folder(url)
    target_dir = os.path.join(base_dir, domain_folder)
    os.makedirs(target_dir, exist_ok=True)

    title = article.title.strip().replace(' ', '_').replace('/', '_')
    filename = f"{title}.txt"
    filepath = os.path.join(target_dir, filename)

    cleaned_text = clean_text(article.text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {article.title}\n\n")
        f.write(cleaned_text)
        f.write(f"\n\n---\nSource: {url}\n")

    print(f"✅ Saved: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gettr.py <URL>")
    else:
        save_article(sys.argv[1])
