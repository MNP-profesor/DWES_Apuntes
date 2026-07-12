# Integración de la UD7 en `DWES_Apuntes`

## 1. Copiar la carpeta

Copia la carpeta `UD7/` completa (10 ficheros, `00-presentacion.qmd` … `09-documentacion.qmd`) a la raíz del repositorio.

## 2. Bloque para `_quarto.yml`

Añade este bloque a la lista de `chapters`/`parts` del libro, a continuación de la parte de la UD6:

```yaml
  - part: "UD7. Servicios web: API REST"
    chapters:
      - UD7/00-presentacion.qmd
      - UD7/01-fundamentos.qmd
      - UD7/02-rutas-api.qmd
      - UD7/03-api-resources.qmd
      - UD7/04-validacion-codigos.qmd
      - UD7/05-sanctum.qmd
      - UD7/06-verificacion.qmd
      - UD7/07-consumo.qmd
      - UD7/08-proyecto.qmd
      - UD7/09-documentacion.qmd
```

La indentación mostrada (dos espacios antes de `- part:`) corresponde a un elemento de la lista de `chapters` del `book`; ajústala si tu `_quarto.yml` anida las partes a otro nivel — comprueba cómo están las UD1–UD6 y replica exactamente su sangría.

## 3. Fila para `descargas.qmd`

Añade la fila de la UD7 a la tabla de descargas, siguiendo el patrón de una columna de PDF por unidad:

```markdown
| UD7 · Desarrollo de servicios web: API REST con Laravel | [DWES-UD7.pdf](download/DWES-UD7.pdf) |
```

El PDF `download/DWES-UD7.pdf` lo genera automáticamente `scripts/build-unit-pdfs.sh` a partir de la carpeta `UD7/`; verifica que el script recorre las unidades por patrón (`UD*/`) y no por lista fija — si es lista fija, añade `UD7` a ella.

## 4. Verificación local

```bash
quarto preview
```

Comprobaciones sugeridas antes del *commit*:

- Las referencias cruzadas `@exr-UD7-7`, `@exr-UD7-9` y `@exr-UD7-10` resuelven (aparecen en `00-presentacion.qmd`, `08-proyecto.qmd` y `09-documentacion.qmd`).
- Los diez ejercicios se numeran en orden E7.1 → E7.10 al renderizar.
- Los cuatro tipos de *callout* muestran sus títulos fijos (en esta unidad solo aparecen `note`, `warning` e `important`; no hay `tip`/Analogía Java, decisión validada).

## 5. Notas de validación

- Sintaxis Markdown/YAML revisada en los 10 `.qmd` (frontmatter YAML válido, cercas de código balanceadas con etiqueta de lenguaje, divs `:::` balanceados).
- Etiquetas de lenguaje usadas: `php`, `bash`, `yaml`, `json`, `text`, `xml`, `javascript` y `markdown` (en este fichero). Las tres últimas van más allá del conjunto habitual del libro (`php`, `html`, `yaml`, `bash`, `text`): `json`, `xml` y `javascript` son lenguajes estándar de Pandoc y deberían resaltar sin configuración extra, pero verifícalo en el primer render.
- Los identificadores `#exr-UD7-n` usan mayúsculas en «UD7»: coherente con las unidades anteriores; los identificadores de Quarto distinguen mayúsculas, así que las referencias `@exr-UD7-n` las respetan.
