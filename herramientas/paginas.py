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
    mailto = ('<a class="btn" href="mailto:' + correo + '?subject=Demostraci%C3%B3n%20de%20ARC">'
              'Escribir <small>' + correo + '</small></a>'
              '<a class="btn btn--linea" href="tel:+34' + tel.replace(" ", "") + '">'
              'Llamar <small>' + tel + '</small></a>') if correo else \
             ('<span class="falta">falta: email de contacto</span>')

    # ==================================================================
    # PORTADA
    # ==================================================================
    # PORTADA
    # ==================================================================
    hechas.append(pagina("index.html",
        "ARC Automatizaciones",
        "CAD/CAM para fábricas de mueble a medida. Del alzado se derivan el "
        "despiece, la documentación de taller, el programa CNC, la optimización de "
        "corte, el escandallo y el presupuesto, según el perfil constructivo de cada "
        "empresa.",
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
      <p class="eti"><b>ARC</b> · CAD/CAM para mueble a medida</p>
      <h1>Del alzado al código de máquina.<br><em>Sin volver a medir.</em></h1>
      <p class="entradilla">Un único modelo del que se derivan el despiece, la
        documentación de taller, el programa del centro de mecanizado, la optimización
        de corte, el escandallo y el presupuesto. Con los espesores, las holguras y el
        herraje definidos en el <strong>perfil constructivo</strong> de la empresa.</p>
      <div class="marcas">
        <span>Cocinas</span><span>Armarios</span><span>Despiece paramétrico</span>
        <span>Postprocesador Biesse</span><span>Optimización de corte</span>
        <span>Multiempresa</span>
      </div>
      <div class="botones">
        <a class="btn" href="/precios">Ver la tarifa <small>349,99 €/mes</small></a>
        <a class="btn btn--linea" href="#contacto">Solicitar demostración</a>
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
    <div class="cifra"><b>6</b><span>Salidas de producción derivadas de un único modelo</span></div>
    <div class="cifra"><b>19 · 10 · 0,8</b><span>Espesores de cuerpo, trasera y canto en mm. Parametrizables por empresa</span></div>
    <div class="cifra"><b>4</b><span>Perfiles de acceso: dirección, oficina técnica, diseño y taller</span></div>
    <div class="cifra"><b>Mes a mes</b><span>Suscripción sin permanencia ni penalización por baja</span></div>
  </div>
</section>
</div>

<div class="hoja"><div class="cota cota--sola"><span>Salidas de producción</span></div></div>

<section class="tira tira--blanca" id="que-hace">
  <div class="hoja">
    <p class="eti"><b>01</b> · Lo que se obtiene</p>
    <h2>Seis salidas del mismo modelo</h2>
    <p class="entradilla">No son módulos que se contraten por separado. Definida la
      composición sobre el alzado, la lista de piezas queda determinada, y de ella se
      derivan las cinco salidas restantes.</p>

    <div class="salidas">
      <article class="salida sube"><span class="ref">SAL-01</span>
        <h3>Modelado y despiece</h3>
        <p>Los módulos se posicionan sobre el alzado y el sistema deriva la lista de
           piezas con sus cotas finales: costados, techos, suelos, baldas, traseras y
           frentes. Los espesores, las holguras y el descuento de puerta se toman del
           perfil constructivo, no de valores por defecto.</p></article>
      <article class="salida sube"><span class="ref">SAL-02</span>
        <h3>Documentación de taller</h3>
        <p>Alzado acotado y ficha de fabricación por módulo: composición, número de
           bisagras, referencia de herraje y posición de cada pieza. En formato
           imprimible, para el puesto de trabajo.</p></article>
      <article class="salida sube"><span class="ref">SAL-03</span>
        <h3>Programación CNC</h3>
        <p>Programa para el centro de mecanizado: ranurado de trasera, taladrado de
           cazoleta y de estante, con la herramienta, el diámetro y las compensaciones
           declaradas en el postprocesador de la empresa.</p></article>
      <article class="salida sube"><span class="ref">SAL-04</span>
        <h3>Optimización de corte</h3>
        <p>Distribución de las piezas sobre formato 2850 × 2100 y cómputo de tableros
           por espesor, considerando el espesor de disco y el diámetro de fresa
           configurados.</p></article>
      <article class="salida sube"><span class="ref">SAL-05</span>
        <h3>Escandallo</h3>
        <p>Tablero, canto, herraje y tiempos de taller y de montaje, desglosados módulo
           a módulo. Incluye la relación de aprovisionamiento por proveedor.</p></article>
      <article class="salida sube"><span class="ref">SAL-06</span>
        <h3>Presupuesto</h3>
        <p>PVP con el margen y los portes aplicados, listo para emitir. Las partidas sin
           confirmar quedan señalizadas, de modo que un presupuesto incompleto no se
           cierra por descuido.</p></article>
    </div>
  </div>
</section>

<section class="tira" id="como">
  <div class="hoja">
    <p class="eti"><b>02</b> · Flujo de trabajo</p>
    <h2>Del alzado al tablero mecanizado</h2>
    <p class="entradilla">Cada etapa opera sobre el resultado de la anterior. Esa
      dependencia es la que impide que convivan dos versiones de una misma cota en
      distintos puntos del proceso.</p>

    <div class="pasos">
      <div class="paso sube"><div class="n">01</div><div>
        <h3>Parametrización del perfil constructivo</h3>
        <p>Espesores, holguras, ranurado de trasera, gola, sistema de ensamblaje,
           zócalo, herraje, tarifa y biblioteca de módulos. La configuración se
           introduce por bloques y se valida en conjunto: un bloque incompleto no se
           registra.</p>
        <span class="dato">cuerpo 19 · trasera 10 · canto 0,8 · holgura de frente 3</span>
      </div></div>

      <div class="paso sube"><div class="n">02</div><div>
        <h3>Definición de la obra</h3>
        <p>Los módulos de la biblioteca se sitúan sobre el alzado con sus cotas y sus
           alturas de montaje. El sistema verifica solapes y comprueba el ajuste de cada
           módulo en su hueco.</p>
      </div></div>

      <div class="paso sube"><div class="n">03</div><div>
        <h3>Derivación automática</h3>
        <p>No existe una fase de generación. El despiece, el plano, el cómputo de canto
           y la optimización de corte se recalculan con cada modificación del modelo.</p>
        <span class="dato">M03 · Columna horno · 10 piezas · 28,0 ml de canto</span>
      </div></div>

      <div class="paso sube"><div class="n">04</div><div>
        <h3>Emisión a taller y a máquina</h3>
        <p>La obra pasa a la cola de fabricación con su estado. El perfil de taller opera
           en modo de solo lectura sobre la orden: obtiene documentación y programa, y
           actualiza el avance. Una orden en curso no se modifica por debajo.</p>
      </div></div>

      <div class="paso sube"><div class="n">05</div><div>
        <h3>Cierre económico</h3>
        <p>Escandallo y presupuesto se calculan sobre el mismo modelo que el despiece. No
           existe una hoja de cálculo paralela que haya que mantener sincronizada.</p>
      </div></div>
    </div>
  </div>
</section>

<section class="tira tira--blanca">
  <div class="hoja">
    <p class="eti"><b>03</b> · Parametrización</p>
    <h2>Cada fábrica tiene su sistema constructivo</h2>
    <p class="entradilla">Dos talleres del mismo polígono resuelven el mismo armario con
      cotas distintas, y ambos correctamente. Un sistema que impone un único criterio
      constructivo obliga a corregir el despiece obra por obra, y esa corrección manual
      es la que devuelve el proceso al papel.</p>

    <div class="envuelve">
    <table class="tabla">
      <thead><tr><th>Parámetro</th><th>En ARC</th></tr></thead>
      <tbody>
        <tr><td>Espesor de cuerpo, trasera y frente</td><td>parametrizable</td></tr>
        <tr><td>Holgura entre frentes y descuento de puerta</td><td>parametrizable</td></tr>
        <tr><td>Trasera encastrada o vista, y cota de ranurado</td><td>parametrizable</td></tr>
        <tr><td>Gola, uñero, altura de altos, alto de columna, zócalo</td><td>parametrizable</td></tr>
        <tr><td>Sistema de ensamblaje y herraje por tipología</td><td>parametrizable</td></tr>
        <tr><td>Herramienta, diámetro y compensación del postprocesador</td><td>parametrizable</td></tr>
        <tr><td>Tarifa de tablero, canto, herraje y mano de obra</td><td>parametrizable</td></tr>
      </tbody>
    </table>
    </div>
    <p class="nota">Todos estos valores residen en un único registro, el perfil
      constructivo, y son los que determinan que el despiece salga conforme a la primera.
      Su definición constituye la puesta en marcha, y se factura aparte de la cuota.</p>
  </div>
</section>

<section class="tira">
  <div class="hoja">
    <p class="eti"><b>04</b> · Control de acceso</p>
    <h2>Cada perfil opera sobre lo que le corresponde</h2>
    <p class="entradilla">No es una cuestión de confianza sino de ergonomía y de
      integridad del dato: el puesto de corte no necesita el lienzo de diseño, y una
      interfaz con controles inoperativos degrada el trabajo de quien la usa.</p>

    <div class="envuelve">
    <table class="tabla">
      <thead><tr><th>Perfil</th><th>Alcance</th></tr></thead>
      <tbody>
        <tr><td><strong>Dirección</strong></td><td>Acceso completo, incluidos el perfil constructivo, la tarifa y la gestión de usuarios</td></tr>
        <tr><td><strong>Oficina técnica</strong></td><td>Diseño, documentación, fabricación y presupuesto. Sin acceso al perfil constructivo</td></tr>
        <tr><td><strong>Diseño</strong></td><td>Modelado y presupuesto. Sin emisión a fabricación</td></tr>
        <tr><td><strong>Taller</strong></td><td>Cola de órdenes: documentación, programa CNC y actualización de estado</td></tr>
      </tbody>
    </table>
    </div>
    <p class="nota">El aislamiento entre empresas se aplica en la propia base de datos y
      no en la interfaz: una consulta emitida fuera de la aplicación tampoco devuelve
      registros de otra empresa.</p>
  </div>
</section>

<section class="tira tira--blanca" id="precio">
  <div class="hoja">
    <p class="eti"><b>05</b> · Condiciones económicas</p>
    <h2>Tarifa publicada</h2>
    <div class="tarifa">
      <div class="panel">
        <div class="panel-cab">
          <p class="eti">Cuota mensual</p>
          <div class="granprecio"><b>349,99 €</b><span>al mes + IVA · 423,49 € IVA incluido</span></div>
        </div>
        <div class="panel-cue">
          <ul class="incluye">
            <li>Mantenimiento correctivo y evolutivo incluidos</li>
            <li><strong>Cinco usuarios</strong> incluidos <em>— el perfil de taller computa como medio</em></li>
            <li>60 € al mes por usuario a partir del sexto</li>
            <li>Alojamiento de obras, perfil constructivo y catálogos, con copia y versionado</li>
            <li><strong>Sin permanencia.</strong> <em>Facturación mensual y baja a voluntad</em></li>
          </ul>
          <div class="botones">
            <a class="btn" href="/precios">Ver la tarifa completa</a>
          </div>
        </div>
      </div>
      <div>
        <h3>Puesta en marcha, facturada aparte</h3>
        <p class="nota" style="margin-top:12px;font-size:15.5px">La parametrización no se
          resuelve rellenando un formulario: consiste en levantar el sistema constructivo
          de la empresa, cargar su biblioteca de módulos, su tarifa y las plantillas de
          su maquinaria, y contrastar el despiece resultante contra módulos ya
          fabricados. Se factura una sola vez, <strong>desde 2.500 €</strong>, en función
          del número de sistemas constructivos y de máquinas a integrar.</p>
        <p class="nota" style="font-size:15.5px">Sin compromiso de permanencia. La
          facturación es mensual y la baja surte efecto al término del periodo abonado,
          sin penalización.</p>
      </div>
    </div>
  </div>
</section>

<section class="tira">
  <div class="hoja">
    <p class="eti"><b>06</b> · Consultas frecuentes</p>
    <h2>Lo que se pregunta antes de contratar</h2>
    <div class="faq">
      <details open><summary>Nuestro sistema constructivo no es el estándar. ¿Es compatible?</summary>
        <p>Es la premisa del producto. Espesores, holguras, ranurado, gola, sistema de
           ensamblaje y herraje se parametrizan por empresa. Si un criterio constructivo
           concreto no está contemplado, se incorpora: forma parte de la puesta en
           marcha.</p></details>
      <details><summary>¿Qué maquinaria se requiere?</summary>
        <p>Para modelar, despiezar, documentar y presupuestar, ninguna: basta un
           navegador. Para la salida a máquina se requiere que el centro de mecanizado
           tenga su postprocesador definido. Actualmente está implementado para Biesse
           con plantillas PGMX; otros controles se incorporan en la puesta en
           marcha.</p></details>
      <details><summary>¿Qué garantía de confidencialidad hay sobre nuestras cotas y nuestra tarifa?</summary>
        <p>Cada empresa dispone de su propio espacio y el aislamiento se aplica en la
           base de datos, no en la interfaz: una consulta emitida fuera de la aplicación
           tampoco devuelve registros ajenos. La tarifa y los catálogos quedan tras la
           autenticación, no en un directorio público.</p></details>
      <details><summary>¿Qué ocurre ante un impago?</summary>
        <p>No se retiene el dato. Las obras existentes siguen siendo consultables,
           imprimibles y exportables, y el taller puede continuar actualizando el estado
           de lo que ya está en producción. Lo que queda suspendido es la creación de
           obras nuevas y la modificación de las existentes, previo aviso: un recibo
           pendiente no interrumpe el servicio de forma inmediata.</p></details>
      <details><summary>¿Cuál es el plazo de implantación?</summary>
        <p>Depende del número de sistemas constructivos a levantar y del estado de la
           tarifa de partida. El factor limitante no es el software, sino el contraste
           del despiece contra módulos ya fabricados hasta obtener coincidencia.</p></details>
      <details><summary>¿Existe compromiso de permanencia?</summary>
        <p>No. La facturación es mensual y la baja puede solicitarse en cualquier momento;
           surte efecto al término del periodo ya abonado, sin penalización ni preaviso
           mínimo. Queda recogido en las
           <a href="/condiciones">condiciones de contratación</a>.</p></details>
    </div>
  </div>
</section>

<section class="tira tira--blanca" id="contacto">
  <div class="hoja">
    <p class="eti"><b>07</b> · Contacto</p>
    <h2>La prueba: un módulo ya fabricado</h2>
    <p class="entradilla">Es el modo más rápido de evaluar el sistema. Facilite un módulo
      que su taller ya haya producido, con sus cotas. Si el despiece resultante coincide
      con el suyo, hay una conversación que mantener; si no coincide, también lo sabrá en
      una tarde.</p>
    <div class="botones">""" + mailto + """</div>
  </div>
</section>

</main>
"""))

    # ==================================================================
    # PRECIOS
    # ==================================================================
    hechas.append(pagina("precios.html",
        "Tarifa de ARC",
        "349,99 € al mes más IVA: mantenimiento y cinco usuarios incluidos, 60 € por "
        "usuario adicional. Sin permanencia. Puesta en marcha desde 2.500 €.",
        """
<main>
<section class="hoja tira">
  <p class="eti"><b>Tarifa</b> · en vigor desde septiembre de 2026</p>
  <h1>Condiciones económicas</h1>
  <p class="entradilla">Sin tramos ocultos ni «consúltenos». La tarifa se publica porque
    un precio con el que no se puede decidir no es un precio.</p>

  <div class="tarifa">
    <div class="panel">
      <div class="panel-cab">
        <p class="eti">Cuota mensual</p>
        <div class="granprecio"><b>349,99 €</b><span>al mes + IVA</span></div>
        <p class="nota" style="margin-top:10px">423,49 € al mes con el 21 % de IVA
          repercutido. Es el importe que se domicilia.</p>
      </div>
      <div class="panel-cue">
        <ul class="incluye">
          <li><strong>Mantenimiento correctivo y evolutivo.</strong> <em>Sin versiones de
              pago diferenciadas: las mejoras publicadas quedan incorporadas.</em></li>
          <li><strong>Cinco usuarios incluidos.</strong> <em>El perfil de taller computa
              como medio usuario, por disponer de acceso de solo lectura sobre su orden y
              de actualización de estado.</em></li>
          <li><strong>60 € al mes por usuario</strong> a partir del sexto. <em>Antes de
              dar de alta un acceso, la aplicación informa del importe resultante: se
              notifica y se factura, no se bloquea.</em></li>
          <li><strong>Alojamiento</strong> de obras, perfil constructivo y catálogos, con
              copia de seguridad y versionado por obra.</li>
          <li><strong>Soporte</strong> por correo electrónico, atendido por quien
              desarrolla el producto.</li>
        </ul>
      </div>
    </div>

    <div class="panel" id="calc">
      <div class="panel-cab">
        <p class="eti">Simulador de cuota</p>
        <p style="font-size:15px;color:var(--apagado)">Ajuste ambos controles. Aplica el
          mismo cómputo que la aplicación al emitir la factura.</p>
      </div>
      <div class="calc">
        <div class="calc-fila">
          <label for="nEdit">Dirección, oficina técnica y diseño</label>
          <div class="calc-val"><b><span id="vEdit">5</span></b><i><span id="eEdit">usuarios</span> · factor 1</i></div>
          <input type="range" id="nEdit" min="1" max="20" value="5">
        </div>
        <div class="calc-fila">
          <label for="nTaller">Taller</label>
          <div class="calc-val"><b><span id="vTaller">2</span></b><i><span id="eTaller">usuarios</span> · factor ½</i></div>
          <input type="range" id="nTaller" min="0" max="20" value="2">
        </div>

        <div class="desglose">
          <div class="dfila"><span>Cuota base</span><b id="dBase">349,99 €</b></div>
          <div class="dfila" id="filaExtra"><span>Usuarios adicionales</span><b id="dExtra">60,00 €</b>
            <em id="dExtraNota"></em></div>
          <div class="dfila"><span>Base imponible</span><b id="dImponible">409,99 €</b></div>
          <div class="dfila"><span>IVA 21 %</span><b id="dIva">86,10 €</b></div>
          <div class="dfila dfila--total"><span>Total mensual</span><b id="dTotal">496,09 €</b></div>
        </div>
        <p class="nota">Usuarios computables: <b id="dQuien">6</b>. <span id="dPagina">Los
          que exceden de cinco se facturan a 60 € cada uno.</span></p>
      </div>
    </div>
  </div>

  <div class="cota cota--sola"><span>Conceptos facturables</span></div>

  <h2>Desglose de conceptos</h2>
  <div class="envuelve">
  <table class="tabla">
    <thead><tr><th>Concepto</th><th>Periodicidad</th><th>Importe</th></tr></thead>
    <tbody>
      <tr><td><strong>Cuota mensual</strong><br><span style="color:var(--apagado);font-size:14px">Licencia de uso, mantenimiento, alojamiento y copias de seguridad. Cinco usuarios incluidos.</span></td>
          <td>Mensual, por anticipado</td><td>349,99 € + IVA</td></tr>
      <tr><td><strong>Usuario adicional</strong><br><span style="color:var(--apagado);font-size:14px">A partir del sexto usuario computable. El perfil de taller computa como medio.</span></td>
          <td>En la cuota del periodo siguiente</td><td>60 € + IVA</td></tr>
      <tr><td><strong>Puesta en marcha</strong><br><span style="color:var(--apagado);font-size:14px">Levantamiento del sistema constructivo, carga de la biblioteca de módulos, de la tarifa y de las plantillas de máquina, y contraste del despiece contra módulos ya fabricados.</span></td>
          <td>Pago único, al inicio</td><td>desde 2.500 € + IVA</td></tr>
      <tr><td><strong>Sistema constructivo o máquina adicional</strong><br><span style="color:var(--apagado);font-size:14px">Segundo postprocesador, criterio constructivo alternativo o biblioteca independiente.</span></td>
          <td>Bajo demanda</td><td>presupuesto aparte</td></tr>
    </tbody>
  </table>
  </div>

  <div class="cota cota--sola"><span>Alta, facturación y baja</span></div>

  <h2>Contratación y baja</h2>
  <div class="pasos">
    <div class="paso"><div class="n">01</div><div>
      <h3>Alcance completo desde el primer periodo</h3>
      <p>No se comercializa una versión reducida ni una demostración limitada: se abona la
         cuota y se opera con el perfil constructivo de la empresa cargado, con todas las
         salidas disponibles.</p></div></div>
    <div class="paso"><div class="n">02</div><div>
      <h3>Sin compromiso de permanencia</h3>
      <p>No se suscribe un plazo mínimo. La facturación es mensual y la relación se
         interrumpe en el periodo que el cliente decida. La permanencia de un cliente
         debe sustentarse en el ahorro de proceso, no en una cláusula.</p></div></div>
    <div class="paso"><div class="n">03</div><div>
      <h3>Facturación mensual anticipada</h3>
      <p>Mediante tarjeta o adeudo domiciliado SEPA, a través de Stripe como proveedor de
         servicios de pago. ARC no almacena datos completos de tarjeta en sus
         sistemas.</p></div></div>
    <div class="paso"><div class="n">04</div><div>
      <h3>Continuidad de acceso ante impago</h3>
      <p>Las obras siguen siendo consultables, imprimibles y exportables, y el taller
         mantiene la actualización de estado de lo que está en producción. Queda
         suspendida la creación y la modificación de obras. Los datos son exportables en
         cualquier momento.</p></div></div>
  </div>

  <p class="nota" style="margin-top:26px">Todo ello, con sus plazos, queda recogido en las
    <a href="/condiciones" style="color:var(--rojo)">condiciones de contratación</a>.</p>

  <div class="botones">""" + mailto + """
    <a class="btn btn--linea" href="/#que-hace">Volver a las salidas de producción</a></div>
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
  <p>La licencia de uso, en régimen de suscripción, de la aplicación ARC para una empresa
     fabricante. Comprende:</p>
  <ul>
    <li>Uso de la aplicación por el número de usuarios computables contratado.</li>
    <li>Alojamiento de las obras, del perfil constructivo y de los catálogos de la empresa.</li>
    <li>Mantenimiento correctivo y evolutivo, sin coste adicional por las versiones que se
        vayan publicando.</li>
    <li>Soporte por correo electrónico en días laborables.</li>
  </ul>
  <p>La <strong>puesta en marcha</strong> —levantamiento del sistema constructivo de la
     empresa, carga de su biblioteca de módulos, de su tarifa y de las plantillas de su
     maquinaria, y contraste del despiece resultante contra módulos ya fabricados— constituye
     un servicio independiente, se presupuesta aparte y se factura por una sola vez.</p>

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
     <strong>solo lectura</strong>: las obras existentes siguen siendo consultables,
     imprimibles y exportables, y el perfil de taller mantiene la actualización de estado de
     lo que ya se encuentra en producción, quedando suspendidas la creación de obras nuevas y
     la modificación de las existentes. En ningún caso se bloquea el acceso a los datos ya
     generados por el cliente.</p>

  <h2>7. Datos del cliente</h2>
  <p>Las obras, el perfil constructivo, la tarifa y los catálogos introducidos por el
     cliente son <strong>de su exclusiva propiedad</strong>. ARC no los destina a finalidad
     distinta de la prestación del servicio, no los cede a terceros y no los emplea en la
     elaboración de productos para otros clientes.</p>
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
  <p>ARC es una herramienta de cálculo y de generación documental. <strong>La verificación
     del despiece, de los programas de máquina y de los presupuestos con carácter previo al
     mecanizado o al cierre de un precio corresponde al cliente</strong>, que es quien conoce
     su taller y su maquinaria. ARC no responde del material mecanizado a partir de datos
     introducidos o parametrizados incorrectamente.</p>
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
  <h3>Solicitudes de información</h3>
  <p>Nombre, dirección de correo, teléfono si se facilita y el contenido del mensaje. Se
     tratan para atender la consulta y, en su caso, para dar seguimiento a la relación
     comercial. Base legal: la solicitud del propio interesado (medidas precontractuales) y
     el interés legítimo en atender una consulta. Plazo de conservación: mientras dure el
     contacto y hasta un año después.</p>

  <h3>Clientes</h3>
  <p>Datos de contacto y de facturación de la empresa, y <strong>dirección de correo y perfil
     de acceso</strong> de cada usuario. Es el dato mínimo necesario para aplicar el control
     de acceso por perfil y para emitir la factura. Base legal: ejecución del contrato y
     obligaciones fiscales. Plazo de conservación: durante la vigencia de la relación y,
     posteriormente, el exigido por la normativa contable y fiscal.</p>
  <p>ARC <strong>no</strong> solicita ni almacena numeración completa de tarjeta. El cobro lo
     procesa Stripe en sus propios sistemas.</p>

  <h3>Contenido introducido en la aplicación</h3>
  <p>Las obras, el perfil constructivo, la tarifa y los catálogos son
     <strong>propiedad del cliente</strong>. ARC los aloja y los trata exclusivamente para la
     prestación del servicio: no se emplean para entrenar modelos, no se ceden y no
     intervienen en la elaboración de productos para terceros. Habitualmente no contienen
     datos personales; si el cliente los incorpora —por ejemplo, el nombre de un consumidor
     final en un presupuesto—, ARC actúa como <em>encargado del tratamiento</em> y el cliente
     como responsable.</p>

  <h3>Este sitio web</h3>
  <p>El sitio no incorpora analítica, píxeles de seguimiento, publicidad ni contenido
     embebido de redes sociales, y no elabora perfil alguno del visitante. El servidor
     conserva registros técnicos de acceso (dirección IP, marca temporal y recurso
     solicitado) durante un plazo breve, por motivos de seguridad.</p>

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
  <p>El interesado puede ejercer los derechos de acceso, rectificación, supresión,
     limitación, oposición y portabilidad dirigiéndose a
     """ + enlace("email") + """. Se contesta en el plazo de un mes.</p>
  <p>Si considera que su solicitud no ha sido atendida debidamente, puede presentar
     reclamación ante la
     <a href="https://www.aepd.es" rel="noopener">Agencia Española de Protección de Datos</a>.</p>

  <h2>Seguridad</h2>
  <p>El acceso a la aplicación requiere autenticación. El aislamiento entre empresas se
     aplica en la propia base de datos y no únicamente en la interfaz: una consulta emitida
     fuera de la aplicación tampoco devuelve registros de otra empresa. Las comunicaciones
     viajan cifradas y se realizan copias de seguridad periódicas.</p>

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

  <h2>Este sitio no utiliza cookies</h2>
  <p>Ni de analítica, ni publicitarias, ni de seguimiento, ni de redes sociales. De ahí que no
     se muestre ningún aviso de consentimiento: no habría nada que consentir.</p>
  <p>Tampoco se cargan recursos de terceros que permitan elaborar un perfil del visitante,
     más allá de la tipografía y de las imágenes propias necesarias para la presentación.</p>

  <h2>Almacenamiento local de la aplicación</h2>
  <p>En el área autenticada, el navegador conserva únicamente lo imprescindible para operar:</p>
  <ul>
    <li><strong>Identificador de sesión.</strong> Evita repetir la autenticación en cada
        pantalla. Se elimina al cerrar sesión.</li>
    <li><strong>Borrador de la obra en curso.</strong> Preserva el trabajo no guardado ante un
        cierre accidental de la pestaña. Reside en el navegador del usuario y no se transmite
        a terceros.</li>
    <li><strong>Preferencias de interfaz</strong>, como el último perfil utilizado.</li>
  </ul>
  <p>Se trata de almacenamiento <strong>técnico y estrictamente necesario</strong> para la
     prestación del servicio, exceptuado del deber de consentimiento previo conforme al
     artículo 22.2 de la LSSI. No se emplea para medición de audiencias ni con fines
     publicitarios.</p>

  <h2>Supresión</h2>
  <p>El almacenamiento de este sitio puede eliminarse en cualquier momento desde la
     configuración del navegador. Hacerlo durante una sesión de trabajo implica la pérdida de
     la sesión y del borrador no guardado.</p>

  <p style="margin-top:32px"><a href="/privacidad">Política de privacidad</a> ·
     <a href="/">Volver al inicio</a></p>
</main>
"""))

    return hechas
