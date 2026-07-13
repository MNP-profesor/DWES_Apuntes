#!/usr/bin/env python3
"""
arregla_titulos_ejercicios.py — REMIENDO (ejecutar una vez y borrar si quieres).

Arregla los ejercicios que tras la migración quedaron con el título
como encabezado huérfano dentro del bloque:

    ::: {.ejercicio}          ::: {.ejercicio}
    **EJ6**                   **Catálogo con cálculo de inventario**
                        -->
    ### E2.6 — Catálogo...    Crea catalogo.php...
    Crea catalogo.php...

Es decir: elimina la línea **EJn** suelta (si existe), convierte el
encabezado ###/#### en la línea de título en negrita (quitando el
prefijo antiguo "E2.6 —" si lo lleva) y deja que renumera_ejercicios.py
ponga el número en el siguiente render.

Solo actúa DENTRO de bloques {.ejercicio}; los encabezados del resto
del documento no se tocan.

Uso:  python scripts/arregla_titulos_ejercicios.py [--dry-run]
"""

import re
import sys
from pathlib import Path

DRY = "--dry-run" in sys.argv
ROOT = Path(__file__).resolve().parents[1]

RE_OPEN = re.compile(r"^:{3,}\s*\{[^}]*\.ejercicio[^}]*\}\s*$")
RE_EJ_SUELTO = re.compile(r"^\s*\*\*EJ\d+\*\*\s*$")
RE_HEADING = re.compile(
    r"^#{2,5}\s+(?:E\d+\.\d+\s*[·—–-]\s*)?(?P<titulo>.+?)\s*(?:\{[^}]*\})?\s*$"
)


def arregla_fichero(qmd: Path) -> int:
    lineas = qmd.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    arreglados = 0
    i = 0
    while i < len(lineas):
        linea = lineas[i]
        out.append(linea)
        if RE_OPEN.match(linea):
            # mirar las primeras líneas de contenido del bloque
            j = i + 1
            while j < len(lineas) and lineas[j].strip() == "":
                j += 1
            k = j
            if k < len(lineas) and RE_EJ_SUELTO.match(lineas[k]):
                k += 1
                while k < len(lineas) and lineas[k].strip() == "":
                    k += 1
            if k < len(lineas):
                m = RE_HEADING.match(lineas[k])
                if m and lineas[k].lstrip().startswith("#"):
                    out.append(f"**{m.group('titulo').strip()}**")
                    # añadir línea en blanco solo si no la hay ya a continuación
                    if k + 1 < len(lineas) and lineas[k + 1].strip() != "":
                        out.append("")
                    arreglados += 1
                    i = k  # saltar EJn suelto, blancos y encabezado
        i += 1
    if arreglados and not DRY:
        qmd.write_text("\n".join(out) + "\n", encoding="utf-8")
    return arreglados


def main() -> None:
    total = 0
    for ud in sorted(ROOT.glob("UD[1-9]")):
        if not ud.is_dir():
            continue
        for qmd in sorted(ud.glob("*.qmd")):
            n = arregla_fichero(qmd)
            if n:
                print(f"  {qmd.relative_to(ROOT)}: {n} título(s) fusionado(s)")
            total += n
    modo = " (dry-run, sin escribir)" if DRY else ""
    print(f"Arreglo completado: {total} ejercicios{modo}.")
    if total and not DRY:
        print("Ahora ejecuta el renumerador (o simplemente 'quarto preview'):")
        print("  python scripts/renumera_ejercicios.py")


if __name__ == "__main__":
    main()
