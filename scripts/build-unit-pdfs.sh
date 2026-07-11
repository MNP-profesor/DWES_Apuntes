#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════
# Genera un PDF independiente por unidad (dwes-udX.pdf).
# Para cada carpeta ud1..ud9 con ficheros .qmd, crea un proyecto
# Quarto temporal con solo esa unidad y lo renderiza a PDF.
# Salida: _unit-pdfs/dwes-udX.pdf
# ══════════════════════════════════════════════════════════════
set -euo pipefail

ROOT="$(pwd)"
OUT="$ROOT/_unit-pdfs"
mkdir -p "$OUT"

declare -A TITULOS=(
  [ud1]="UD1 · Arquitecturas y tecnologías web en servidor"
  [ud2]="UD2 · Inserción de código PHP en páginas web"
  [ud3]="UD3 · Estructuras de programación, funciones y formularios"
  [ud4]="UD4 · POO en PHP: autenticación, sesiones y cookies"
  [ud5]="UD5 · Separación de la lógica de negocio: MVC con Laravel"
  [ud6]="UD6 · Acceso a almacenes de datos con PDO"
  [ud7]="UD7 · Servicios web REST"
  [ud8]="UD8 · Páginas web dinámicas e interactivas"
  [ud9]="UD9 · Aplicaciones web híbridas: Composer y repositorios heterogéneos"
)

for dir in ud1 ud2 ud3 ud4 ud5 ud6 ud7 ud8 ud9; do
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

Unidad didáctica del módulo **Desarrollo Web en Entorno Servidor** (DWES, 0613) · 2º DAW.
IDX

  {
    echo "project:"
    echo "  type: book"
    echo "lang: es"
    echo "book:"
    echo "  title: \"${TITULOS[$dir]:-$dir}\""
    echo "  subtitle: \"DWES · Módulo 0613 · 2º DAW\""
    echo "  author: \"Manel Navarro Pérez\""
    echo "  date: today"
    echo "  output-file: \"dwes-$dir\""
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
    number-sections: true
    colorlinks: true
    linkcolor: MidnightCoral
    urlcolor: MidnightCoral
    highlight-style: tango
    code-block-bg: "#EFF3FB"
    include-in-header: theme/pdf-header.tex
FMT
  } > "$tmp/_quarto.yml"

  (cd "$tmp" && quarto render --to pdf)
  cp "$tmp/_book/dwes-$dir.pdf" "$OUT/"
  rm -rf "$tmp"
done

echo "PDFs por unidad generados en $OUT:"
ls -1 "$OUT" || true
