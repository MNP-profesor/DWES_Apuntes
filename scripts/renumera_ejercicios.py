#!/usr/bin/env python3
"""
renumera_ejercicios.py — RENUMERADOR automático de ejercicios.

Recorre las carpetas UD1..UD9 en orden y, dentro de cada una, sus
ficheros .qmd por orden de nombre. Cada bloque

    ::: {.ejercicio}
    **Título del ejercicio**

recibe (o actualiza) el prefijo secuencial de su unidad:

    ::: {.ejercicio}
    **EJ3 · Título del ejercicio**

La numeración se reinicia en cada UD. Si insertas un ejercicio en medio,
la siguiente ejecución renumera todos los posteriores. Es idempotente:
ejecutarlo sobre ficheros ya numerados no produce cambios.

Si un bloque .ejercicio no empieza con una línea en negrita, se le
inserta una línea "**EJn**" para que el número siempre sea visible.

Pensado como pre-render de Quarto (se ejecuta solo antes de cada render):
    project:
      pre-render: python scripts/renumera_ejercicios.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RE_OPEN = re.compile(r"^:{3,}\s*\{[^}]*\.ejercicio[^}]*\}\s*$")
# línea de título en negrita; captura y descarta un prefijo previo EJn ·
# o EX.n — (formatos antiguos) para no duplicarlo
RE_TITULO = re.compile(
    r"^(?P<pre>\s*)\*\*"
    r"(?:(?:EJ\d+|E\d+\.\d+)\s*[·—–-]\s*)?"
    r"(?P<titulo>.*?)"
    r"\*\*(?P<post>.*)$"
)


def renumera_unidad(ud: Path) -> tuple[int, int]:
    n = 0
    tocados = 0
    for qmd in sorted(ud.glob("*.qmd")):
        lineas = qmd.read_text(encoding="utf-8").splitlines()
        out: list[str] = []
        cambiado = False
        i = 0
        while i < len(lineas):
            linea = lineas[i]
            out.append(linea)
            if RE_OPEN.match(linea):
                n += 1
                # saltar líneas en blanco hasta el primer contenido
                j = i + 1
                while j < len(lineas) and lineas[j].strip() == "":
                    out.append(lineas[j])
                    j += 1
                if j < len(lineas):
                    m = RE_TITULO.match(lineas[j])
                    if m:
                        titulo = m.group("titulo").strip()
                        # un título que es solo "EJn" proviene de una
                        # inserción previa del propio script: tratarlo
                        # como vacío para mantener la idempotencia
                        if re.fullmatch(r"EJ\d+", titulo):
                            titulo = ""
                        if titulo:
                            nueva = f"{m.group('pre')}**EJ{n} · {titulo}**{m.group('post')}"
                        else:
                            nueva = f"{m.group('pre')}**EJ{n}**{m.group('post')}"
                        if nueva != lineas[j]:
                            cambiado = True
                        out.append(nueva)
                    else:
                        # bloque sin título en negrita: insertar el número
                        out.append(f"**EJ{n}**")
                        out.append("")
                        out.append(lineas[j])
                        cambiado = True
                    i = j
            i += 1
        if cambiado:
            qmd.write_text("\n".join(out) + "\n", encoding="utf-8")
            tocados += 1
    return n, tocados


def main() -> None:
    total = 0
    for ud in sorted(ROOT.glob("UD[1-9]")):
        if not ud.is_dir():
            continue
        n, tocados = renumera_unidad(ud)
        total += n
        if n:
            extra = f" ({tocados} fichero(s) actualizados)" if tocados else " (sin cambios)"
            print(f"  {ud.name}: {n} ejercicios{extra}")
    print(f"Renumeración completada: {total} ejercicios en total.")


if __name__ == "__main__":
    main()
