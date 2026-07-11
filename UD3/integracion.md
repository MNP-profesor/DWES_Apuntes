# Integración de UD3 en el libro Quarto

Instrucciones para incorporar la carpeta `UD3/` al repo público `DWES_Apuntes`
y la carpeta `UD3-soluciones/` al repo privado `DWES_Soluciones`.

---

## 1. Bloque a añadir en `_quarto.yml`

Añade este bloque dentro de la clave `chapters:`, a continuación del bloque de UD2
(o donde corresponda según el orden del módulo):

```yaml
  - part: "UD3 - Estructuras de control, funciones y formularios en PHP"
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

> **Atención de indentación:** en YAML, `part` y `chapters` deben quedar al mismo
> nivel de sangría que los bloques `part` de las unidades adyacentes.
> Usa **espacios** (nunca tabuladores).

---

## 2. Fila a añadir en `descargas.qmd`

Añade esta fila en la tabla de descargas, en la columna correspondiente a UD3:

```markdown
| 3 | Estructuras de control, funciones y formularios en PHP | [Descargar](download/DWES-UD3.pdf) |
```

> Los ficheros `.docx` y `.pptx` deben copiarse a la carpeta `assets/` del repo
> (o la ruta que uses para recursos descargables) antes de hacer el commit.

---

## 3. Pasos manuales en el repo público (`DWES_Apuntes`)

1. Copia la carpeta `UD3/` (los 8 ficheros `.qmd`) en la raíz del repo.
2. Aplica el bloque YAML del apartado 1 en `_quarto.yml`.
3. Copia los ficheros `UD3_Estructuras_control_PHP.docx` y
   `UD3_Estructuras_control_PHP.pptx` a `assets/`.
4. Añade la fila en `descargas.qmd` (apartado 2).
5. Ejecuta `quarto preview` en local para verificar el render antes de hacer push.
6. Haz commit y push; GitHub Actions publicará la nueva versión en GitHub Pages.

---

## 4. Pasos manuales en el repo privado (`DWES_Soluciones`)

1. Copia la carpeta `UD3-soluciones/` en la raíz del repo **renombrándola `UD3/`**,
   de modo que la ruta quede `UD3/soluciones.md`.
2. Si el repo de soluciones tiene su propio `_quarto.yml`, añade el mismo bloque
   `part` del apartado 1 apuntando a `UD3/soluciones.md` en lugar de los 8 ficheros.

---

## 5. Notas sobre construcciones no estándar

Las siguientes construcciones de los ficheros `.qmd` **requieren Quarto ≥ 1.4**
(verificado con la spec de Quarto 1.4/1.5 vigente en la fecha de generación):

- `::: {#exr-UD3-n}` — bloques de ejercicio con ID para referencias cruzadas
  (`@exr-UD3-1`). Requiere la extensión `quarto-ext/exercise` o bien Quarto ≥ 1.4
  con soporte nativo de `callout` tipado. Si el render falla, comprueba la versión
  de Quarto instalada con `quarto --version`.
- `{.callout-important title="..."}` con `title` inline — sintaxis soportada desde
  Quarto 1.3. En versiones anteriores el título debe ir en la primera línea del
  bloque como texto plano.
- Las tablas de código con `php` como etiqueta de lenguaje en bloques de código
  dentro de un fichero `.qmd` que también contiene código HTML en ejercicios
  (E3.8): Quarto los trata como bloques de código literal; no hay ambigüedad.

> **No hay HTML crudo** en ningún fichero `.qmd` de esta unidad; todo es Markdown
> estándar + extensiones Quarto. Los bloques de código PHP y HTML dentro de los
> ejercicios y soluciones son bloques de código delimitados por tres acentos
> graves, no HTML embebido en el documento.
