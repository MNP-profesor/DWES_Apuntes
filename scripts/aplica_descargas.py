#!/usr/bin/env python3
"""
aplica_descargas.py — INTERRUPTOR de la página de Descargas.

Antes de cada render, reconstruye descargas.qmd a partir de:
  - theme/descargas-activas.md    (tabla completa, con sus condicionales
                                    de formato ya resueltos)
  - theme/descargas-inactivas.md  (mensaje de "no disponibles todavía")

según el valor de la clave de proyecto `descargas-activas` en `_quarto.yml`:

    descargas-activas: true    # muestra las tablas y enlaces
    descargas-activas: false   # muestra el mensaje de sustitución

Es tu único punto de cambio: edita ese `true`/`false` y listo. No hace
falta tocar descargas.qmd a mano — de hecho, este script lo reescribe
en cada render, así que cualquier edición manual de descargas.qmd se
perdería. Para cambiar el contenido, edita los dos ficheros de theme/.

Pensado como pre-render de Quarto:
    project:
      pre-render:
        - python scripts/renumera_ejercicios.py
        - python scripts/aplica_descargas.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
YML = ROOT / "_quarto.yml"
DESTINO = ROOT / "descargas.qmd"
ACTIVAS = ROOT / "theme" / "descargas-activas.md"
INACTIVAS = ROOT / "theme" / "descargas-inactivas.md"

TITULO = "# Descargas {.unnumbered}"

RE_FLAG = re.compile(r"^descargas-activas:\s*(true|false)\s*$", re.MULTILINE)


def lee_flag() -> bool:
    texto = YML.read_text(encoding="utf-8")
    m = RE_FLAG.search(texto)
    if not m:
        print(
            "AVISO: no se encontró 'descargas-activas: true|false' en "
            "_quarto.yml; se asume true (descargas activas)."
        )
        return True
    return m.group(1) == "true"


def main() -> None:
    activas = lee_flag()
    fuente = ACTIVAS if activas else INACTIVAS
    if not fuente.exists():
        print(f"ERROR: falta {fuente.relative_to(ROOT)}", file=sys.stderr)
        sys.exit(1)

    cuerpo = fuente.read_text(encoding="utf-8").strip()
    contenido = f"{TITULO}\n\n{cuerpo}\n"

    if not DESTINO.exists() or DESTINO.read_text(encoding="utf-8") != contenido:
        DESTINO.write_text(contenido, encoding="utf-8")
        print(f"descargas.qmd regenerado ({'activas' if activas else 'inactivas'}).")
    else:
        print(f"descargas.qmd sin cambios ({'activas' if activas else 'inactivas'}).")


if __name__ == "__main__":
    main()
