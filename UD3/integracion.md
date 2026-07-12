# Integración de UD3 en el libro Quarto

---

## 1. Bloque a añadir en `_quarto.yml`

A continuación del bloque de UD2 (o donde corresponda):

```yaml
  - part: "UD3. Estructuras de control, funciones y formularios en PHP"
    chapters:
      - UD3/01-presentacion.qmd
      - UD3/02-condicionales.qmd
      - UD3/03-bucles.qmd
      - UD3/04-arrays.qmd
      - UD3/05-funciones.qmd
      - UD3/06-formularios.qmd
      - UD3/07-recogida-datos.qmd
      - UD3/08-evaluacion.qmd
```

> Usa **espacios**, nunca tabuladores. `part` y `chapters` deben quedar al mismo nivel
> de sangría que los bloques de las unidades adyacentes.

---

## 2. Fila a añadir en `descargas.qmd`

```markdown
| UD3 | Estructuras de control en PHP | [Word](assets/UD3_Estructuras_control_PHP.docx) | [PPT](assets/UD3_Estructuras_control_PHP.pptx) |
```

Copia los ficheros `.docx` y `.pptx` a la carpeta `assets/` antes de hacer commit.

---

## 3. Pasos

1. Copia la carpeta `UD3/` (los 8 ficheros `.qmd`) a la raíz del repo.
2. Aplica el bloque YAML del apartado 1 en `_quarto.yml`.
3. Copia los ficheros descargables a `assets/`.
4. Añade la fila en `descargas.qmd`.
5. Ejecuta `quarto preview` en local para verificar el render.
6. Commit y push — GitHub Actions publicará la versión en GitHub Pages.

---

## 4. Notas sobre construcciones Quarto

- `::: {#exr-UD3-n}` — requiere **Quarto ≥ 1.4**. Comprueba con `quarto --version`.
- `{.callout-X title="..."}` con título inline — soportado desde Quarto 1.3.
- No hay HTML crudo en ningún `.qmd`; todo es Markdown estándar + extensiones Quarto.
