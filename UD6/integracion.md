# Integración de la UD6 en el libro DWES

Pasos para incorporar la unidad al libro. Solo tocas dos ficheros del esqueleto; el resto ya existe.

## 1. Copiar la carpeta

Copia la carpeta `UD6/` (con sus 8 `.qmd`) a la raíz del proyecto del libro, junto a las demás `UD1/`…`UD5/`.

## 2. Bloque para `_quarto.yml`

Añade este `part` dentro de `book:` → `chapters:`, en el orden que corresponda (después del bloque de la UD5):

```yaml
  - part: "UD6. Acceso a BBDD con PDO: seguridad e integridad"
    chapters:
      - UD6/00-presentacion.qmd
      - UD6/01-tecnologias-acceso.qmd
      - UD6/02-conexion-pdo.qmd
      - UD6/03-recuperacion-seguridad.qmd
      - UD6/04-publicacion-web.qmd
      - UD6/05-conjuntos-datos.qmd
      - UD6/06-crud-transacciones.qmd
      - UD6/07-proyecto.qmd
```

## 3. Fila para `descargas.qmd`

Añade la fila de la UD6 a la tabla de descargas. Ajusta las columnas para que **coincidan exactamente** con la cabecera que ya tengas en ese fichero (esta es la forma habitual, con el PDF en minúsculas por compatibilidad de URL):

```markdown
| UD6 · Acceso a datos con PDO | [PDF](pdf/ud6.pdf) |
```

> Si tu tabla de `descargas.qmd` tiene más columnas (p. ej. una de "Contenido" o "Soluciones"), replica el patrón de las filas UD1–UD5 y rellena solo la celda del PDF público; no añadas aquí enlaces a soluciones.

## 4. Render y publicación

```bash
quarto preview        # revisión local
# git add UD6/ _quarto.yml descargas.qmd
# git commit -m "UD6: acceso a datos con PDO"
# git push
```

## Notas de validación (revísalas al renderizar)

- **Sin H1 en el cuerpo**: cada `.qmd` toma su título del `title:` del frontmatter; no hay `#` de nivel 1 en el cuerpo, para evitar la doble numeración que corregimos en la UD3.
- **Callouts**: usan los cuatro tipos y títulos fijos (`note` = "Concepto clave", `tip` = "Analogía Java", `warning` = "Errores frecuentes"). En esta unidad no aparece `important` ("Normativa · RA-CE") porque la presentación web omite la referencia a la ley, según lo acordado.
- **Ejercicios**: cada uno va en `::: {#exr-UD6-n}` con el título en negrita dentro del bloque (no como encabezado), igual que en UD3–UD5, para que no se numeren dos veces. La forma en que tu tema renderiza los bloques `#exr-` es la que ya tienes configurada; aquí solo respeto la convención.
- **Salidas esperadas**: las que muestran los apuntes asumen los tres contactos de la base de prácticas definida en `00-presentacion.qmd`. Son reproducibles si importas ese `INSERT`.
- **Java**: solo hay dos analogías (en `03` y `05`), ambas donde PHP se comporta distinto a Java (binding por array asociativo y orden de hidratación de `FETCH_CLASS`).

Todo el Markdown y el YAML se han validado sintácticamente. No hay construcciones de las que dude, salvo el detalle de columnas de `descargas.qmd`, que depende de tu tabla actual (ver punto 3).
