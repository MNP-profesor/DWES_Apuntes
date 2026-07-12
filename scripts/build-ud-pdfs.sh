#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════
# Genera un PDF independiente por unidad (DWES-UDX.pdf).
# Para cada carpeta UD1..UD9 con ficheros .qmd, crea un proyecto
# Quarto temporal con solo esa unidad y lo renderiza a PDF.
# Salida: _UD-PDF/DWES-UDX.pdf
# ══════════════════════════════════════════════════════════════
set -euo pipefail

ROOT="$(pwd)"
OUT="$ROOT/_ud-pdfs"
mkdir -p "$OUT"

declare -A TITULOS=(
  [UD1]="UD1. Arquitecturas y tecnologías de programación Web en servidor"
  [UD2]="UD2. Fundamentos de PHP: variables, operadores y sintaxis embebida"
  [UD3]="UD3. Estructuras de control, funciones y formularios en PHP"
  [UD4]="UD4. POO en PHP + Desarrollo de funcionalidades Web: autenticación, sesiones y cookies"
  [UD5]="UD5. Separación de la lógica de negocio: MVC con Laravel"
  [UD6]="UD6. Acceso a BBDD con PDO: seguridad e integridad"
  [UD7]="UD7. Servicios Web: API REST con Laravel (Resources y Sanctum)"
  [UD8]="UD8. Generación dinámica de páginas Web"
  [UD9]="UD9. Aplicaciones web híbridas: librerías y repositorios heterogéneos (Composer)"
)

for dir in UD1 UD2 UD3 UD4 UD5 UD6 UD7 UD8 UD9; do
  [ -d "$ROOT/$dir" ] || continue
  mapfile -t qmds < <(find "$ROOT/$dir" -maxdepth 1 -name '*.qmd' | sort)
  [ ${#qmds[@]} -gt 0 ] || continue

  echo "── Generando PDF de $dir ──"
  tmp="$(mktemp -d)"
  cp -r "$ROOT/$dir" "$tmp/"
  cp -r "$ROOT/theme" "$tmp/"

  # index.qmd mínimo obligatorio para proyectos tipo book
  cat > "$tmp/index.qmd" << 'IDX'
# Presentación {.unnumbered}

Unidad didáctica del módulo **Desarrollo Web en Entorno Servidor** (DWES, 0613) | 2º DAW.
IDX

  {
    echo "project:"
    echo "  type: book"
    echo "lang: es"
    echo "book:"
    echo "  title: \"${TITULOS[$dir]:-$dir}\""
    echo "  subtitle: \"DWES | Módulo 0613 | 2º DAW\""
    echo "  author: \"Manel Navarro Pérez\""
    echo "  output-file: \"DWES-$dir\""
    echo "  chapters:"
    echo "    - index.qmd"
    for f in "${qmds[@]}"; do
      echo "    - $dir/$(basename "$f")"
    done
    cat << 'FMT'
format:
  pdf:
    documentclass: scrreprt
    papersize: a4
    geometry:
      - top=2.5cm
      - bottom=2.5cm
      - left=2.5cm
      - right=2.2cm
    toc: true
    toc-depth: 2
    number-sections: false
    colorlinks: true
    linkcolor: MidnightCoral
    urlcolor: MidnightCoral
    highlight-style: tango
    code-block-bg: "#EFF3FB"
    include-in-header: theme/pdf-header.tex
FMT
  } > "$tmp/_quarto.yml"

  (cd "$tmp" && quarto render --to pdf)
  cp "$tmp/_book/DWES-$dir.pdf" "$OUT/"
  rm -rf "$tmp"
done

echo "PDFs por UD generados en $OUT:"
ls -1 "$OUT" || true
