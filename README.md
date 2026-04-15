# Aion - Links Hub

Un hub de links con temática cyberpunk. Una colección de websites interesantes organizados por categoría.

## Estructura

```
Web/
├── index.html    # Página principal (HTML + CSS + JS)
├── links.json    # Datos de links (fuente de verdad)
├── links.js      # JS con los links (generado desde JSON)
└── README.md    # Este archivo
```

## Cómo funciona

1. `links.json` contiene todos los links en formato JSON
2. `links.js` es un archivo JS que carga los links (generado automáticamente)
3. `index.html` carga `links.js` y renderiza los links por categoría

## Cómo agregar más links

### Opción 1: Editar directamente links.json

Agregar un objeto con este formato:

```json
{
  "name": "Nombre del sitio",
  "url": "https://ejemplo.com",
  "desc": "Descripción breve",
  "category": "Nombre de categoría"
}
```

### Opción 2: Regenerar links.js desde JSON

Si modificas `links.json`, regenera `links.js`:

```bash
python3 -c "
import json
with open('links.json', 'r') as f:
    links = json.load(f)
with open('links.js', 'w') as f:
    f.write(f'const linksData = {json.dumps(links, ensure_ascii=False)};\n')
print(f'Generated links.js with {len(links)} links')
"
```

### Opción 3: Script para agregar links

```python
import json

with open('links.json', 'r') as f:
    links = json.load(f)

existing_urls = {link['url'] for link in links}

nuevos_links = [
    {"name": "Nuevo Sitio", "url": "https://ejemplo.com", "desc": "Descripción", "category": "Categoría"}
]

for link in nuevos_links:
    if link['url'] not in existing_urls:
        links.append(link)
        existing_urls.add(link['url'])

with open('links.json', 'w') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)
```

## Eliminar duplicados

```python
import json

with open('links.json', 'r') as f:
    links = json.load(f)

seen = set()
unique_links = []
for link in links:
    if link['url'] not in seen:
        unique_links.append(link)
        seen.add(link['url'])

print(f"Original: {len(links)}, Unique: {len(unique_links)}")

with open('links.json', 'w') as f:
    json.dump(unique_links, f, ensure_ascii=False, indent=2)
```

## Push a GitHub

```bash
git add links.json links.js
git commit -m "Agregar nuevos links"
git push
```

## Notas

- **No editar `index.html`** para agregar links - usa `links.json`
- Las categorías se generan automáticamente desde los links
- Verificar que no haya duplicados antes de hacer push
- Las URLs deben usar `https://` cuando sea posible

## Formato de link

```json
{
  "name": "Nombre visible del link",
  "url": "https://url-completa.com",
  "desc": "Descripción corta (1-2 líneas)",
  "category": "Categoría (se creará automáticamente)"
}
```

## Categorías actuales

- Weird Web
- Knowledge
- Tools
- Fun
- Privacy
- Search

(Las categorías se generan dinámicamente según los links existentes)
