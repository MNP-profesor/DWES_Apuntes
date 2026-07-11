# Integración de UD2 en el libro Quarto

## 1. Bloque para `_quarto.yml`

Añadir dentro de la clave `book.chapters`, en la posición que corresponda a UD2
(después de la entrada de UD1 y antes de UD3). El bloque completo de la parte:

```yaml
  - part: "UD2 - Fundamentos de PHP"
    chapters:
      - UD2/01-presentacion.qmd
      - UD2/02-generacion-embebida.qmd
      - UD2/03-sintaxis-variables.qmd
      - UD2/04-tipos-conversion.qmd
      - UD2/05-directivas-operadores.qmd
      - UD2/06-ambito.qmd
      - UD2/07-evaluacion.qmd
```

> **Nota de sangría:** en `_quarto.yml` la clave `chapters` del libro principal
> suele estar al mismo nivel que `title`, `author`, etc. El bloque `part + chapters`
> debe tener exactamente 2 espacios de sangría respecto a la clave padre.
> Verificar que el archivo final siga siendo YAML válido antes de hacer `quarto render`.

---

## 2. Fila para `descargas.qmd`

Añadir una fila en la tabla de descargas apuntando al PDF de la UD2.
El PDF lo genera Quarto automáticamente si el libro tiene `format: pdf` activo
o si se genera por separado. Ajustar la ruta al patrón que use el proyecto:

```markdown
| 2 | Fundamentos de PHP | [Descargar](download/DWES-UD2.pdf) |
```

> Sustituir `<org>` por el nombre de organización/usuario real del repositorio privado.

---

## 3. Pasos manuales

### 3a. Copiar la carpeta de contenido (repo público)

```bash
# Desde la raíz del repo DWES_Apuntes:
cp -r /ruta/local/UD2  .
git add UD2/
git commit -m "feat(UD2): añadir unidad fundamentos de PHP"
git push
```

### 3b. Copiar la carpeta de soluciones (repo privado)

```bash
# Desde la raíz del repo DWES_Soluciones:
cp -r /ruta/local/UD2-soluciones  ./UD2
git add UD2/
git commit -m "feat(UD2): añadir soluciones fundamentos de PHP"
git push
```

### 3c. Aplicar el bloque de `_quarto.yml`

Editar `_quarto.yml` en el repo público e insertar el bloque del apartado 1.

### 3d. Aplicar la fila de `descargas.qmd`

Editar `descargas.qmd` en el repo público e insertar la fila del apartado 2.

### 3e. Verificación local antes de publicar

```bash
quarto preview
```

Abrir el navegador en `http://localhost:4200` y comprobar:

- La parte «UD2 · Fundamentos de PHP» aparece en el índice lateral.
- Los 7 capítulos se renderizan sin errores.
- Los bloques de ejercicio (`#exr-UD2-1` … `#exr-UD2-9`) muestran el número de ejercicio.
- Los callouts (`note`, `tip`, `warning`, `important`) se renderizan con sus títulos fijos.
- Los bloques de código PHP muestran resaltado de sintaxis.

---

## 4. Construcciones a verificar en el render local

Las siguientes construcciones son sintácticamente correctas en Quarto/Pandoc
pero conviene confirmarlas visualmente en el primer render:

| Construcción | Fichero | Posible problema |
|---|---|---|
| Tabla con columna de porcentajes (`---:`) | `07-evaluacion.qmd` | Alineación derecha — verificar que el render no la ignore |
| Tabla con columna de `✓` centrada (`:---:`) | `07-evaluacion.qmd` | Los símbolos Unicode ✓ deben mostrarse correctamente en HTML y PDF |
| Operadores `\|\|` escapados en tabla Markdown | `05-directivas-operadores.qmd` | En tablas Markdown el `|` debe escaparse como `\|`; ya está aplicado |
| Bloque `::: {#exr-UD2-n}` con `###` interno | Todos los ficheros con ejercicios | Quarto trata el `###` como H3 dentro del div; si el esquema de numeración de capítulos ya usa H2/H3, puede haber saltos de nivel — revisar visualmente |
| `<?= ?>` en bloques de código php | `02-generacion-embebida.qmd` | No debe interpretarse como código Quarto; al estar dentro de fenced code block es seguro, pero confirmar en el render |
