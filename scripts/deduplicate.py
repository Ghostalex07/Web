#!/usr/bin/env python3
"""
Script para eliminar duplicados
Uso: python deduplicate.py
"""

import json

LINKS_FILE = 'links.json'
JS_FILE = 'links.js'


def deduplicate():
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        links = json.load(f)
    
    original = len(links)
    
    seen = set()
    unique = []
    for link in links:
        if link['url'] not in seen:
            unique.append(link)
            seen.add(link['url'])
    
    duplicates = original - len(unique)
    
    if duplicates == 0:
        print("✓ No hay duplicados")
        print(f"  Total: {len(unique)} links")
        return
    
    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(unique, f, ensure_ascii=False, indent=2)
    
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write(f'const linksData = {json.dumps(unique, ensure_ascii=False)};\n')
    
    print(f"✓ Eliminados {duplicates} duplicados")
    print(f"  Original: {original}")
    print(f"  Final: {len(unique)}")


if __name__ == '__main__':
    deduplicate()
