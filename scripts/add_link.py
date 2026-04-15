#!/usr/bin/env python3
"""
Quick script to add a link
Usage: python add_link.py "Name" "https://url.com" "Description" "Category"
"""

import json
import sys

LINKS_FILE = 'links.json'
JS_FILE = 'links.js'


def add_link(name, url, desc, category):
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        links = json.load(f)

    existing_urls = {link['url'] for link in links}

    if url in existing_urls:
        print(f"Already exists: {url}")
        return False

    new_link = {
        'name': name,
        'url': url,
        'desc': desc,
        'category': category
    }

    links.append(new_link)

    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=2)

    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write(f'const linksData = {json.dumps(links, ensure_ascii=False)};\n')

    print(f"Added: {name}")
    print(f"  Total links: {len(links)}")
    return True


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print(__doc__)
        print("\nExamples:")
        print('  python add_link.py "GitHub" "https://github.com" "Code hosting" "Tools"')
        print('  python add_link.py "Wikipedia" "https://wikipedia.org" "Free encyclopedia" "Knowledge"')
        sys.exit(1)

    name = sys.argv[1]
    url = sys.argv[2]
    desc = sys.argv[3]
    category = sys.argv[4]

    add_link(name, url, desc, category)
