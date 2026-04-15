#!/usr/bin/env python3
"""
Aion Links Manager
Script para gestionar los links del hub
"""

import json
import sys
import os

LINKS_FILE = 'links.json'
JS_FILE = 'links.js'


def load_links():
    """Cargar links desde JSON"""
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_links(links):
    """Guardar links en JSON y regenerar JS"""
    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, ensure_ascii=False, indent=2)
    generate_js()
    print(f"Guardado: {len(links)} links")


def generate_js():
    """Generar links.js desde links.json"""
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        links = json.load(f)
    
    js_content = f'const linksData = {json.dumps(links, ensure_ascii=False)};\n'
    
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"Generado: {JS_FILE} ({len(links)} links)")


def add_links(new_links):
    """Agregar nuevos links"""
    links = load_links()
    existing_urls = {link['url'] for link in links}
    
    added = 0
    for link in new_links:
        if link['url'] not in existing_urls:
            links.append(link)
            existing_urls.add(link['url'])
            added += 1
    
    save_links(links)
    print(f"Agregados: {added} links")
    return added


def remove_duplicates():
    """Eliminar links duplicados por URL"""
    links = load_links()
    original_count = len(links)
    
    seen = set()
    unique_links = []
    for link in links:
        if link['url'] not in seen:
            unique_links.append(link)
            seen.add(link['url'])
    
    removed = original_count - len(unique_links)
    save_links(unique_links)
    print(f"Duplicados eliminados: {removed}")
    print(f"Total final: {len(unique_links)} links")
    return removed


def list_categories():
    """Listar todas las categorías"""
    links = load_links()
    categories = {}
    for link in links:
        cat = link.get('category', 'Uncategorized')
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n=== Categorías ===")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
    print(f"\nTotal: {len(categories)} categorías, {len(links)} links")


def search_links(query):
    """Buscar links por nombre, descripción o URL"""
    links = load_links()
    query_lower = query.lower()
    
    results = []
    for link in links:
        if (query_lower in link['name'].lower() or
            query_lower in link['desc'].lower() or
            query_lower in link['url'].lower()):
            results.append(link)
    
    print(f"\n=== Resultados para '{query}' ({len(results)}) ===")
    for link in results[:20]:
        print(f"  [{link['category']}] {link['name']}")
        print(f"    {link['url']}")
    
    if len(results) > 20:
        print(f"  ... y {len(results) - 20} más")
    
    return results


def validate_links():
    """Validar formato de links"""
    links = load_links()
    errors = []
    
    for i, link in enumerate(links):
        required = ['name', 'url', 'desc', 'category']
        for field in required:
            if field not in link:
                errors.append(f"Falta '{field}' en link {i}: {link.get('name', 'Unknown')}")
        
        if 'url' in link and not link['url'].startswith(('http://', 'https://')):
            errors.append(f"URL inválida: {link['url']}")
    
    if errors:
        print("\n=== Errores encontrados ===")
        for err in errors[:20]:
            print(f"  {err}")
        if len(errors) > 20:
            print(f"  ... y {len(errors) - 20} más")
    else:
        print("✓ Todos los links son válidos")
    
    return len(errors) == 0


def export_to_markdown():
    """Exportar links a formato Markdown"""
    links = load_links()
    
    categories = {}
    for link in links:
        cat = link.get('category', 'Uncategorized')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(link)
    
    md = "# Aion Links\n\n"
    md += f"> Total: {len(links)} links en {len(categories)} categorías\n\n"
    
    for cat in sorted(categories.keys()):
        md += f"## {cat}\n\n"
        for link in sorted(categories[cat], key=lambda x: x['name']):
            md += f"- [{link['name']}]({link['url']}) - {link['desc']}\n"
        md += "\n"
    
    with open('links.md', 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"Exportado a links.md ({len(links)} links)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nUso:")
        print("  python manager.py add <name> <url> <desc> <category>")
        print("  python manager.py duplicates")
        print("  python manager.py categories")
        print("  python manager.py search <query>")
        print("  python manager.py validate")
        print("  python manager.py export")
        print("  python manager.py generate")
        sys.exit(1)
    
    cmd = sys.argv[1].lower()
    
    if cmd == 'add' and len(sys.argv) >= 6:
        link = {
            'name': sys.argv[2],
            'url': sys.argv[3],
            'desc': sys.argv[4],
            'category': sys.argv[5]
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
        print(f"Comando desconocido: {cmd}")
        sys.exit(1)


if __name__ == '__main__':
    main()
