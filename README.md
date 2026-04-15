# Aion - Links Hub

> A cyberpunk-themed links hub. A collection of interesting websites organized by category.

## Project Structure

```
Web/
├── index.html           # Main page (HTML + CSS + inline JS)
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
3. **`index.html`** - Main page that loads everything
4. **`scripts/`** - Scripts to manage links

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Ghostalex07/Web.git
cd Web
```

### 2. Open in browser
```bash
# With Python
python -m http.server 8000

# With PHP
php -S localhost:8000

# With Node.js
npx serve
```

Then open: `http://localhost:8000`

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

### Option 3: Edit directly
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
