# Integración de la UD9 en DWES_Apuntes

## 1. Bloque para `_quarto.yml`

Añadir dentro de `book:` → `chapters:`, a continuación de la part de la UD8:

```yaml
  - part: "UD9 · Aplicaciones Web híbridas"
    chapters:
      - UD9/00-presentacion.qmd
      - UD9/01-aplicaciones-hibridas.qmd
      - UD9/02-composer.qmd
      - UD9/03-consumo-repositorios.qmd
      - UD9/04-repositorios-propios.qmd
      - UD9/05-librerias-terceros.qmd
      - UD9/06-analitica-bigdata.qmd
      - UD9/07-prueba-documentacion.qmd
      - UD9/08-evaluacion.qmd
```

(Respeta la indentación exacta de las parts anteriores del fichero.)

## 2. Fila para `descargas.qmd`

Añadir a la tabla de descargas, tras la fila de la UD8:

```markdown
| UD9 · Aplicaciones Web híbridas: librerías y repositorios heterogéneos | [PDF](download/DWES-UD9.pdf) |
```

Ajusta el texto de las celdas al formato exacto de las filas existentes si difiere. El PDF `download/DWES-UD9.pdf` lo genera automáticamente `scripts/build-unit-pdfs.sh` al detectar la nueva carpeta `UD9/`.

## 3. Pasos manuales

1. Copiar la carpeta `UD9/` a la raíz del repositorio.
2. Aplicar los cambios de los puntos 1 y 2.
3. Verificar en local con `quarto preview` antes de hacer commit.
4. Antes del commit, `Ctrl+Shift+F` sobre "UD9" para confirmar que no queda ninguna referencia pendiente (índices, navegación).

## 4. Notas de validación

- Sintaxis Markdown y YAML revisadas manualmente en todos los ficheros (aquí no hay Quarto para renderizar).
- **Construcción a verificar en el primer render**: los ejercicios usan el patrón de div con identificador `::: {#exr-UD9-n}` con un encabezado `####` en su interior como título del ejercicio (p. ej. `#### E9.1 · Restricciones de versión`). El identificador va **solo en el div**, no duplicado en el encabezado, para evitar IDs repetidos; las referencias cruzadas de `08-evaluacion.qmd` (`@exr-UD9-1` … `@exr-UD9-11`) resuelven contra esos divs. Si en las unidades anteriores el patrón renderizado difiere (p. ej. encabezado fuera del div), unifica con un reemplazo global antes del commit.
- Los bloques de salida de ejemplos usan la etiqueta `text`; los de comandos, `bash`; los de configuración, `json`/`yaml`; todo el código PHP lleva etiqueta `php` (incluidos los fragmentos Blade, para heredar el resaltado).
- Numeración de ejercicios: E9.1–E9.6 (aprendizaje, intercalados) y E9.7–E9.11 (proyecto, al cierre de su capítulo). E9.7 aparece en el capítulo 2, antes que E9.3 (capítulo 3): es intencionado, conforme al esquema acordado de numerar los ejercicios de proyecto a continuación de los de aprendizaje.
