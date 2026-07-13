# Integración de UD4 en el libro Quarto

## 1. Bloque para `_quarto.yml`

Añadir dentro de `book: chapters:`, como una nueva `part`, en la posición que corresponda a UD4 (tras la `part` de UD3):

```yaml
  - part: "UD4. POO en PHP + Desarrollo de funcionalidades Web"
    chapters:
      - UD4/00-presentacion.qmd
      - UD4/01-ambito-y-clases.qmd
      - UD4/02-constructores-y-encapsulacion.qmd
      - UD4/03-herencia-namespaces-excepciones.qmd
      - UD4/04-poo-avanzada.qmd
      - UD4/05-sesiones.qmd
      - UD4/06-cookies.qmd
      - UD4/07-autenticacion.qmd
      - UD4/08-login-registro.qmd
      - UD4/09-recordarme-y-roles.qmd
      - UD4/10-depuracion-y-cierre.qmd
```

## 2. Fila para `descargas.qmd`

Si `descargas.qmd` usa una tabla markdown con una fila por unidad, añadir (ajustar columnas al formato real de las filas ya existentes de UD1-UD3):

```markdown
| UD4 | POO en PHP + Desarrollo de funcionalidades Web | [PDF](../UD4.pdf) |
```

Revisa el formato exacto de la tabla existente antes de pegar: si las columnas o el estilo de enlace difieren de lo mostrado aquí, ajusta esta fila al patrón real usado en UD1-UD3.

## 3. Pasos manuales

1. Copiar la carpeta `UD4/` (11 ficheros `.qmd`) a la raíz del repo `DWES_Apuntes`, junto a `UD1/`, `UD2/`, `UD3/`.
2. Pegar el bloque YAML del punto 1 en `_quarto.yml`, en el lugar correspondiente dentro de `chapters:`.
3. Añadir la fila del punto 2 en `descargas.qmd`.
4. Ejecutar `quarto preview` en local para comprobar el render antes de hacer commit (aquí no se ha podido renderizar; solo se ha validado la sintaxis Markdown/YAML manualmente).
5. La carpeta `UD4-soluciones/soluciones.md` es para tu gestión aparte del repo privado; no se ha tocado ningún fichero de `DWES_Soluciones`.

## 4. Cambios de esta revisión (fusión con los PDF de referencia)

Tras comparar con `DIAPOSITIVAS_-_ORIENTACIÓN_A_OBJETOS_EN_PHP.pdf` y `8__Programación_orientada_a_objetos_con_PHP.pdf`, se ha añadido contenido ausente del Word origen:

- **`02-constructores-y-encapsulacion.qmd`**: nota de convención de orden dentro de una clase + sección nueva de getters/setters mágicos (`__get`/`__set`).
- **`03-herencia-namespaces-excepciones.qmd`**: sección nueva de polimorfismo, nombrado explícito de "sobreescritura/override", y aviso de que PHP no tiene sobrecarga de métodos.
- **`04-poo-avanzada.qmd` (fichero nuevo)**: clases estáticas (`const`, `static`, `self::`), asignación vs. clonado (`clone`), clases abstractas, interfaces, y métodos de reflexión (`instanceof`, `get_class`, `class_exists`/`method_exists`/`property_exists`, `get_class_methods`/`get_class_vars`/`get_object_vars`). Incluye dos ejercicios de autoevaluación (E4.12, E4.13).
- **Renumeración en cascada**: `04-sesiones.qmd`…`09-depuracion-y-cierre.qmd` pasan a ser `05-sesiones.qmd`…`10-depuracion-y-cierre.qmd`. La numeración de ejercicios (E4.1–E4.13) **no cambia**, es independiente del nombre de fichero.
- `00-presentacion.qmd`: mapa de contenidos y tabla de evaluación actualizados con la fila de POO avanzada y los dos ejercicios nuevos.
- `soluciones.md`: añadidas las soluciones de E4.12 y E4.13.

**Aviso importante — descuadre con el material de aula:** este contenido nuevo (estáticas, clonado, abstractas, interfaces, reflexión) **no estaba en el alcance de 10h/5 sesiones acordado para el bloque de POO** en el Word/PPTX/solucionario de clase de UD4. Lo he incorporado aquí porque el libro Quarto puede servir como referencia más completa que las sesiones presenciales, pero si quieres que las horas de clase, el Word o el PPTX reflejen también este contenido, dímelo explícitamente — no he tocado esos documentos.

## 5. Puntos a revisar tú mismo (no verificables sin Quarto/red)


- **Cross-references**: los bloques de ejercicio usan `::: {#exr-UD4-n}`. Si en UD1-UD3 usas `\@exr-UD1-n` en algún sitio para referenciarlos desde otro capítulo, confirma que el patrón de ID coincide exactamente (sensible a mayúsculas/guiones).
- **Callouts**: se ha usado la sintaxis `::: {.callout-note title="Concepto clave"}` (y variantes `tip`/`warning`/`important`). No he podido confirmar que el tema (`theme/`) no sobrescriba estos títulos por defecto; si en UD1-UD3 los callouts muestran un título distinto al `title=` indicado, puede haber una configuración global que lo fuerce.
- **Numeración de encabezados**: cada `.qmd` empieza con un único `#` (título de capítulo) y usa `##` para las secciones internas, sin YAML propio — coherente con cómo entiendo que están montados UD1-UD3, pero no he podido verificarlo contra esos ficheros en este entorno.
- **`descargas.qmd`**: la fila del punto 2 es una plantilla; el formato real (columnas, si hay icono, si el PDF se genera por CI) depende de cómo esté hecho ese fichero, que no está en mis archivos de proyecto.
