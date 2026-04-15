# Aion - Links Hub

> A minimalist links hub. A collection of interesting websites organized by category.

## Project Structure

```
Web/
├── index.html           # Main page
├── admin.html           # Admin page (add links via web)
├── server.py            # Flask server (optional, for web interface)
├── scripts/
│   ├── manager.py       # Full links manager
│   ├── add_link.py      # Quick script to add a link
│   └── deduplicate.py   # Remove duplicates
├── links.json           # Links data (source of truth)
├── links.js             # JS with links (auto-generated from JSON)
└── README.md           # Documentation
```

## How it works

1. **`links.json`** - Contains all links in JSON format (source of truth)
2. **`links.js`** - JS file that loads the links (auto-generated from JSON)
3. **`index.html`** - Main page that displays links
4. **`admin.html`** - Web interface to add links (requires server.py)
5. **`server.py`** - Flask server with REST API for adding links

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Ghostalex07/Web.git
cd Web
```

### 2. Open in browser (static)
```bash
# With Python
python -m http.server 8000

# With PHP
php -S localhost:8000

# With Node.js
npx serve
```

Then open: `http://localhost:8000`

### 3. Web Server (optional - for adding links via web)

Requires Flask:
```bash
pip install flask
python server.py
```

Then open:
- Main page: `http://localhost:5000`
- Admin page: `http://localhost:5000/admin`
- API: `http://localhost:5000/api/stats`

## Adding links

### Option 1: Quick script (recommended)
```bash
python scripts/add_link.py "Name" "https://url.com" "Description" "Category"
```

Example:
```bash
python scripts/add_link.py "GitHub" "https://github.com" "Code hosting" "Development"
```

### Option 2: Full manager
```bash
python scripts/manager.py add "Name" "https://url.com" "Description" "Category"
```

### Option 3: Web API (requires server.py running)
```bash
curl -X POST http://localhost:5000/api/links \
  -H "Content-Type: application/json" \
  -d '{"name":"Example","url":"https://example.com","desc":"Cool site","category":"Weird Web"}'
```

### Option 4: Edit directly
Open `links.json` and add:
```json
{
  "name": "Site name",
  "url": "https://example.com",
  "desc": "Short description",
  "category": "Category name"
}
```

Then regenerate `links.js`:
```bash
python scripts/manager.py generate
```

## API Endpoints (when server.py is running)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/links` | List all links |
| GET | `/api/links?limit=10&sort=newest` | List with options |
| POST | `/api/links` | Add new link |
| GET | `/api/stats` | Get statistics |
| POST | `/api/deduplicate` | Remove duplicates |

## Managing links

### List categories
```bash
python scripts/manager.py categories
```

### Search links
```bash
python scripts/manager.py search "term"
```

### Remove duplicates
```bash
python scripts/manager.py duplicates
# or simply
python scripts/deduplicate.py
```

### Validate links
```bash
python scripts/manager.py validate
```

### Export to Markdown
```bash
python scripts/manager.py export
```

## Push to GitHub

```bash
git add .
git commit -m "Add new links"
git push
```

## Link format

```json
{
  "name": "Visible link name",
  "url": "https://full-url.com",
  "desc": "Short description (1-2 lines)",
  "category": "Category (auto-created)"
}
```

## Keyboard shortcuts

- `H` - Go to Home
- `L` - Go to Links

## Requirements

- Python 3.6+ (for scripts)
- Modern browser (Chrome, Firefox, Safari, Edge)

## Notes

- Categories are auto-generated from links
- Check for duplicates before pushing
- URLs should use `https://` when possible
- `links.js` is auto-generated from `links.json`

## License

MIT License
