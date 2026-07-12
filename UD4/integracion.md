# Integración de UD4 en el libro Quarto

## 1. Bloque para `_quarto.yml`

Añadir dentro de `book: chapters:`, como una nueva `part`, en la posición que corresponda a UD4 (tras la `part` de UD3):

```yaml
  - part: "UD4. POO en PHP y Desarrollo de funcionalidades Web: autenticación, sesiones y cookies"
    chapters:
      - UD4/00-presentacion.qmd
      - UD4/01-ambito-y-clases.qmd
      - UD4/02-constructores-y-encapsulacion.qmd
      - UD4/03-herencia-namespaces-excepciones.qmd
      - UD4/04-sesiones.qmd
      - UD4/05-cookies.qmd
      - UD4/06-autenticacion.qmd
      - UD4/07-login-registro.qmd
      - UD4/08-recordarme-y-roles.qmd
      - UD4/09-depuracion-y-cierre.qmd
```

## 2. Fila para `descargas.qmd`

Si `descargas.qmd` usa una tabla markdown con una fila por unidad, añadir (ajustar columnas al formato real de las filas ya existentes de UD1-UD3):

```markdown
| UD4 | POO en PHP + Desarrollo de funcionalidades Web | [PDF](../UD4.pdf) |
```

Revisa el formato exacto de la tabla existente antes de pegar: si las columnas o el estilo de enlace difieren de lo mostrado aquí, ajusta esta fila al patrón real usado en UD1-UD3.

## 3. Pasos manuales

1. Copiar la carpeta `UD4/` (10 ficheros `.qmd`) a la raíz del repo `DWES_Apuntes`, junto a `UD1/`, `UD2/`, `UD3/`.
2. Pegar el bloque YAML del punto 1 en `_quarto.yml`, en el lugar correspondiente dentro de `chapters:`.
3. Añadir la fila del punto 2 en `descargas.qmd`.
4. Ejecutar `quarto preview` en local para comprobar el render antes de hacer commit (aquí no se ha podido renderizar; solo se ha validado la sintaxis Markdown/YAML manualmente).
5. La carpeta `UD4-soluciones/soluciones.md` es para tu gestión aparte del repo privado; no se ha tocado ningún fichero de `DWES_Soluciones`.

## 4. Puntos a revisar tú mismo (no verificables sin Quarto/red)

- **Cross-references**: los bloques de ejercicio usan `::: {#exr-UD4-n}`. Si en UD1-UD3 usas `\@exr-UD1-n` en algún sitio para referenciarlos desde otro capítulo, confirma que el patrón de ID coincide exactamente (sensible a mayúsculas/guiones).
- **Callouts**: se ha usado la sintaxis `::: {.callout-note title="Concepto clave"}` (y variantes `tip`/`warning`/`important`). No he podido confirmar que el tema (`theme/`) no sobrescriba estos títulos por defecto; si en UD1-UD3 los callouts muestran un título distinto al `title=` indicado, puede haber una configuración global que lo fuerce.
- **Numeración de encabezados**: cada `.qmd` empieza con un único `#` (título de capítulo) y usa `##` para las secciones internas, sin YAML propio — coherente con cómo entiendo que están montados UD1-UD3, pero no he podido verificarlo contra esos ficheros en este entorno.
- **`descargas.qmd`**: la fila del punto 2 es una plantilla; el formato real (columnas, si hay icono, si el PDF se genera por CI) depende de cómo esté hecho ese fichero, que no está en mis archivos de proyecto.
