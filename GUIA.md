# Guía rápida – Amanecer Pinturas

## 1. Subir el sitio a GitHub (una sola vez)
1. Entrá a github.com → **New repository**. Nombre: `amanecer-pinturas`. Marcalo **Public**. Create.
2. En el repositorio: **Add file → Upload files** y arrastrá TODO el contenido de esta carpeta
   (index.html, generar_manifest.py, la carpeta `archivos` y la carpeta oculta `.github`).
   Si no ves `.github`, creá el archivo con **Add file → Create new file**, escribiendo de nombre
   `.github/workflows/publicar.yml` y pegando su contenido.
3. **Settings → Pages → Source: GitHub Actions**.
4. Esperá 1–2 minutos (pestaña **Actions**). Tu link será:
   `https://TU-USUARIO.github.io/amanecer-pinturas/`

## 2. Subir tus archivos (cada vez que quieras)
- Entrá a `archivos/Amanecer` (o `archivos/Opal`) → **Add file → Upload files**.
- Arrastrá los archivos revueltos. El navegador acepta hasta 100 por vez; si tenés 150, subí en 2 tandas.
- **Commit changes**. En 1–2 minutos el sitio se actualiza solo.

## 3. Cómo ponerles nombre
El sitio agrupa solo por el nombre del producto y detecta el tipo por una palabra clave:
- `ficha` → Ficha técnica · `flyer`/`flyers` → Flyer · `catalogo` → Catálogo
- Cualquier otro (ej: "color nuevo") aparece dentro de la misma carpeta del producto.

Ejemplos que se juntan en la carpeta **Goma Liquida**:
`Goma liquida ficha.pdf`, `Goma liquida flyers.jpg`, `Goma liquida color nuevo.jpg`

Regla importante: escribí el nombre del producto igual al principio de cada archivo.
Con `Dura frent duna` y `Durafrent ficha` se juntan, porque el nombre corto va primero.
