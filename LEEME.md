# ARC Automatizaciones · el sitio público

La web comercial de ARC. Vive **fuera** del repositorio de la aplicación a
propósito: ahí dentro están las reglas de construcción de BANAT, las tarifas
con precios y las plantillas de la Biesse, y ese repositorio tiene que seguir
siendo privado. Este es público, y no contiene nada de ninguna fábrica.

## Qué hay

    index.html          la portada
    precios.html        el precio, con la calculadora de cuota
    condiciones.html    condiciones de contratación   ← las que mira Stripe
    privacidad.html     RGPD
    aviso-legal.html    LSSI art. 10
    cookies.html        no hay cookies, y se dice
    css/arc.css         la hoja de estilo
    js/arc.js           el plano animado y la calculadora
    js/fondo.js         el papel de la portada, detrás de todo
    marca/              logotipos y favicons
    herramientas/       de aquí salen las seis páginas

## No se edita el HTML a mano

Las seis páginas se generan. La cabecera, la barra y el cajetín del pie son
los mismos en todas, y una cabecera copiada seis veces acaba siendo seis
cabeceras distintas.

    python3 herramientas/generar.py

- **`herramientas/generar.py`** — el molde y **los datos de la empresa**.
- **`herramientas/paginas.py`** — el texto de cada página.

### Los datos fiscales

Están todos en el bloque `EMPRESA` de `generar.py`, y tienen tres estados:

| valor | qué hace |
|---|---|
| `"algo"` | se publica |
| `""` | se ha decidido **no** publicarlo: no sale, y no deja hueco |
| `None` | falta y **sale marcado en rojo** en la web |

Ahora mismo el **CIF**, el **domicilio** y los **datos registrales** están en
`""`. Ponles su valor y ejecuta el generador: aparecen solos en el pie, en el
aviso legal, en las condiciones y en la política de privacidad.

> Para una S.L., el artículo 10 de la LSSI pide el NIF y el domicilio social en
> la web, y es lo primero que mira Stripe al revisar una cuenta. Mientras estén
> vacíos, el aviso legal dice que se facilitan a quien los pida.

## El fondo de la portada

`js/fondo.js` dibuja el papel que va DETRÁS del titular y del plano. El plano
—el alzado que se acota y se despieza— es de `js/arc.js` y no se toca: son dos
cosas distintas y por eso están en dos ficheros distintos.

Hay cinco dibujos y se cambian sin desplegar, poniéndolo en la dirección:

    ?fondo=0  ninguno      ?fondo=3  cotas
    ?fondo=1  escuadra     ?fondo=4  mecanizado   (puesto: 1, al 150 %)
    ?fondo=2  lápiz        ?fondo=5  mapa de corte

Y `&fuerza=80` para bajarlo o `&fuerza=200` para subirlo. Cuando uno convenza,
se pone en `ELEGIDO` y `FUERZA`, arriba del fichero.

Cuidado con la fuerza: **depende del dibujo**. La escuadra son dos líneas
finas y aguanta el 150 %; el lápiz, que cruza la hoja con trazo negro, al 150 %
se pelea con el texto. Si cambias de dibujo, vuelve a mirar el número.

## El precio está en dos sitios y tiene que cuadrar

`js/arc.js` empieza con:

```js
const PLAN = { base: 349.99, incluidos: 5, porUsuario: 60, pesoTaller: 0.5, iva: 0.21 };
```

Son los mismos números de la tabla `planes` de la aplicación
(`supabase/suscripciones.sql`). **Si cambian allí, cambian aquí**, o esta
página le dice a un cliente un precio que luego no es el suyo.

## Desplegar

Vercel publica solo con cada `git push` a `main`. No hay compilación: son
ficheros estáticos y se sirven tal cual.
