# Integración de UD1 en el libro Quarto

## 1. Bloque a añadir en `_quarto.yml`

Añade la siguiente entrada dentro de la clave `book.chapters`, en el lugar que corresponda a UD1 (antes de UD2):

```yaml
  - part: "UD1 - Arquitecturas y tecnologías Web en entorno servidor"
    chapters:
      - UD1/00-presentacion.qmd
      - UD1/01-modelo-ejecucion.qmd
      - UD1/02-paginas-dinamicas.qmd
      - UD1/03-servidor-web-aplicaciones.qmd
      - UD1/04-lenguajes-tecnologias.qmd
      - UD1/05-integracion-marcas.qmd
      - UD1/06-herramientas.qmd
```

> **Nota sobre sangría:** Quarto es sensible a la sangría YAML. Asegúrate de que `- part:` queda al mismo nivel que el resto de entradas `- part:` existentes en `book.chapters`.

---

## 2. Fila a añadir en `descargas.qmd`

Añade la siguiente fila en la tabla de descargas, en la sección correspondiente a UD1:

```markdown
| 1 | Arquitecturas y tecnologías web en servidor | [Descargar](download/DWES-UD1.pdf) |
```

> Sustituye `ruta/` por la ruta relativa real donde alojes los ficheros descargables (p. ej. `descargas/` si los colocas en esa carpeta del repo).

---

## 3. Pasos manuales adicionales

### 3a. Copiar la carpeta al repo público

```bash
# Desde la raíz del repo DWES_Apuntes:
cp -r /ruta/a/outputs/UD1 .
git add UD1/
git commit -m "feat: añadir UD1 — Arquitecturas y tecnologías Web en entorno servidor"
git push
```

### 3b. Copiar las soluciones al repo privado

```bash
# Desde la raíz del repo DWES_Soluciones:
cp -r /ruta/a/outputs/UD1-soluciones/. UD1/
git add UD1/
git commit -m "feat: añadir soluciones UD1"
git push
```

> La carpeta de destino en `DWES_Soluciones` debe llamarse `UD1/` (misma convención que en el repo público), y el fichero dentro será `soluciones.md`.

---

## 4. Referencias cruzadas disponibles

Una vez integrada la UD1, puedes referenciar los ejercicios desde cualquier otro `.qmd` del libro con:

```markdown
@exr-UD1-1  →  E1.1 — Clasificación de tecnologías por lugar de ejecución
@exr-UD1-2  →  E1.2 — Estático, dinámico embebido o script independiente
@exr-UD1-3  →  E1.3 — Identificación de roles en una arquitectura real
@exr-UD1-4  →  E1.4 — Estudio comparativo razonado
@exr-UD1-5  →  E1.5 — Trazado manual de la salida generada
@exr-UD1-6  →  E1.6 — Puesta en marcha del entorno de trabajo
```

---

## 5. Advertencias de sintaxis a verificar en el render local

Las siguientes construcciones son correctas en Quarto ≥ 1.4 pero conviene verificarlas en tu entorno exacto:

| Construcción | Estado | Qué comprobar |
|---|---|---|
| `::: {#exr-UD1-n}` con `## Ejercicio E1.n {#exr-UD1-n}` | ✅ Estándar Quarto | El ancla está tanto en el heading como en el div; si Quarto duplica el número en el PDF, elimina el `{#exr-UD1-n}` del heading y conserva solo el del div. |
| `{.striped}` en tablas | ✅ Bootstrap/HTML | Solo aplica en formato `html`; en PDF se ignora sin error. |
| Callouts (`::: {.callout-*}`) | ✅ Estándar Quarto ≥ 1.3 | Verificar que `title=` usa comillas dobles en el YAML del callout. |
| `[php.net/manual/es](https://...)` en `00-presentacion.qmd` | ✅ Markdown estándar | Enlace externo, sin dependencias internas. |
