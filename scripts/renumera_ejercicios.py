#!/usr/bin/env python3
"""
renumera_ejercicios.py — RENUMERADOR automático de ejercicios + índice.

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

Además genera INDICE_EJERCICIOS.md en la raíz del repo: una tabla por
unidad con número, título y fichero de cada ejercicio. Útil como mapa
del módulo y para cotejar con las soluciones del repo privado. El
fichero solo se reescribe si su contenido cambia.

Pensado como pre-render de Quarto (se ejecuta solo antes de cada render):
    project:
      pre-render: python scripts/renumera_ejercicios.py
"""

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDICE = ROOT / "INDICE_EJERCICIOS.md"

RE_OPEN = re.compile(r"^:{3,}\s*\{[^}]*\.ejercicio[^}]*\}\s*$")
# línea de título en negrita; captura y descarta un prefijo previo EJn ·
# o EX.n — (formatos antiguos) para no duplicarlo
RE_TITULO = re.compile(
    r"^(?P<pre>\s*)\*\*"
    r"(?:(?:EJ\d+|E\d+\.\d+)\s*[·—–-]\s*)?"
    r"(?P<titulo>.*?)"
    r"\*\*(?P<post>.*)$"
)

RE_YAML_TITLE = re.compile(r'^title:\s*(?:"(?P<d>[^"]*)"|\'(?P<s>[^\']*)\'|(?P<n>.+?))\s*$')


def titulo_unidad(ud: Path) -> str:
    """Lee el título de la UD del frontmatter YAML de su fichero de
    presentación (00-presentacion.qmd o 01-presentacion.qmd). Si no lo
    encuentra, devuelve el nombre de la carpeta (UD1, UD2, ...)."""
    candidatos = sorted(ud.glob("*presentacion*.qmd")) or sorted(ud.glob("*.qmd"))
    for qmd in candidatos:
        lineas = qmd.read_text(encoding="utf-8").splitlines()
        if not lineas or lineas[0].strip() != "---":
            continue
        for linea in lineas[1:40]:
            if linea.strip() == "---":
                break
            m = RE_YAML_TITLE.match(linea.strip())
            if m:
                return (m.group("d") or m.group("s") or m.group("n") or "").strip()
    return ud.name


def renumera_unidad(ud: Path) -> tuple[int, int, list[tuple[int, str, str]]]:
    """Renumera una unidad. Devuelve (nº ejercicios, ficheros tocados,
    registros [(n, título, fichero), ...] para el índice)."""
    n = 0
    tocados = 0
    registros: list[tuple[int, str, str]] = []
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
                        registros.append((n, titulo or "*(sin título)*", qmd.name))
                    else:
                        # bloque sin título en negrita: insertar el número
                        out.append(f"**EJ{n}**")
                        out.append("")
                        out.append(lineas[j])
                        cambiado = True
                        registros.append((n, "*(sin título)*", qmd.name))
                    i = j
            i += 1
        if cambiado:
            qmd.write_text("\n".join(out) + "\n", encoding="utf-8")
            tocados += 1
    return n, tocados, registros


def escribe_indice(datos: dict[str, tuple[str, list[tuple[int, str, str]]]]) -> bool:
    """Genera INDICE_EJERCICIOS.md. Devuelve True si lo ha reescrito."""
    lineas = [
        "# Índice de ejercicios del módulo DWES",
        "",
        "> Generado automáticamente por `scripts/renumera_ejercicios.py` "
        "en cada render — **no editar a mano**.",
        f">",
        f"> Última actualización: {date.today().isoformat()}",
        "",
    ]
    total = 0
    for ud, (titulo_ud, registros) in datos.items():
        if not registros:
            continue
        total += len(registros)
        lineas.append(f"## {titulo_ud} ({len(registros)} ejercicios)")
        lineas.append("")
        lineas.append("| Nº | Título | Fichero |")
        lineas.append("|:--:|--------|---------|")
        for n, titulo, fichero in registros:
            lineas.append(f"| EJ{n} | {titulo} | `{fichero}` |")
        lineas.append("")
    lineas.append(f"**Nº Ejercicios totales del módulo: {total}**")
    lineas.append("")
    contenido = "\n".join(lineas)

    # comparar ignorando la línea de fecha, para no reescribir (ni
    # disparar el watcher de quarto preview) cuando nada ha cambiado
    def sin_fecha(texto: str) -> str:
        return re.sub(r"> Última actualización: \d{4}-\d{2}-\d{2}", "", texto)

    if INDICE.exists() and sin_fecha(INDICE.read_text(encoding="utf-8")) == sin_fecha(contenido):
        return False
    INDICE.write_text(contenido, encoding="utf-8")
    return True


def main() -> None:
    total = 0
    datos: dict[str, tuple[str, list[tuple[int, str, str]]]] = {}
    for ud in sorted(ROOT.glob("UD[1-9]")):
        if not ud.is_dir():
            continue
        n, tocados, registros = renumera_unidad(ud)
        datos[ud.name] = (titulo_unidad(ud), registros)
        total += n
        if n:
            extra = f" ({tocados} fichero(s) actualizados)" if tocados else " (sin cambios)"
            print(f"  {ud.name}: {n} ejercicios{extra}")
    print(f"Renumeración completada: {total} ejercicios en total.")
    if escribe_indice(datos):
        print(f"Índice actualizado: {INDICE.name}")


if __name__ == "__main__":
    main()
