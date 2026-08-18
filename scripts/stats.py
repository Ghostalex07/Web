#!/usr/bin/env python3
"""Show statistics about the Aion link collection."""

import json
import os
from collections import Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)


def main():
    with open(os.path.join(ROOT_DIR, 'links.json'), 'r') as f:
        links = json.load(f)

    print(f"\n{'='*50}")
    print(f"  AION LINK DATABASE STATS")
    print(f"{'='*50}\n")
    print(f"  Total links:     {len(links)}")

    cats = Counter(l['category'] for l in links)
    subs = Counter(f"{l['category']}/{l.get('subcategory', '?')}" for l in links)
    print(f"  Main categories: {len(cats)}")
    print(f"  Subcategories:   {len(subs)}")
    print()

    print("  Top 15 categories:")
    for cat, count in cats.most_common(15):
        bar = '#' * (count // 20)
        print(f"    {cat:25s} {count:4d}  {bar}")

    print(f"\n  Smallest categories (<=5 links):")
    for cat, count in sorted(cats.items(), key=lambda x: x[1]):
        if count <= 5:
            print(f"    {cat}: {count}")

    empty_desc = sum(1 for l in links if not l.get('desc'))
    print(f"\n  Links with empty description: {empty_desc}")

    no_sub = sum(1 for l in links if not l.get('subcategory'))
    print(f"  Links without subcategory: {no_sub}")

    print(f"\n{'='*50}\n")


if __name__ == '__main__':
    main()
