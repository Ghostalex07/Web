# Aion - Links Hub

> Un hub de enlaces con temática cyberpunk. Colección de websites interesantes organizados por categoría.

## Estructura del Proyecto

```
Web/
├── index.html           # Página principal
├── css/
│   └── styles.css       # Estilos CSS
├── js/
│   └── app.js           # Lógica de la aplicación
├── scripts/
│   ├── manager.py       # Gestor completo de links
│   ├── add_link.py      # Script rápido para agregar un link
│   └── deduplicate.py   # Eliminar duplicados
├── links.json           # Datos de links (fuente de verdad)
├── links.js             # JS con los links (generado automáticamente)
└── README.md            # Documentación
```

## Cómo funciona

1. **`links.json`** - Contiene todos los links en formato JSON (fuente de verdad)
2. **`links.js`** - Archivo JS que carga los links (generado desde JSON)
3. **`css/styles.css`** - Estilos de la página
4. **`js/app.js`** - Lógica de navegación, búsqueda y renderizado
5. **`index.html`** - Página principal que carga todo

## Primeros pasos

### 1. Clonar el repositorio
```bash
git clone https://github.com/Ghostalex07/Web.git
cd Web
```

### 2. Abrir en navegador
```bash
# Con Python
python -m http.server 8000

# Con PHP
php -S localhost:8000

# Con Node.js
npx serve
```

Luego abrir: `http://localhost:8000`

## Agregar links

### Opción 1: Script rápido (recomendado)
```bash
python scripts/add_link.py "Nombre" "https://url.com" "Descripción" "Categoría"
```

Ejemplo:
```bash
python scripts/add_link.py "GitHub" "https://github.com" "Code hosting" "Development"
```

### Opción 2: Gestor completo
```bash
python scripts/manager.py add "Nombre" "https://url.com" "Descripción" "Categoría"
```

### Opción 3: Editar directamente
Abrir `links.json` y agregar:
```json
{
  "name": "Nombre del sitio",
  "url": "https://ejemplo.com",
  "desc": "Descripción breve",
  "category": "Nombre de categoría"
}
```

Después regenerar `links.js`:
```bash
python scripts/manager.py generate
```

## Gestionar links

### Ver categorías
```bash
python scripts/manager.py categories
```

### Buscar links
```bash
python scripts/manager.py search "término"
```

### Eliminar duplicados
```bash
python scripts/manager.py duplicates
# o simplemente
python scripts/deduplicate.py
```

### Validar links
```bash
python scripts/manager.py validate
```

### Exportar a Markdown
```bash
python scripts/manager.py export
```

## Subir cambios a GitHub

```bash
git add .
git commit -m "Agregar nuevos links"
git push
```

## Formato de link

```json
{
  "name": "Nombre visible del link",
  "url": "https://url-completa.com",
  "desc": "Descripción corta (1-2 líneas)",
  "category": "Categoría (se crea automáticamente)"
}
```

## Atajos de teclado

- `H` - Ir a Home
- `L` - Ir a Links
- `Esc` - Limpiar filtros

## Requisitos

- Python 3.6+ (para scripts)
- Navegador moderno (Chrome, Firefox, Safari, Edge)

## Notas

- Las categorías se generan automáticamente desde los links
- Verificar que no haya duplicados antes de hacer push
- Las URLs deben usar `https://` cuando sea posible
- El archivo `links.js` se genera automáticamente desde `links.json`

## Licencia

MIT License
