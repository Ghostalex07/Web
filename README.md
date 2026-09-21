# Aion - Links Hub

> A cyberpunk-themed links hub. 7,500+ curated links organized into 22 categories with subcategories.

## Project Structure

```
Web/
├── index.html              # Main page
├── css/style.css           # Styles
├── js/app.js               # Frontend logic
├── links.js                # Auto-generated from links.json
├── scripts/
│   ├── manager.py          # CLI: add, search, validate, export
│   ├── migrate.py          # Category migration tool
│   ├── stats.py            # Database statistics
│   ├── health_check.py     # Check URLs are alive
│   ├── add_link.py         # Quick add a link
│   └── deduplicate.py      # Remove duplicates
├── links.json              # Source of truth (all links)
├── niche_websites.json     # Additional niche links
├── README.md
└── LICENSE
```

## Quick Start

```bash
# Serve locally
python -m http.server 8000
# or
npx serve
```

Open `http://localhost:8000`

## Managing Links

```bash
# Add a link
python scripts/manager.py add "Name" "https://url.com" "Description" "Category" "Subcategory"

# List all categories
python scripts/manager.py categories

# Search
python scripts/manager.py search "privacy"

# Validate links
python scripts/manager.py validate

# Export to Markdown
python scripts/manager.py export

# Regenerate links.js
python scripts/manager.py generate

# Database stats
python scripts/stats.py

# Check URLs (first 50)
python scripts/health_check.py 50
```

## Link Format

```json
{
  "name": "Site Name",
  "url": "https://example.com",
  "desc": "Short description",
  "category": "Technology",
  "subcategory": "Programming"
}
```

## Keyboard Shortcuts

- `H` — Home
- `L` — Links
- `A` — About
- `/` — Focus search
- `?` — Show shortcuts
- `T` — Toggle theme
- `R` — Refresh random picks

## License

MIT License
