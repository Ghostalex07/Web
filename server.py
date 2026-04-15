#!/usr/bin/env python3
"""
Aion Links Manager - Flask Server
Simple web interface to add and manage links
"""

import json
import os
from flask import Flask, request, jsonify, send_file, send_from_directory

app = Flask(__name__)

LINKS_FILE = 'links.json'
JS_FILE = 'links.js'

def load_links():
    """Load links from JSON file"""
    if not os.path.exists(LINKS_FILE):
        return []
    with open(LINKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_links(links):
    """Save links to JSON file and regenerate JS"""
    with open(LINKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(links, f, indent=2, ensure_ascii=False)
    
    regenerate_js(links)

def regenerate_js(links):
    """Regenerate links.js from links data"""
    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write('const linksData = ')
        json.dump(links, f, indent=2, ensure_ascii=False)
        f.write(';')

@app.route('/')
def index():
    """Serve main page"""
    return send_file('index.html')

@app.route('/links')
def links_page():
    """Serve links page (same as index)"""
    return send_file('index.html')

@app.route('/admin')
def admin():
    """Serve admin page"""
    return send_file('admin.html')

@app.route('/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('.', filename)

@app.route('/api/links', methods=['GET', 'POST'])
def api_links():
    """API endpoint for links"""
    links = load_links()
    
    if request.method == 'GET':
        # Get query parameters
        limit = request.args.get('limit', type=int)
        sort = request.args.get('sort', 'name')  # name, newest, category
        search = request.args.get('search', '').lower()
        category = request.args.get('category', '')
        
        # Filter links
        filtered = links
        if search:
            filtered = [l for l in filtered if 
                search in l.get('name', '').lower() or 
                search in l.get('desc', '').lower()]
        if category:
            filtered = [l for l in filtered if l.get('category') == category]
        
        # Sort links
        if sort == 'name':
            filtered.sort(key=lambda x: x.get('name', '').lower())
        elif sort == 'newest':
            filtered = list(reversed(filtered))
        elif sort == 'category':
            filtered.sort(key=lambda x: (x.get('category', '').lower(), x.get('name', '').lower()))
        
        # Limit results
        if limit:
            filtered = filtered[:limit]
        
        return jsonify(filtered)
    
    elif request.method == 'POST':
        # Add new link
        data = request.get_json()
        
        # Validate required fields
        if not data.get('name') or not data.get('url'):
            return jsonify({'error': 'Name and URL are required'}), 400
        
        name = data['name'].strip()
        url = data['url'].strip()
        desc = data.get('desc', '').strip()
        category = data.get('category', '').strip() or 'Miscellaneous'
        
        # Normalize URL
        if not url.startswith(('http://', 'https://', 'gemini://', 'gopher://')):
            url = 'https://' + url
        
        # Check for duplicates
        for link in links:
            if link['url'].lower() == url.lower():
                return jsonify({'error': 'Link already exists', 'existing': link}), 409
        
        # Add new link
        new_link = {
            'name': name,
            'url': url,
            'desc': desc,
            'category': category
        }
        links.append(new_link)
        
        # Sort alphabetically by category then name
        links.sort(key=lambda x: (x.get('category', '').lower(), x.get('name', '').lower()))
        
        save_links(links)
        
        return jsonify({'success': True, 'link': new_link, 'total': len(links)})

@app.route('/api/links/<int:index>', methods=['DELETE'])
def delete_link(index):
    """Delete a link by index"""
    links = load_links()
    if index < 0 or index >= len(links):
        return jsonify({'error': 'Index out of range'}), 400
    
    deleted = links.pop(index)
    save_links(links)
    
    return jsonify({'success': True, 'deleted': deleted, 'total': len(links)})

@app.route('/api/stats')
def api_stats():
    """Get statistics"""
    links = load_links()
    categories = set(l.get('category', 'Miscellaneous') for l in links)
    
    return jsonify({
        'total': len(links),
        'categories': len(categories),
        'category_list': sorted(categories)
    })

@app.route('/api/deduplicate', methods=['POST'])
def deduplicate():
    """Remove duplicate links"""
    links = load_links()
    seen_urls = set()
    seen_names = set()
    original_count = len(links)
    unique_links = []
    
    for link in links:
        url = link.get('url', '').lower()
        name = link.get('name', '').lower()
        
        if url not in seen_urls and name not in seen_names:
            seen_urls.add(url)
            seen_names.add(name)
            unique_links.append(link)
    
    save_links(unique_links)
    
    return jsonify({
        'removed': original_count - len(unique_links),
        'remaining': len(unique_links)
    })

if __name__ == '__main__':
    # Initialize JS file if it doesn't exist
    if os.path.exists(LINKS_FILE) and not os.path.exists(JS_FILE):
        links = load_links()
        regenerate_js(links)
        print(f"Generated {JS_FILE} with {len(links)} links")
    
    print("""
╔═══════════════════════════════════════════════════╗
║  Aion Links Manager                              ║
║                                                  ║
║  Local:   http://127.0.0.1:5000                 ║
║  Admin:   http://127.0.0.1:5000/admin            ║
║                                                  ║
║  API Endpoints:                                  ║
║  GET  /api/links     - List all links            ║
║  POST /api/links     - Add new link              ║
║  GET  /api/stats     - Get statistics            ║
║  POST /api/deduplicate - Remove duplicates        ║
╚═══════════════════════════════════════════════════╝
    """)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
