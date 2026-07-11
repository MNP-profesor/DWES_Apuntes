# Apuntes DWES · 2º DAW (Módulo 0613)

Libro Quarto con los apuntes del módulo **Desarrollo Web en Entorno Servidor**.
Web pública con descargas en PDF y EPUB, regeneradas automáticamente en cada actualización.

**Autor:** Manel Navarro Pérez · Licencia CC BY-NC-SA 4.0

---

## Puesta en marcha (una sola vez)

### 1. Requisitos en tu equipo

- [Git](https://git-scm.com)
- [Quarto](https://quarto.org/docs/get-started/)
- VS Code + extensión **Quarto**
- Para renderizar PDF en local: `quarto install tinytex`

### 2. Configuración del repositorio en GitHub

1. Crea el repositorio público `dwes-apuntes` (vacío, sin README).
2. En **Settings → Pages → Build and deployment → Source**, selecciona **GitHub Actions**.
3. Edita `_quarto.yml` y sustituye `USUARIO` por tu usuario de GitHub en `repo-url`.

### 3. Primera subida

Desde la carpeta de este proyecto:

```bash
git init
git add .
git commit -m "Esqueleto del libro Quarto DWES"
git branch -M main
git remote add origin https://github.com/MNP-profesor/DWES_Apuntes.git
git push -u origin main
```

En ~3-5 minutos (el primer PDF tarda algo más), la web estará en
`https://github.com/MNP-profesor/DWES_Apuntes`.

---

## Trabajo en local

```bash
quarto preview        # web con recarga en vivo mientras editas
quarto render         # genera HTML + PDF + EPUB en _book/
```

No necesitas renderizar antes de subir: GitHub Actions lo hace por ti en cada `push`.

---

## Añadir una unidad (flujo por UD)

1. Copia la carpeta `UDX/` recibida a la raíz del repo.
2. En `_quarto.yml`, descomenta el bloque de la unidad y ajusta sus ficheros.
3. En `descargas.qmd`, descomenta la fila de la unidad.
4. Sube los cambios:

```bash
git add .
git commit -m "UDX: versión web"
git push
```

## Editar contenido

Cada fichero `.qmd` es Markdown estándar con extras de Quarto (callouts, referencias cruzadas). Se edita con VS Code (previsualización con `quarto preview`) o directamente desde github.com (icono ✏️ en cada página de la web, enlace «Edit this page»).

### Chuleta de callouts del módulo

```markdown
::: {.callout-note title="Concepto clave"}
...
:::

::: {.callout-tip title="Analogía Java"}
...
:::

::: {.callout-warning title="Errores frecuentes"}
...
:::

::: {.callout-important title="Normativa · RA-CE"}
...
:::
```

---

## Estructura

```
dwes-apuntes/
├── _quarto.yml            # configuración del libro (capítulos, formatos)
├── index.qmd              # presentación del módulo
├── descargas.qmd          # página de descargas PDF/EPUB
├── UD1/ … UD9/            # una carpeta por unidad (.qmd)
├── theme/                 # tema Midnight (SCSS web, LaTeX PDF, portada)
├── scripts/build-unit-pdfs.sh   # PDF independiente por unidad
└── .github/workflows/publish.yml # publicación automática
```

Las **soluciones de los ejercicios** viven en el repo privado `dwes-soluciones`
y nunca deben añadirse a este repositorio.
