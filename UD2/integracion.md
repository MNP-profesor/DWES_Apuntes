# Integración de UD2 en el libro Quarto

## 1. Bloque para `_quarto.yml`

Añadir dentro de la clave `book.chapters`, en la posición que corresponda a UD2
(después de la entrada de UD1 y antes de UD3):

```yaml
  - part: "UD2. Fundamentos de PHP: variables, operadores y sintaxis embebida"
    chapters:
      - UD2/01-presentacion.qmd
      - UD2/02-generacion-embebida.qmd
      - UD2/03-sintaxis-variables.qmd
      - UD2/04-tipos-conversion.qmd
      - UD2/05-directivas-operadores.qmd
      - UD2/06-ambito.qmd
      - UD2/07-evaluacion.qmd
```

El bloque `part + chapters` debe tener exactamente 2 espacios de sangría
respecto a la clave padre. Verificar que el archivo sigue siendo YAML válido
antes de hacer `quarto render`.

---

## 2. Fila para `descargas.qmd`

```markdown
| UD2 | Fundamentos de PHP: variables, operadores y sintaxis embebida | [PDF](descargas/UD2_Fundamentos_PHP.pdf) |
```

Ajustar la ruta al patrón que use el proyecto si difiere de `descargas/`.

---

## 3. Pasos manuales

```bash
# Desde la raíz del repo DWES_Apuntes:
cp -r /ruta/local/UD2  .
git add UD2/
git commit -m "feat(UD2): añadir unidad fundamentos de PHP"
git push
```

Después, editar `_quarto.yml` (apartado 1) y `descargas.qmd` (apartado 2),
y verificar en local:

```bash
quarto preview
```

Comprobar en `http://localhost:4200`:

- La parte «UD2 · Fundamentos de PHP» aparece en el índice lateral.
- Los 7 capítulos se renderizan sin errores.
- Los bloques `#exr-UD2-1` … `#exr-UD2-9` muestran el número de ejercicio.
- Los callouts con títulos `Concepto clave`, `Errores frecuentes`, `Analogía Java`
  y `Normativa · RA-CE` se renderizan correctamente.
- Los bloques de código PHP muestran resaltado de sintaxis.

---

## 4. Construcciones a verificar en el primer render

| Construcción | Fichero | Qué revisar |
|---|---|---|
| `\|\|` escapado en tabla Markdown | `05-directivas-operadores.qmd` | El `\|` debe renderizarse como `\|\|` visible, no como separador de celda |
| `::: {#exr-UD2-n}` con `###` interno | Todos los ficheros con ejercicios | El `###` se trata como H3 dentro del div; si el esquema del libro usa H2 como nivel máximo puede generar saltos de nivel — revisar visualmente |
| `<?= ?>` dentro de fenced code block | `02-generacion-embebida.qmd` | Seguro dentro de bloque de código, pero confirmar que no se interpreta como sintaxis Quarto |
