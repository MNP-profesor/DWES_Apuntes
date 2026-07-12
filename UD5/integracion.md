# Integración de la UD5 en el libro Quarto

## 1. Bloque para `_quarto.yml`

Añadir dentro de `book.chapters`, a continuación del bloque de la UD4:

```yaml
    - part: "UD5. Separación de la lógica de negocio: MVC con Laravel"
      chapters:
        - UD5/00-presentacion.qmd
        - UD5/01-mvc.qmd
        - UD5/02-instalacion-laravel.qmd
        - UD5/03-rutas-controladores.qmd
        - UD5/04-blade.qmd
        - UD5/05-formularios.qmd
        - UD5/06-eloquent.qmd
        - UD5/07-sesiones.qmd
        - UD5/08-configuracion.qmd
        - UD5/09-poo-servicios.qmd
        - UD5/10-pruebas-proyecto.qmd
```

> Nota: la indentación (4 espacios antes de `- part`) debe coincidir con la de los bloques de las unidades anteriores en tu `_quarto.yml`; ajústala si tu fichero usa otra.

## 2. Fila para `descargas.qmd`

Siguiendo el patrón de las unidades anteriores (fila de tabla Markdown; **ajusta los nombres de columna/enlaces al formato exacto de tu tabla actual** — no tengo el fichero a la vista):

```markdown
| UD5 · MVC con Laravel | [Apuntes (PDF)](pdf/ud5_apuntes.pdf) | [Presentación (PDF)](pdf/ud5_presentacion.pdf) |
```

Recuerda la convención: los PDF generados van con nombre en **minúsculas** para compatibilidad de URLs.

## 3. Pasos manuales

1. Copiar la carpeta `UD5/` a la raíz del repo `DWES_Apuntes` (junto a `UD1/`–`UD4/`). Verificar que la carpeta queda como `UD5` en mayúsculas (en Windows el cambio de mayúsculas puede no registrarse en git: `git mv ud5 UD5` si hiciera falta).
2. Aplicar el bloque del punto 1 a `_quarto.yml` y la fila del punto 2 a `descargas.qmd`.
3. Exportar los PDF del Word y del PPT de la UD5 con nombre en minúsculas (`ud5_apuntes.pdf`, `ud5_presentacion.pdf`, o el patrón que uses) y colocarlos donde residan los de las otras unidades.
4. `quarto preview` en local: comprobar en particular
   - los tres cross-refs `@sec-ud5-eloquent` (en `00-presentacion.qmd` y `05-formularios.qmd`), `@sec-ud5-instalacion` y `@sec-ud5-pruebas` (en `08-configuracion.qmd` y `09-poo-servicios.qmd`),
   - la numeración de los bloques de ejercicio `#exr-UD5-1` … `#exr-UD5-9`.
5. Commit y push. El workflow de GitHub Pages publica.

## 4. Avisos de validación

- Sintaxis Markdown y YAML revisadas fichero a fichero; sin HTML crudo en ningún `.qmd`.
- Construcción de la que no estoy 100% seguro sin renderizar: el uso de `@sec-...` **dentro de un comentario PHPDoc en un bloque de código** se evitó a propósito (las referencias solo aparecen en prosa), pero verifica en el preview que ninguna referencia haya quedado dentro de bloques ```` ``` ````, donde Quarto no las resuelve.
- Los bloques `::: {#exr-...}` usan un encabezado interno de nivel `###`; si en las UD anteriores usaste otro nivel, unifícalo (es solo estético, no rompe el render).
