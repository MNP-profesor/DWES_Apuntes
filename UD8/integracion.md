# Integración de la UD8 en DWES_Apuntes

## 1. Bloque para `_quarto.yml`

Añadir dentro de `book: chapters:`, a continuación del bloque de la UD7:

```yaml
    - part: "UD8 · Páginas web interactivas: PHP y consumo de APIs"
      chapters:
        - UD8/00-presentacion.qmd
        - UD8/01-modelos-ejecucion.qmd
        - UD8/02-tecnologias-frameworks.qmd
        - UD8/03-interaccion-fetch.qmd
        - UD8/04-verificacion-formularios.qmd
        - UD8/05-dom-dinamico.qmd
        - UD8/06-proyecto.qmd
```

La indentación mostrada (4 espacios antes de `- part:`) asume la misma profundidad que las parts existentes; ajústala si tu `_quarto.yml` usa otra.

## 2. Fila para `descargas.qmd`

Añadir a la tabla de descargas, tras la fila de la UD7:

```markdown
| UD8 · Páginas web interactivas: PHP y consumo de APIs | [PDF](download/DWES-UD8.pdf) |
```

El PDF `download/DWES-UD8.pdf` lo genera automáticamente `scripts/build-unit-pdfs.sh` al detectar la carpeta `UD8/`; no requiere paso manual adicional. Verifica tras el primer render que el script la ha recogido.

## 3. Pasos manuales

1. Copiar la carpeta `UD8/` a la raíz del repo `DWES_Apuntes`.
2. Aplicar los cambios de los puntos 1 y 2.
3. `quarto preview` en local y revisar: los siete capítulos en el índice lateral, los callouts con sus títulos, y las referencias `@exr-UD8-1` … `@exr-UD8-5` y `@exr-UD8-e1` … `@exr-UD8-e7` si se usan.
4. Commit y push; GitHub Actions renderiza y publica.

## 4. Notas de validación

- YAML y Markdown validados sintácticamente en local (yaml.safe_load y revisión de bloques de código balanceados, tablas y frontmatter).
- Anclas de ejercicios: `#exr-UD8-1` … `#exr-UD8-5` (ejercicios intercalados) y `#exr-UD8-e1` … `#exr-UD8-e7` (actividades evaluables). Construcción de la que no estoy 100 % seguro: los divs `::: {#exr-...}` sin encabezado interno los renderiza Quarto como entorno "Ejercicio N" numerado automáticamente con la etiqueta en negrita como primer párrafo; si prefieres que el título forme parte del encabezado del entorno, habría que añadir `## título` dentro del div. Compruébalo en el primer `quarto preview` y dime si quieres el otro formato.
- Los diagramas ASCII usan bloques `text` y caracteres de caja Unicode (┌ ─ ▶); se han evitado en los títulos y en el YAML. Si la fuente monoespaciada del tema los desalinea, avísame y los convierto a ASCII puro.
