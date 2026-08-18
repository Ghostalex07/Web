#!/usr/bin/env python3
"""
Aion Links Manager
Manage links in the hub: add, remove, search, validate, export.
"""

import json
import sys
import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
LINKS_FILE = os.path.join(ROOT_DIR, 'links.json')
JS_FILE = os.path.join(ROOT_DIR, 'links.js')


def load_links():
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_links(links):
    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=2)
    generate_js()
    print(f"Saved: {len(links)} links")


def generate_js():
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        links = json.load(f)
    js = f'const linksData = {json.dumps(links, ensure_ascii=False)};\n'
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"Generated: links.js ({len(links)} links)")


def add_links(new_links):
    links = load_links()
    existing = {l['url'] for l in links}
    added = 0
    for link in new_links:
        if link['url'] not in existing:
            link.setdefault('subcategory', link.get('subcategory', 'General'))
            links.append(link)
            existing.add(link['url'])
            added += 1
    save_links(links)
    print(f"Added: {added} new links")
    return added


def remove_duplicates():
    links = load_links()
    seen = set()
    unique = []
    for l in links:
        if l['url'] not in seen:
            unique.append(l)
            seen.add(l['url'])
    removed = len(links) - len(unique)
    save_links(unique)
    print(f"Removed: {removed} duplicates, {len(unique)} remaining")


def list_categories():
    links = load_links()
    tree = {}
    for l in links:
        cat = l.get('category', 'Uncategorized')
        sub = l.get('subcategory', 'General')
        if cat not in tree:
            tree[cat] = {}
        tree[cat][sub] = tree[cat].get(sub, 0) + 1

    print(f"\n=== Categories ({len(tree)} main) ===\n")
    for cat in sorted(tree.keys()):
        total = sum(tree[cat].values())
        print(f"  {cat} ({total})")
        for sub, count in sorted(tree[cat].items()):
            print(f"    {sub}: {count}")
        print()


def search_links(query):
    links = load_links()
    q = query.lower()
    results = [l for l in links if q in (l['name'] + l['desc'] + l['url'] + l.get('category', '') + l.get('subcategory', '')).lower()]
    print(f"\n=== Results for '{query}' ({len(results)}) ===\n")
    for l in results[:20]:
        print(f"  [{l.get('category', '?')}/{l.get('subcategory', '?')}] {l['name']}")
        print(f"    {l['url']}")
    if len(results) > 20:
        print(f"  ... and {len(results) - 20} more")
    return results


def validate_links():
    links = load_links()
    errors = []
    for i, l in enumerate(links):
        for field in ['name', 'url', 'desc', 'category']:
            if field not in l:
                errors.append(f"Missing '{field}' in link {i}: {l.get('name', '?')}")
        if 'url' in l and not l['url'].startswith(('http://', 'https://', 'gopher://')):
            errors.append(f"Invalid URL: {l['url']}")
        if not l.get('subcategory'):
            errors.append(f"Missing subcategory: {l.get('name', '?')}")

    if errors:
        print(f"\n=== {len(errors)} errors found ===")
        for e in errors[:20]:
            print(f"  {e}")
    else:
        print("All links valid")
    return len(errors) == 0


def export_to_markdown():
    links = load_links()
    tree = {}
    for l in links:
        cat = l.get('category', 'Uncategorized')
        sub = l.get('subcategory', 'General')
        if cat not in tree:
            tree[cat] = {}
        if sub not in tree[cat]:
            tree[cat][sub] = []
        tree[cat][sub].append(l)

    md = "# Aion Links\n\n"
    md += f"> {len(links)} links across {len(tree)} categories\n\n"
    for cat in sorted(tree.keys()):
        md += f"## {cat}\n\n"
        for sub in sorted(tree[cat].keys()):
            md += f"### {sub}\n\n"
            for l in sorted(tree[cat][sub], key=lambda x: x['name']):
                md += f"- [{l['name']}]({l['url']}) — {l['desc']}\n"
            md += "\n"

    out = os.path.join(ROOT_DIR, 'links.md')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"Exported to links.md ({len(links)} links)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nCommands:")
        print("  add <name> <url> <desc> <category> [subcategory]")
        print("  duplicates")
        print("  categories")
        print("  search <query>")
        print("  validate")
        print("  export")
        print("  generate")
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == 'add' and len(sys.argv) >= 6:
        link = {
            'name': sys.argv[2],
            'url': sys.argv[3],
            'desc': sys.argv[4],
            'category': sys.argv[5],
            'subcategory': sys.argv[6] if len(sys.argv) > 6 else 'General',
        }
        add_links([link])
    elif cmd == 'duplicates':
        remove_duplicates()
    elif cmd == 'categories':
        list_categories()
    elif cmd == 'search' and len(sys.argv) >= 3:
        search_links(sys.argv[2])
    elif cmd == 'validate':
        validate_links()
    elif cmd == 'export':
        export_to_markdown()
    elif cmd == 'generate':
        generate_js()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == '__main__':
    main()
