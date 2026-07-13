#!/usr/bin/env python3
"""
migra_ejercicios.py — MIGRACIÓN (ejecutar UNA sola vez).

Convierte el marcado antiguo de ejercicios al convenio nuevo:

  1. Elimina encabezados del tipo:   ## Ejercicio E1.2 {#exr-UD1-2}
  2. Convierte aperturas de div:     ::: {#exr-UD1-2}            -> ::: {.ejercicio}
                                     ::: {#exr-UD2-3 name="..."} -> ::: {.ejercicio}
                                                                     **...**
     (si el div tenía name="...", ese texto pasa a ser la primera
      línea en negrita del bloque, para no perder el título)

No numera nada: de eso se encarga renumera_ejercicios.py.
Uso:  python scripts/migra_ejercicios.py            (desde la raíz del repo)
      python scripts/migra_ejercicios.py --dry-run  (solo muestra, no escribe)
"""

import re
import sys
from pathlib import Path

DRY = "--dry-run" in sys.argv
ROOT = Path(__file__).resolve().parents[1]

RE_HEADING = re.compile(r"^#{2,4}\s+Ejercicio\b[^\n]*\{#exr-[^}]*\}\s*$")
RE_DIV = re.compile(r"^(?P<colons>:{3,})\s*\{(?P<attrs>[^}]*#exr-[^}]*)\}\s*$")
RE_NAME = re.compile(r'name\s*=\s*"(?P<name>[^"]*)"')


def migra_fichero(qmd: Path) -> tuple[int, int]:
    lineas = qmd.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    headings, divs = 0, 0
    for linea in lineas:
        if RE_HEADING.match(linea):
            headings += 1
            # descarta el encabezado y evita dejar doble línea en blanco
            if out and out[-1].strip() == "":
                out.pop()
            continue
        m = RE_DIV.match(linea)
        if m:
            divs += 1
            out.append(f"{m.group('colons')} {{.ejercicio}}")
            mn = RE_NAME.search(m.group("attrs"))
            if mn:
                out.append(f"**{mn.group('name').strip()}**")
                out.append("")
            continue
        out.append(linea)
    if (headings or divs) and not DRY:
        qmd.write_text("\n".join(out) + "\n", encoding="utf-8")
    return headings, divs


def main() -> None:
    total_h = total_d = 0
    for ud in sorted(ROOT.glob("UD[1-9]")):
        if not ud.is_dir():
            continue
        for qmd in sorted(ud.glob("*.qmd")):
            h, d = migra_fichero(qmd)
            if h or d:
                print(f"  {qmd.relative_to(ROOT)}: {d} div(s) convertidos, {h} encabezado(s) eliminados")
            total_h += h
            total_d += d
    modo = "(dry-run, sin escribir)" if DRY else ""
    print(f"Migración: {total_d} ejercicios convertidos, {total_h} encabezados eliminados {modo}")
    # Aviso de referencias cruzadas que quedarían rotas
    rotas = []
    for ud in sorted(ROOT.glob("UD[1-9]")):
        for qmd in sorted(ud.glob("*.qmd")):
            for i, linea in enumerate(qmd.read_text(encoding="utf-8").splitlines(), 1):
                if "@exr-" in linea:
                    rotas.append(f"  {qmd.relative_to(ROOT)}:{i}")
    if rotas:
        print("AVISO: referencias @exr- que debes convertir a enlaces normales a mano:")
        print("\n".join(rotas))


if __name__ == "__main__":
    main()
