#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARC · genera las páginas del sitio
-----------------------------------------------------------------
El sitio son ficheros HTML sueltos: Vercel los sirve tal cual y no
hay ningún paso de compilación que pueda fallar un viernes. Lo que
sí se repite en las seis páginas es la cabecera, la barra y el
cajetín del pie, y una cabecera copiada seis veces acaba siendo
seis cabeceras distintas.

Esto las escribe. Se toca aquí y se ejecuta:

    python3 herramientas/generar.py

Los datos fiscales están TODOS en el bloque EMPRESA de abajo. Se
rellenan una vez y salen en las seis páginas a la vez. Lo que
todavía no se sabe se deja en None y sale marcado en rojo en la
página: un aviso legal con «Calle Ejemplo 1» es peor que uno con
un hueco, porque el hueco se arregla y la mentira se queda.
"""
import os, re, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ======================= LOS DATOS DE LA EMPRESA =======================
# Tres estados, y la diferencia importa:
#   un valor   -> sale publicado
#   ""         -> se ha decidido NO publicarlo: no sale, y no sale ningún hueco
#   None       -> falta y todavía no se ha decidido: sale marcado en rojo en la
#                 web, para que no se olvide. Un aviso legal con «Calle Ejemplo 1»
#                 es peor que uno con un hueco: el hueco se arregla, la mentira se
#                 queda.
#
# ARC lo lleva un AUTÓNOMO, no una sociedad. Eso cambia tres cosas y no es
# una formalidad:
#   · el titular es una persona con nombre y apellidos, no una marca;
#   · el número es un NIF de persona física (8 cifras y letra), no un CIF
#     de sociedad (que empieza por letra);
#   · no hay datos registrales, porque un autónomo no se inscribe en el
#     Registro Mercantil. Por eso `registro` va vacío y no marcado: no es
#     que falte, es que no existe.
# «ARC Automatizaciones» es el nombre comercial, y es lo que ve el cliente
# en todas partes menos en el aviso legal y en el contrato.
EMPRESA = {
    "marca":        "ARC Automatizaciones",   # nombre comercial
    "razon":        "Hamza Arcoub Bourht",
    "cif":          "61014038Y",
    "etiqueta_nif": "NIF",    # «NIF» si es persona, «CIF» si es sociedad
    "domicilio":    "C/ José Miguel Iturrioz, 11 · 20200 Beasain (Gipuzkoa)",
    "email":        "arc.automatizaciones@gmail.com",
    "telefono":     "631 248 441",
    "registro":     "",       # no aplica: un autónomo no se inscribe
    "descriptor":   "ARC_automatizaciones",   # lo que ve el cliente en su extracto
    "web":          "arcautomatizaciones.vercel.app",
}
ACTUALIZADO = "2 de septiembre de 2026"

# ======================= EL PLAN =======================
# Los mismos números que factura la aplicación (tabla `planes`).
PLAN = {"base": "349,99 €", "incluidos": 5, "usuario": "60 €",
        "iva": "21 %", "total": "423,49 €", "prueba": 3,
        "permanencia": 12, "integracion": "3.500 €"}


def dato(clave, que=None):
    """El dato, o un hueco que se ve. Lo que se ha decidido no publicar
       devuelve cadena vacía y no deja rastro."""
    v = EMPRESA.get(clave)
    if v:
        return v
    if v == "":
        return ""
    return f'<span class="falta">falta: {que or clave}</span>'


def campo(etiqueta, clave, que=None):
    """Una fila de la ficha legal. Si el dato no se publica, la fila no
       existe: una etiqueta con el hueco al lado es peor que no ponerla."""
    v = dato(clave, que)
    if not v:
        return ""
    return f'<div><b>{etiqueta}</b><span>{v}</span></div>'


def enlace(clave):
    v = EMPRESA.get(clave)
    if not v:
        return dato(clave)
    if clave == "email":
        return f'<a href="mailto:{v}">{v}</a>'
    if clave == "telefono":
        return f'<a href="tel:+34{v.replace(" ", "")}">{v}</a>'
    return v


CABEZA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" sizes="32x32" href="/marca/favicon-32.png">
<link rel="apple-touch-icon" href="/marca/arc-icono-180.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ARC Automatizaciones">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="/marca/arc-lockup.png">
<meta name="theme-color" content="#E00F16">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/css/arc.css">
</head>
<body>

<header class="barra">
  <div class="hoja">
    <a href="/" aria-label="ARC Automatizaciones, inicio">
      <img class="claro" src="/marca/arc-lockup.png" alt="ARC Automatizaciones" width="1400" height="237">
      <img class="oscuro" src="/marca/arc-lockup-neg.png" alt="" width="1400" height="237" aria-hidden="true">
    </a>
    <nav>
      <a href="/#que-hace" class="oculta-movil">Qué hace</a>
      <a href="/#como" class="oculta-movil">Cómo funciona</a>
      <a href="/precios">Precio</a>
      <a href="/#contacto">Contacto</a>
    </nav>
  </div>
</header>
"""

PIE = """
<footer class="pie">
  <div class="hoja">
    <div class="cajetin">
      <div class="celda">
        <h4>Quién responde</h4>
        <p>{razon}{cif}</p>
      </div>
      <div class="celda">
        <h4>Contacto</h4>
        <p>{email}<br>{telefono}</p>
      </div>
      <div class="celda">
        <h4>El producto</h4>
        <a href="/#que-hace">Qué hace</a>
        <a href="/#como">Cómo funciona</a>
        <a href="/precios">Precio</a>
      </div>
      <div class="celda">
        <h4>Condiciones</h4>
        <a href="/condiciones">Condiciones de contratación</a>
        <a href="/privacidad">Privacidad</a>
        <a href="/aviso-legal">Aviso legal</a>
        <a href="/cookies">Cookies</a>
      </div>
    </div>
    <div class="pie-abajo">
      <span>© <span data-anio>2026</span> {marca} · Software para fábricas de mueble a medida</span>
      <span style="margin-left:auto">Precios sin IVA salvo donde se indique</span>
    </div>
  </div>
</footer>

<script src="/js/arc.js"></script>
</body>
</html>
"""


def pagina(nombre, titulo, desc, cuerpo):
    html = CABEZA.format(titulo=titulo, desc=desc) + cuerpo + PIE.format(
        razon=dato("razon", "nombre y apellidos del titular"),
        cif=(f'<br>{dato("cif")}' if dato("cif") else ""),
        email=enlace("email"),
        telefono=enlace("telefono"),
        marca=EMPRESA["marca"],
    )
    ruta = os.path.join(RAIZ, nombre)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    return ruta


if __name__ == "__main__":
    import paginas          # el contenido, para no mezclarlo con el molde
    hechas = paginas.todas(pagina, dato, campo, enlace, PLAN, EMPRESA, ACTUALIZADO)
    for h in hechas:
        print("·", os.path.relpath(h, RAIZ))
    faltan = [k for k, v in EMPRESA.items() if v is None]
    if faltan:
        print("\n  PENDIENTE, y sale marcado en la web:", ", ".join(faltan))
