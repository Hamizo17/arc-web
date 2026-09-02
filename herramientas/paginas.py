# -*- coding: utf-8 -*-
"""
ARC · el contenido de las páginas
-----------------------------------------------------------------
Aquí está lo que dice el sitio. El molde —cabecera, barra, pie— vive
en generar.py. Separados a propósito: el texto se toca a menudo y el
molde casi nunca, y mezclarlos hace que tocar una coma obligue a
mirar el HTML entero.
"""


def todas(pagina, dato, campo, enlace, PLAN, EMPRESA, ACTUALIZADO):
    hechas = []
    correo = EMPRESA.get("email")
    tel = EMPRESA.get("telefono", "")
    mailto = ('<a class="btn" href="mailto:' + correo + '?subject=Demo%20de%20ARC">'
              'Escríbeme <small>' + correo + '</small></a>'
              '<a class="btn btn--linea" href="tel:+34' + tel.replace(" ", "") + '">'
              'Llámame <small>' + tel + '</small></a>') if correo else \
             ('<span class="falta">falta: email de contacto</span>')

    # ==================================================================
    # PORTADA
    # ==================================================================
    hechas.append(pagina("index.html",
        "ARC Automatizaciones",
        "Software para fábricas de cocinas y armarios a medida: del dibujo salen el "
        "despiece, los planos de taller, el programa de máquina, el mapa de corte, el "
        "coste y el presupuesto, con los gruesos y las holguras de tu casa.",
        """
<main>

<!-- El fondo va DETRÁS de todo el bloque de portada: del titular y también
     del plano. Envuelve a `.hoja` en vez de ir dentro, porque `.hoja` está
     limitada a 1180 px y el papel tiene que llegar hasta los bordes. -->
<div class="escena">
  <canvas id="fondoPortada" aria-hidden="true"></canvas>
<section class="hoja portada">
  <div class="portada-rej">
    <div>
      <p class="eti"><b>ARC</b> · Software de fabricación a medida</p>
      <h1>Dibuja el mueble una vez.<br><em>Lo demás sale solo.</em></h1>
      <p class="entradilla">Del mismo alzado salen el despiece, los planos de taller, el
        programa de la máquina, el mapa de corte, el coste y el presupuesto. Con los
        gruesos, las holguras y los herrajes de <strong>tu</strong> fábrica, no con los
        de un catálogo.</p>
      <div class="marcas">
        <span>Cocinas</span><span>Armarios</span><span>Despiece</span>
        <span>Post-procesador Biesse</span><span>Mapa de corte</span><span>Multi-empresa</span>
      </div>
      <div class="botones">
        <a class="btn" href="/precios">Ver el precio <small>349,99 €/mes</small></a>
        <a class="btn btn--linea" href="#contacto">Pedir una demo</a>
      </div>
    </div>

    <div class="plano">
      <div class="plano-cab">
        <b>ARC-01</b><span>Alzado de cocina · 3600 × 2400 mm · escala variable</span>
      </div>
      <canvas id="plano" width="1000" height="560"
        aria-label="Alzado de una cocina de 3600 por 2400 milímetros que se acota y se despieza en las diez piezas de una columna de horno."></canvas>
      <div class="plano-pie">
        <div class="fase" id="fases"><i></i><i class="on"></i><i></i><i></i></div>
        <span id="faseNombre">Cotas</span>
        <button type="button" id="replay">Repetir</button>
      </div>
    </div>
  </div>

  <div class="cifras sube">
    <div class="cifra"><b>6</b><span>Documentos distintos del mismo dibujo, sin volver a medir nada</span></div>
    <div class="cifra"><b>19 · 10 · 0,8</b><span>Cuerpo, trasera y canto en mm. Los tuyos: se ponen una vez</span></div>
    <div class="cifra"><b>4</b><span>Vistas: dirección, oficina técnica, diseño y taller</span></div>
    <div class="cifra"><b>Mes a mes</b><span>Sin permanencia y sin penalización: se deja cuando quieras</span></div>
  </div>
</section>
</div>

<div class="hoja"><div class="cota cota--sola"><span>Lo que sale del dibujo</span></div></div>

<section class="tira tira--blanca" id="que-hace">
  <div class="hoja">
    <p class="eti"><b>01</b> · Lo que sale</p>
    <h2>Seis cosas, y todas del mismo dibujo</h2>
    <p class="entradilla">No son seis módulos que se compran por separado. Es que en cuanto
      hay muebles en la pared, ya están las piezas — y de las piezas sale todo lo demás.</p>

    <div class="salidas">
      <article class="salida sube"><span class="ref">SAL-01</span>
        <h3>Dibujar y despiezar</h3>
        <p>Colocas los muebles sobre la pared y sale la lista de piezas con su medida real:
           costados, techos, suelos, baldas, traseras y frentes. Con tus gruesos y tus
           holguras, restadas como las restas tú.</p></article>
      <article class="salida sube"><span class="ref">SAL-02</span>
        <h3>Planos y ficha de taller</h3>
        <p>Alzado acotado y la ficha que baja al taller: qué lleva cada mueble, cuántas
           bisagras, qué herraje y por dónde va cada pieza. En papel, para el que corta.</p></article>
      <article class="salida sube"><span class="ref">SAL-03</span>
        <h3>Sacar a máquina</h3>
        <p>El programa del centro de mecanizado. Canal de trasera, taladros de bisagra y de
           estante, con la herramienta, el diámetro y las compensaciones de tu
           post-procesador.</p></article>
      <article class="salida sube"><span class="ref">SAL-04</span>
        <h3>Mapa de corte</h3>
        <p>Cómo caben las piezas en tableros de 2850×2100 y cuántos hacen falta de cada
           grueso. Con el disco y la fresa con los que cortas.</p></article>
      <article class="salida sube"><span class="ref">SAL-05</span>
        <h3>Hoja de costes</h3>
        <p>Tablero, canto, herrajes, horas de taller y de montaje, mueble a mueble. Y la
           lista de lo que hay que pedirle a cada proveedor.</p></article>
      <article class="salida sube"><span class="ref">SAL-06</span>
        <h3>Presupuesto al cliente</h3>
        <p>El precio de venta con tu margen y tu transporte, listo para imprimir. Lo que
           falta por confirmar sale marcado, para que no se cierre un presupuesto a medias.</p></article>
    </div>
  </div>
</section>

<section class="tira" id="como">
  <div class="hoja">
    <p class="eti"><b>02</b> · El recorrido</p>
    <h2>De la pared al tablero cortado</h2>
    <p class="entradilla">El orden importa: cada paso usa lo que dejó el anterior, y por eso
      no hay dos versiones de la misma medida dando vueltas por la fábrica.</p>

    <div class="pasos">
      <div class="paso sube"><div class="n">01</div><div>
        <h3>Se configura tu fábrica. Una vez.</h3>
        <p>Gruesos, holguras, canal de la trasera, gola, unión, patas, herrajes, tarifa y tu
           biblioteca de muebles. Se rellena desde la pantalla, bloque a bloque, y se guarda
           entero o no se guarda: media configuración es peor que ninguna.</p>
        <span class="dato">cuerpo 19 · trasera 10 · canto 0,8 · holgura de frente 3</span>
      </div></div>

      <div class="paso sube"><div class="n">02</div><div>
        <h3>Se dibuja la obra</h3>
        <p>Arrastras muebles de tu biblioteca sobre la pared, con sus medidas y sus alturas.
           La aplicación cuadra, avisa de lo que se solapa y de lo que no encaja en el hueco.</p>
      </div></div>

      <div class="paso sube"><div class="n">03</div><div>
        <h3>El despiece ya está</h3>
        <p>No hay un botón de «generar». En cuanto hay un mueble hay piezas, y en cuanto hay
           piezas hay plano, canto y mapa de corte. Cambias un mueble y cambia todo con él.</p>
        <span class="dato">M03 · Columna horno · 10 piezas · 28,0 ml de canto</span>
      </div></div>

      <div class="paso sube"><div class="n">04</div><div>
        <h3>Baja al taller y a la máquina</h3>
        <p>La obra pasa a la cola del taller con su estado. El taller no dibuja: abre su
           orden, saca los papeles y el programa, y marca lo que va quedando hecho. Lo que
           está en la sierra no se le mueve por debajo.</p>
      </div></div>

      <div class="paso sube"><div class="n">05</div><div>
        <h3>Se cierra el precio</h3>
        <p>Coste y presupuesto salen de los mismos números que el despiece. No hay una hoja
           de cálculo aparte que alguien tiene que acordarse de actualizar.</p>
      </div></div>
    </div>
  </div>
</section>

<section class="tira tira--blanca">
  <div class="hoja">
    <p class="eti"><b>03</b> · Por qué no vale un programa genérico</p>
    <h2>Tu fábrica no monta como la de al lado</h2>
    <p class="entradilla">Dos talleres de la misma calle hacen el mismo armario con medidas
      distintas, y los dos lo hacen bien. Un programa que trae «un» sistema constructivo
      obliga a corregir a mano el despiece de cada obra — y entonces vuelve el papel.</p>

    <div class="envuelve">
    <table class="tabla">
      <thead><tr><th>Lo que cambia de una fábrica a otra</th><th>En ARC</th></tr></thead>
      <tbody>
        <tr><td>Grueso del cuerpo, de la trasera y del frente</td><td>tuyo</td></tr>
        <tr><td>Holgura entre frentes y descuento de puerta</td><td>tuyo</td></tr>
        <tr><td>Trasera encastrada o vista, y a qué distancia va el canal</td><td>tuyo</td></tr>
        <tr><td>Gola, uñero, altura de altos, alto de columna, patas</td><td>tuyo</td></tr>
        <tr><td>Unión del cuerpo y herraje de cada tipo de mueble</td><td>tuyo</td></tr>
        <tr><td>Herramienta, diámetro y compensación de la máquina</td><td>tuyo</td></tr>
        <tr><td>Tarifa de tablero, canto, herrajes y horas</td><td>tuya</td></tr>
      </tbody>
    </table>
    </div>
    <p class="nota">Todo eso vive en un solo sitio, el perfil de fábrica, y es lo que hace
      que el despiece salga bien a la primera. Configurarlo es la puesta en marcha, y va
      aparte de la cuota.</p>
  </div>
</section>

<section class="tira">
  <div class="hoja">
    <p class="eti"><b>04</b> · Quién ve qué</p>
    <h2>Cada uno entra a lo suyo</h2>
    <p class="entradilla">No es desconfianza: es que a quien está cortando no le sirve el
      lienzo de diseño, y una pantalla llena de botones que no puede pulsar es una pantalla
      peor.</p>

    <div class="envuelve">
    <table class="tabla">
      <thead><tr><th>Rol</th><th>Qué tiene delante</th></tr></thead>
      <tbody>
        <tr><td><strong>Dirección</strong></td><td>Todo, y el perfil de fábrica: cómo monta la casa, la tarifa y los usuarios</td></tr>
        <tr><td><strong>Oficina técnica</strong></td><td>La aplicación entera. El perfil de fábrica no lo toca</td></tr>
        <tr><td><strong>Diseño</strong></td><td>Dibuja y presupuesta. No lanza a fabricar</td></tr>
        <tr><td><strong>Taller</strong></td><td>Su cola de órdenes: papeles, programa y marcar lo hecho</td></tr>
      </tbody>
    </table>
    </div>
    <p class="nota">Cada empresa ve sus obras y solo las suyas. No es una opción de pantalla:
      la base de datos no le devuelve a nadie una fila de otra fábrica.</p>
  </div>
</section>

<section class="tira tira--blanca" id="precio">
  <div class="hoja">
    <p class="eti"><b>05</b> · Lo que cuesta</p>
    <h2>Un precio, y está escrito</h2>
    <div class="tarifa">
      <div class="panel">
        <div class="panel-cab">
          <p class="eti">Cuota mensual</p>
          <div class="granprecio"><b>349,99 €</b><span>al mes + IVA · 423,49 € con IVA</span></div>
        </div>
        <div class="panel-cue">
          <ul class="incluye">
            <li>Mantenimiento y actualizaciones incluidos</li>
            <li><strong>Cinco usuarios</strong> incluidos <em>— el de taller cuenta medio</em></li>
            <li>60 € al mes por cada usuario a partir del sexto</li>
            <li>Tus obras, tu perfil y tus catálogos, en la nube</li>
            <li><strong>Sin permanencia.</strong> <em>Se paga mes a mes y se deja cuando quieras</em></li>
          </ul>
          <div class="botones">
            <a class="btn" href="/precios">Ver el precio entero</a>
          </div>
        </div>
      </div>
      <div>
        <h3>Y la puesta en marcha, aparte</h3>
        <p class="nota" style="margin-top:12px;font-size:15.5px">Configurar tu fábrica no es
          rellenar un formulario: es medir cómo montas, cargar tu biblioteca de muebles, tu
          tarifa y las plantillas de tu máquina, y comprobar el despiece contra muebles que
          ya has hecho. Se cobra una vez, <strong>desde 2.500 €</strong>, y depende de
          cuántos sistemas constructivos y cuántas máquinas haya que meter.</p>
        <p class="nota" style="font-size:15.5px">Y no hay permanencia. Se paga mes a mes; si
          un día deja de encajarte, avisas y se acaba al terminar el mes que estás pagando.
          Sin penalización y sin tener que dar explicaciones.</p>
      </div>
    </div>
  </div>
</section>

<section class="tira">
  <div class="hoja">
    <p class="eti"><b>06</b> · Preguntas</p>
    <h2>Lo que preguntan siempre</h2>
    <div class="faq">
      <details open><summary>Mi fábrica monta distinto. ¿Sirve igual?</summary>
        <p>Es justo para lo que está hecho. Los gruesos, las holguras, el canal, la gola, la
           unión y los herrajes se configuran por empresa. Si tu manera de montar no cabe en
           lo que hay, se añade: eso es parte de la puesta en marcha.</p></details>
      <details><summary>¿Qué máquina hace falta?</summary>
        <p>Para dibujar, despiezar, sacar planos y presupuestar, ninguna: un navegador. Para
           sacar el programa hace falta que tu centro de mecanizado tenga su post-procesador
           configurado — ahora mismo está hecho para Biesse con plantillas PGMX, y otras se
           añaden en la puesta en marcha.</p></details>
      <details><summary>¿Mis medidas y mis precios se mezclan con los de otra fábrica?</summary>
        <p>No. Cada empresa tiene su espacio y la base de datos no devuelve filas de otra,
           aunque alguien lo intente por fuera de la pantalla. Tu tarifa y tus catálogos
           están detrás de tu sesión, no en una carpeta pública.</p></details>
      <details><summary>¿Y si un mes no pago?</summary>
        <p>No se te encierra con tus datos dentro. Tus obras siguen ahí: se abren, se
           imprimen y se exportan, y el taller puede seguir marcando lo que ya está
           cortando. Lo que se para hasta regularizar es crear obras nuevas y cambiar las que
           hay. Y antes de eso hay un aviso: un recibo pendiente no corta nada de golpe.</p></details>
      <details><summary>¿Cuánto se tarda en tenerlo funcionando?</summary>
        <p>Depende de cuántos sistemas constructivos tengas y de en qué estado esté tu
           tarifa. Lo que marca el ritmo no es el software: es cuadrar el despiece contra
           muebles que ya has fabricado, hasta que salgan iguales.</p></details>
      <details><summary>¿Hay permanencia?</summary>
        <p>No. Se paga mes a mes y se deja cuando quieras: avisas y el servicio termina al
           acabar el mes que ya has pagado. Sin penalización, sin plazo de preaviso largo y
           sin tener que justificar nada. Está escrito en las
           <a href="/condiciones">condiciones de contratación</a>, que es donde tiene que
           estar.</p></details>
    </div>
  </div>
</section>

<section class="tira tira--blanca" id="contacto">
  <div class="hoja">
    <p class="eti"><b>07</b> · Hablarlo</p>
    <h2>Enséñame un mueble tuyo y te lo despiezo</h2>
    <p class="entradilla">Es la forma más rápida de saber si esto te sirve: un mueble que ya
      hayas fabricado, con sus medidas. Si el despiece sale igual que el tuyo, hay algo de
      qué hablar. Si no sale igual, también lo sabrás en una tarde.</p>
    <div class="botones">""" + mailto + """</div>
  </div>
</section>

</main>
"""))

    # ==================================================================
    # PRECIOS
    # ==================================================================
    hechas.append(pagina("precios.html",
        "Precio de ARC",
        "349,99 € al mes más IVA: mantenimiento y cinco usuarios incluidos, 60 € por "
        "usuario a partir del sexto. Sin permanencia: se cancela cuando se quiera. Puesta en "
        "marcha desde 2.500 €.",
        """
<main>
<section class="hoja tira">
  <p class="eti"><b>Tarifa</b> · vigente desde septiembre de 2026</p>
  <h1>Lo que cuesta, entero</h1>
  <p class="entradilla">Sin tramos escondidos y sin «consúltanos». El precio está aquí porque
    si no puedes decidir con él delante, no es un precio.</p>

  <div class="tarifa">
    <div class="panel">
      <div class="panel-cab">
        <p class="eti">Cuota mensual</p>
        <div class="granprecio"><b>349,99 €</b><span>al mes + IVA</span></div>
        <p class="nota" style="margin-top:10px">423,49 € al mes con el 21 % de IVA. Es lo que
          se carga en la tarjeta.</p>
      </div>
      <div class="panel-cue">
        <ul class="incluye">
          <li><strong>Mantenimiento y actualizaciones.</strong> <em>No hay versiones de pago
              aparte: lo que se añade lo tienes.</em></li>
          <li><strong>Cinco usuarios incluidos.</strong> <em>El usuario de taller cuenta medio,
              porque solo lee su orden y marca por dónde va.</em></li>
          <li><strong>60 € al mes por usuario</strong> a partir del sexto. <em>Antes de dar un
              acceso se te dice lo que sube: se avisa y se cobra, no se bloquea.</em></li>
          <li><strong>Tus obras y tus catálogos en la nube</strong>, con copia y con historial
              de versiones de cada obra.</li>
          <li><strong>Soporte</strong> por correo, de quien ha escrito el programa.</li>
        </ul>
      </div>
    </div>

    <div class="panel" id="calc">
      <div class="panel-cab">
        <p class="eti">Calcula la tuya</p>
        <p style="font-size:15px;color:var(--apagado)">Mueve las dos barras. Es la misma
          cuenta que hace la aplicación cuando te factura.</p>
      </div>
      <div class="calc">
        <div class="calc-fila">
          <label for="nEdit">Diseñan, presupuestan o llevan la casa</label>
          <div class="calc-val"><b><span id="vEdit">5</span></b><i><span id="eEdit">personas</span> · cuentan 1</i></div>
          <input type="range" id="nEdit" min="1" max="20" value="5">
        </div>
        <div class="calc-fila">
          <label for="nTaller">Taller</label>
          <div class="calc-val"><b><span id="vTaller">2</span></b><i><span id="eTaller">personas</span> · cuentan ½</i></div>
          <input type="range" id="nTaller" min="0" max="20" value="2">
        </div>

        <div class="desglose">
          <div class="dfila"><span>Cuota</span><b id="dBase">349,99 €</b></div>
          <div class="dfila" id="filaExtra"><span>Usuarios de más</span><b id="dExtra">60,00 €</b>
            <em id="dExtraNota"></em></div>
          <div class="dfila"><span>Base imponible</span><b id="dImponible">409,99 €</b></div>
          <div class="dfila"><span>IVA 21 %</span><b id="dIva">86,10 €</b></div>
          <div class="dfila dfila--total"><span>Total al mes</span><b id="dTotal">496,09 €</b></div>
        </div>
        <p class="nota">Cuentan <b id="dQuien">6</b> usuarios. <span id="dPagina">Los que pasan
          de cinco se cobran a 60 € cada uno.</span></p>
      </div>
    </div>
  </div>

  <div class="cota cota--sola"><span>Conceptos facturables</span></div>

  <h2>Los conceptos, uno a uno</h2>
  <div class="envuelve">
  <table class="tabla">
    <thead><tr><th>Concepto</th><th>Cuándo se cobra</th><th>Importe</th></tr></thead>
    <tbody>
      <tr><td><strong>Cuota mensual</strong><br><span style="color:var(--apagado);font-size:14px">Uso del software, mantenimiento, actualizaciones, alojamiento y copias. Cinco usuarios.</span></td>
          <td>Cada mes, por adelantado</td><td>349,99 € + IVA</td></tr>
      <tr><td><strong>Usuario adicional</strong><br><span style="color:var(--apagado);font-size:14px">A partir del sexto. El de taller cuenta medio.</span></td>
          <td>En la cuota del mes siguiente</td><td>60 € + IVA</td></tr>
      <tr><td><strong>Puesta en marcha</strong><br><span style="color:var(--apagado);font-size:14px">Configurar tu sistema constructivo, cargar tu biblioteca, tu tarifa y tus plantillas de máquina, y cuadrar el despiece contra muebles ya fabricados.</span></td>
          <td>Una vez, al empezar</td><td>desde 2.500 € + IVA</td></tr>
      <tr><td><strong>Sistema constructivo o máquina adicional</strong><br><span style="color:var(--apagado);font-size:14px">Un segundo post-procesador, otra forma de montar, otra biblioteca.</span></td>
          <td>Cuando se pide</td><td>presupuesto aparte</td></tr>
    </tbody>
  </table>
  </div>

  <div class="cota cota--sola"><span>Alta, cobro y baja</span></div>

  <h2>Cómo se paga y cómo se deja</h2>
  <div class="pasos">
    <div class="paso"><div class="n">01</div><div>
      <h3>Desde el primer mes, la aplicación entera</h3>
      <p>No hay demo capada ni versión recortada: se paga la cuota y se trabaja con tu
         fábrica dentro, con todo lo que hay.</p></div></div>
    <div class="paso"><div class="n">02</div><div>
      <h3>Sin permanencia, ningún mes</h3>
      <p>No se firma un año ni tres meses ni nada. Se paga mes a mes, y el mes que decidas
         dejarlo lo dejas. Si esto tiene que retenerte, que sea porque te ahorra trabajo, no
         porque hayas firmado un papel.</p></div></div>
    <div class="paso"><div class="n">03</div><div>
      <h3>Se cobra por adelantado, todos los meses</h3>
      <p>Con tarjeta o domiciliación SEPA, a través de Stripe. ARC no guarda tu número de
         tarjeta en ningún sitio.</p></div></div>
    <div class="paso"><div class="n">04</div><div>
      <h3>Y si dejas de pagar, no se te encierra</h3>
      <p>Tus obras se siguen abriendo, imprimiendo y exportando, y el taller puede seguir
         marcando lo que ya está en la sierra. Lo que se para es crear obras nuevas y cambiar
         las que hay. Puedes llevarte tus datos cuando quieras.</p></div></div>
  </div>

  <p class="nota" style="margin-top:26px">Todo esto, escrito y con sus plazos, está en las
    <a href="/condiciones" style="color:var(--rojo)">condiciones de contratación</a>.</p>

  <div class="botones">""" + mailto + """
    <a class="btn btn--linea" href="/#contacto">Volver a lo que hace</a></div>
</section>
</main>
"""))

    # ==================================================================
    # CONDICIONES DE CONTRATACIÓN
    # ==================================================================
    hechas.append(pagina("condiciones.html",
        "Condiciones de contratación",
        "Condiciones del servicio ARC: objeto, precio, IVA, forma de pago, duración, "
        "cancelación sin permanencia y disponibilidad.",
        """
<main class="hoja legal">
  <p class="eti"><b>Legal</b> · Condiciones</p>
  <h1>Condiciones de contratación</h1>
  <span class="fecha">Última actualización: """ + ACTUALIZADO + """</span>

  <p>Estas condiciones regulan la contratación del servicio <strong>ARC</strong>, software en
     la nube para el diseño, el despiece y el presupuesto de mueble a medida, prestado por
     <strong>""" + dato("razon", "nombre y apellidos del titular") + """</strong>, que opera bajo el nombre
     comercial <strong>""" + EMPRESA["marca"] + """</strong> (en adelante, «ARC»).</p>

  <div class="ficha">
    """ + campo("Prestador", "razon", "nombre y apellidos del titular") + campo(EMPRESA["etiqueta_nif"], "cif") + \
          campo("Domicilio", "domicilio") + """
    <div><b>Contacto</b><span>""" + enlace("email") + """ · """ + enlace("telefono") + """</span></div>
  </div>

  <h2>1. Qué se contrata</h2>
  <p>El acceso, por suscripción, a la aplicación ARC para una empresa fabricante. Incluye:</p>
  <ul>
    <li>Uso de la aplicación por el número de usuarios contratado.</li>
    <li>Alojamiento de las obras, del perfil de fábrica y de los catálogos de la empresa.</li>
    <li>Mantenimiento correctivo y las mejoras que se vayan publicando, sin coste añadido.</li>
    <li>Soporte por correo electrónico en días laborables.</li>
  </ul>
  <p>La <strong>puesta en marcha</strong> —configurar el sistema constructivo de la empresa,
     cargar su biblioteca de muebles, su tarifa y las plantillas de su maquinaria, y
     comprobar el despiece contra muebles ya fabricados— es un servicio distinto, se
     presupuesta aparte y se factura una sola vez.</p>

  <h2>2. Precio e IVA</h2>
  <ul>
    <li><strong>Cuota mensual:</strong> 349,99 € más IVA. Incluye mantenimiento y cinco
        usuarios.</li>
    <li><strong>Usuario adicional:</strong> 60 € más IVA al mes por cada usuario que exceda
        de cinco. A estos efectos, un usuario con perfil de taller computa como medio
        usuario, por tener acceso únicamente de lectura a su orden y a marcar su estado.</li>
    <li><strong>Puesta en marcha:</strong> desde 2.500 € más IVA, según el alcance
        presupuestado.</li>
  </ul>
  <p>Todos los importes se expresan sin IVA salvo indicación expresa. Se aplicará el tipo
     impositivo vigente en cada momento (actualmente el 21 %). En operaciones
     intracomunitarias con NIF-IVA válido se aplicará la inversión del sujeto pasivo, y la
     factura se emitirá sin IVA.</p>
  <p>ARC podrá actualizar sus tarifas comunicándolo con <strong>treinta días</strong> de
     antelación. El cliente que no acepte la nueva tarifa puede darse de baja antes de que
     entre en vigor, sin penalización.</p>

  <h2>3. Forma de pago</h2>
  <p>La cuota se abona <strong>por adelantado</strong>, al inicio de cada periodo mensual,
     mediante tarjeta o adeudo domiciliado SEPA a través de <strong>Stripe</strong>, que
     actúa como proveedor de servicios de pago. ARC no almacena datos completos de tarjeta en
     sus sistemas.</p>
  <p>En el extracto bancario del cliente, el cargo aparece como
     <strong>""" + EMPRESA["descriptor"] + """</strong>.</p>
  <p>El número de usuarios se calcula al cierre de cada periodo y las altas se reflejan en la
     cuota del mes siguiente. Antes de dar de alta a un usuario, la propia aplicación informa
     del importe al que pasaría la cuota.</p>

  <h2>4. Duración</h2>
  <ul>
    <li>El contrato se inicia el día del alta y se renueva automáticamente por periodos
        mensuales mientras el cliente no lo cancele.</li>
    <li><strong>No existe compromiso de permanencia</strong>, ni al principio ni después. El
        cliente puede darse de baja en cualquier momento, sin penalización de ningún tipo y
        sin necesidad de justificar el motivo.</li>
    <li>Desde el primer mes se dispone de la aplicación completa: no hay versiones
        recortadas ni funciones reservadas a planes superiores.</li>
  </ul>

  <h2>5. Cancelación y devoluciones</h2>
  <p>La baja se solicita por escrito al correo de contacto, <strong>en cualquier
     momento</strong>. Surte efecto al terminar el periodo mensual que el cliente ya tiene
     abonado, y a partir de ahí no se emiten más cargos.</p>
  <p><strong>No hay penalización por cancelar</strong>, ni cuotas pendientes que abonar, ni
     plazo mínimo de permanencia.</p>
  <p>El mes ya iniciado no se prorratea ni se devuelve, por tratarse de un servicio ya
     prestado y disponible durante todo ese periodo.</p>
  <p>Si la cancelación se debe a un <strong>incumplimiento de ARC</strong> —indisponibilidad
     continuada del servicio o incumplimiento de lo pactado, no subsanado en treinta días
     desde la reclamación— no se aplicará penalización alguna y se devolverá la parte de
     cuota correspondiente al periodo no prestado.</p>
  <p>La puesta en marcha, una vez ejecutada, no es reembolsable. Si se cancela antes de
     terminarla, se factura únicamente el trabajo realizado hasta ese momento.</p>
  <p>Al tratarse de un contrato entre empresarios, no resulta de aplicación el derecho de
     desistimiento previsto para consumidores.</p>

  <h2>6. Impago</h2>
  <p>Si un recibo resulta impagado, ARC lo comunicará y el servicio continuará con
     normalidad mientras se regulariza. De persistir el impago, la cuenta pasa a
     <strong>solo lectura</strong>: las obras existentes se pueden abrir, imprimir y
     exportar, y el taller puede seguir marcando el estado de lo que ya está en producción,
     pero no se pueden crear obras nuevas ni modificar las existentes. En ningún caso se
     bloquea el acceso a los datos ya generados por el cliente.</p>

  <h2>7. Datos del cliente</h2>
  <p>Las obras, el perfil de fábrica, la tarifa y los catálogos que el cliente introduce
     <strong>son suyos</strong>. ARC no los usa para otra finalidad que prestar el servicio,
     no los cede a terceros y no los emplea para elaborar productos para otros clientes.</p>
  <p>El cliente puede solicitar en cualquier momento una copia exportable de sus obras y de
     su perfil. Tras la baja, los datos se conservan <strong>sesenta días</strong> por si el
     cliente los reclama, y después se eliminan.</p>

  <h2>8. Disponibilidad y soporte</h2>
  <p>ARC pone los medios razonables para que el servicio esté disponible de forma continuada,
     apoyándose en proveedores de infraestructura profesionales. No se garantiza un
     porcentaje de disponibilidad, y pueden producirse interrupciones por mantenimiento, que
     se avisarán cuando sean previsibles.</p>
  <p>El soporte se presta por correo electrónico en días laborables. Las incidencias que
     impiden trabajar se atienden con prioridad.</p>

  <h2>9. Responsabilidad</h2>
  <p>ARC es una herramienta de cálculo y de documentación. <strong>La comprobación del
     despiece, de los programas de máquina y de los presupuestos antes de cortar o de cerrar
     un precio corresponde al cliente</strong>, que conoce su taller y su maquinaria. ARC no
     responde del material cortado a partir de datos introducidos o configurados
     incorrectamente.</p>
  <p>Salvo dolo o negligencia grave, la responsabilidad de ARC se limita al importe de las
     cuotas abonadas por el cliente en los doce meses anteriores al hecho que la origine.</p>

  <h2>10. Ley aplicable</h2>
  <p>Estas condiciones se rigen por la legislación española. Para cualquier controversia, las
     partes se someten a los juzgados y tribunales del domicilio de ARC, salvo que una norma
     imperativa disponga otro fuero.</p>

  <p style="margin-top:32px"><a href="/precios">Volver al precio</a></p>
</main>
"""))

    # ==================================================================
    # PRIVACIDAD
    # ==================================================================
    hechas.append(pagina("privacidad.html",
        "Política de privacidad",
        "Qué datos trata ARC, para qué, con qué base legal, quién los procesa y cómo "
        "ejercer los derechos del RGPD.",
        """
<main class="hoja legal">
  <p class="eti"><b>Legal</b> · Privacidad</p>
  <h1>Política de privacidad</h1>
  <span class="fecha">Última actualización: """ + ACTUALIZADO + """</span>

  <p>Esta política explica qué datos personales trata ARC, para qué y durante cuánto tiempo.
     Está escrita para que se entienda, no para cubrirse.</p>

  <h2>Responsable del tratamiento</h2>
  <div class="ficha">
    """ + campo("Responsable", "razon", "nombre y apellidos del titular") + campo(EMPRESA["etiqueta_nif"], "cif") + \
          campo("Domicilio", "domicilio") + """
    <div><b>Contacto</b><span>""" + enlace("email") + """ · """ + enlace("telefono") + """</span></div>
  </div>

  <h2>Qué datos se tratan y para qué</h2>
  <h3>Si escribes para pedir información</h3>
  <p>Tu nombre, tu correo, tu teléfono si lo das y lo que cuentes en el mensaje. Se usan para
     contestarte y, si hay presupuesto, para seguir la conversación comercial. Base legal: tu
     propia solicitud (medidas precontractuales) y el interés legítimo en atender una
     consulta. Se conservan mientras dure el contacto y hasta un año después.</p>

  <h3>Si eres cliente</h3>
  <p>Los datos de contacto y de facturación de la empresa, y el <strong>correo electrónico y
     el rol</strong> de cada usuario que accede. Es lo mínimo para que cada persona entre a
     lo suyo y para emitir la factura. Base legal: la ejecución del contrato y las
     obligaciones fiscales. Se conservan mientras dure la relación y, después, los años que
     exijan las normas contable y fiscal.</p>
  <p>ARC <strong>no</strong> pide ni almacena números de tarjeta. El cobro lo procesa Stripe
     con sus propios sistemas.</p>

  <h3>Lo que metes dentro de la aplicación</h3>
  <p>Las obras, el perfil de fábrica, la tarifa y los catálogos son <strong>tuyos</strong>.
     ARC los aloja y los procesa únicamente para prestarte el servicio. No se usan para
     entrenar nada, no se ceden y no sirven para elaborar productos para otros clientes.
     Normalmente no contienen datos personales; si tú los metes —por ejemplo, el nombre de un
     cliente final en un presupuesto—, ARC actúa como <em>encargado del tratamiento</em> y tú
     como responsable.</p>

  <h3>Esta web</h3>
  <p>El sitio no lleva analítica, ni píxeles, ni publicidad, ni redes sociales incrustadas. No
     se crea ningún perfil de quien lo visita. El servidor guarda registros técnicos de acceso
     (dirección IP, momento y página) durante un plazo breve, por seguridad.</p>

  <h2>Quién más ve los datos</h2>
  <p>Solo los proveedores necesarios para que esto funcione, todos con contrato de encargado
     de tratamiento:</p>
  <ul>
    <li><strong>Vercel</strong> — alojamiento del sitio y de la aplicación.</li>
    <li><strong>Supabase</strong> — base de datos, autenticación y almacenamiento de ficheros.</li>
    <li><strong>Stripe</strong> — cobros y facturación. Trata los datos de pago como
        responsable propio.</li>
    <li>Proveedor de correo electrónico, para la comunicación y el soporte.</li>
  </ul>
  <p>Alguno de estos proveedores puede tratar datos fuera del Espacio Económico Europeo. En
     ese caso se ampara en las cláusulas contractuales tipo aprobadas por la Comisión Europea
     o en una decisión de adecuación. No se cede ningún dato a nadie más, y no se venden.</p>

  <h2>Tus derechos</h2>
  <p>Puedes pedir acceso a tus datos, su rectificación, su supresión, la limitación u
     oposición al tratamiento y su portabilidad, escribiendo a
     """ + enlace("email") + """. Se contesta en el plazo de un mes.</p>
  <p>Si crees que no se ha atendido bien tu solicitud, puedes reclamar ante la
     <a href="https://www.aepd.es" rel="noopener">Agencia Española de Protección de Datos</a>.</p>

  <h2>Seguridad</h2>
  <p>El acceso a la aplicación exige cuenta y contraseña. Cada empresa está aislada de las
     demás en la propia base de datos, no solo en la pantalla: una consulta hecha por fuera
     de la aplicación tampoco devuelve filas de otra empresa. Las comunicaciones van cifradas
     y se hacen copias de seguridad periódicas.</p>

  <p style="margin-top:32px"><a href="/">Volver al inicio</a></p>
</main>
"""))

    # ==================================================================
    # AVISO LEGAL
    # ==================================================================
    hechas.append(pagina("aviso-legal.html",
        "Aviso legal",
        "Datos identificativos del titular del sitio, condiciones de uso y propiedad "
        "intelectual.",
        """
<main class="hoja legal">
  <p class="eti"><b>Legal</b> · Aviso</p>
  <h1>Aviso legal</h1>
  <span class="fecha">Última actualización: """ + ACTUALIZADO + """</span>

  <p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la
     información y de comercio electrónico, se hacen constar los datos del titular de este
     sitio.</p>

  <div class="ficha">
    """ + campo("Titular", "razon", "nombre y apellidos del titular") + campo(EMPRESA["etiqueta_nif"], "cif") + \
          campo("Domicilio", "domicilio") + """
    <div><b>Correo</b><span>""" + enlace("email") + """</span></div>
    <div><b>Teléfono</b><span>""" + enlace("telefono") + """</span></div>
    """ + campo("Datos registrales", "registro") + """
    <div><b>Nombre comercial</b><span>""" + EMPRESA["marca"] + """</span></div>
    <div><b>Actividad</b><span>Desarrollo y explotación de software para la fabricación de mueble a medida</span></div>
  </div>
  <p>ARC Automatizaciones es el <strong>nombre comercial</strong> bajo el que ejerce su
     actividad la persona física indicada arriba. Al tratarse de un empresario individual y no
     de una sociedad mercantil, no procede inscripción en el Registro Mercantil ni existen, por
     tanto, datos registrales.</p>

  <h2>Uso del sitio</h2>
  <p>Este sitio ofrece información sobre el servicio ARC. Quien lo visita se compromete a no
     utilizarlo para fines ilícitos ni a intentar dañar sus sistemas.</p>
  <p>Se procura que la información esté actualizada y sea correcta. Los precios publicados
     son los vigentes en la fecha de actualización que figura arriba; las condiciones que
     obligan a las partes son las que se firman al contratar, recogidas en las
     <a href="/condiciones">condiciones de contratación</a>.</p>

  <h2>Propiedad intelectual</h2>
  <p>El software ARC, este sitio, sus textos, su código y la marca <strong>ARC
     Automatizaciones</strong> y su logotipo pertenecen a su titular. Contratar el servicio da
     derecho a usar la aplicación durante la vigencia del contrato; no transfiere la
     propiedad del software ni permite copiarlo, descompilarlo o revenderlo.</p>
  <p>Los datos que cada cliente introduce en la aplicación —sus obras, su forma de montar, su
     tarifa y sus catálogos— son propiedad del cliente, no de ARC.</p>

  <h2>Enlaces</h2>
  <p>Si este sitio enlaza a páginas de terceros, es por referencia. ARC no responde de su
     contenido.</p>

  <h2>Legislación</h2>
  <p>Este aviso se rige por la legislación española.</p>

  <p style="margin-top:32px"><a href="/">Volver al inicio</a></p>
</main>
"""))

    # ==================================================================
    # COOKIES
    # ==================================================================
    hechas.append(pagina("cookies.html",
        "Política de cookies",
        "Esta web no usa cookies de analítica, publicidad ni seguimiento. Qué guarda la "
        "aplicación y por qué.",
        """
<main class="hoja legal">
  <p class="eti"><b>Legal</b> · Cookies</p>
  <h1>Política de cookies</h1>
  <span class="fecha">Última actualización: """ + ACTUALIZADO + """</span>

  <h2>Esta web no usa cookies</h2>
  <p>Ni de analítica, ni de publicidad, ni de seguimiento, ni de redes sociales. Por eso no
     hay ningún cartel pidiéndote que aceptes nada: no habría nada que aceptar.</p>
  <p>Tampoco se cargan fuentes ni recursos que perfilen a quien visita el sitio más allá de la
     tipografía y de las imágenes propias necesarias para verlo.</p>

  <h2>Lo que sí guarda la aplicación</h2>
  <p>Dentro de la aplicación —la parte con usuario y contraseña— el navegador guarda lo
     imprescindible para trabajar:</p>
  <ul>
    <li><strong>La sesión.</strong> Para no pedirte la contraseña en cada pantalla. Se borra
        al cerrar sesión.</li>
    <li><strong>El borrador de la obra que tienes abierta.</strong> Para que un cierre
        accidental de la pestaña no se lleve por delante media mañana de trabajo. Se queda en
        tu navegador y no se envía a ningún tercero.</li>
    <li><strong>Preferencias de pantalla</strong>, como el último perfil usado.</li>
  </ul>
  <p>Todo ello es almacenamiento <strong>técnico y necesario</strong>: sin él la aplicación no
     funciona, y por eso no requiere consentimiento previo (art. 22.2 LSSI). No se usa para
     medir audiencias ni para publicidad.</p>

  <h2>Cómo borrarlo</h2>
  <p>Desde la configuración de tu navegador puedes borrar el almacenamiento de este sitio en
     cualquier momento. Si lo haces mientras trabajas, perderás la sesión y el borrador que no
     hayas guardado.</p>

  <p style="margin-top:32px"><a href="/privacidad">Política de privacidad</a> ·
     <a href="/">Volver al inicio</a></p>
</main>
"""))

    return hechas
