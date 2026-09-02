/* ===========================================================
   ARC Automatizaciones · el sitio, por dentro
   -----------------------------------------------------------
   Tres cosas y ninguna más:

     1. EL PLANO de la portada. Un alzado que se acota y se
        despieza solo. No es una ilustración inventada: son las
        medidas que salen de verdad de un mueble de 600 con
        cuerpo de 19, trasera de 10 y holgura de frente de 3.

     2. LA CALCULADORA de la cuota. Reproduce EXACTAMENTE la
        regla que factura la aplicación (`cuota_de()`): cinco
        incluidos, sesenta el siguiente, el de taller cuenta
        medio, y el IVA encima de la base. Si algún día cambia
        la regla, cambia en los dos sitios o esta página miente
        a un cliente sobre lo que va a pagar.

     3. Que lo que se lee no dependa de que esto se ejecute.
        Sin JavaScript la página se ve entera; lo único que se
        pierde es el movimiento.
   =========================================================== */
(() => {
  "use strict";
  document.documentElement.classList.add("js");
  const $  = (s, d = document) => d.querySelector(s);
  const $$ = (s, d = document) => [...d.querySelectorAll(s)];
  const quieto = matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- la página actual, en la barra ---------- */
  const aqui = location.pathname.replace(/\/index\.html$/, "/").replace(/\.html$/, "");
  $$(".barra nav a").forEach(a => {
    const suyo = new URL(a.getAttribute("href"), location.href).pathname
      .replace(/\/index\.html$/, "/").replace(/\.html$/, "");
    if (suyo === aqui) a.setAttribute("aria-current", "page");
  });

  /* ---------- aparición al entrar ----------
     Aditiva de verdad: NADA se esconde esperando a un observador.
     Escondiendo hasta que el observador dispare, una captura de la
     página entera, la vista previa de un enlace compartido y quien
     no llega a hacer scroll ven media web EN BLANCO. Aquí la clase
     solo lanza una animación que arranca ya visible. */
  if (!quieto && "IntersectionObserver" in window) {
    const ojo = new IntersectionObserver((es) => {
      es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("vista"); ojo.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: .06 });
    $$(".sube").forEach((n, i) => { n.style.animationDelay = `${Math.min(i % 6, 5) * 55}ms`; ojo.observe(n); });
  } else {
    $$(".sube").forEach(n => n.classList.add("vista"));
  }

  /* ===========================================================
     1 · EL PLANO
     ========================================================= */
  const lienzo = $("#plano");
  if (lienzo) dibujaPlano(lienzo);

  function dibujaPlano(cv) {
    const ctx = cv.getContext("2d");
    const ANCHO = 1000, ALTO = 560;          // el papel, en px lógicos
    const MURO = 3600, TECHO = 2400;         // la pared, en mm

    /* Los muebles del alzado. Medidas de verdad, en mm desde el
       suelo y desde la esquina izquierda. */
    const COL = { x0: 0, x1: 600, y0: 0, y1: 2400, t: "Columna horno", ref: "M03" };
    const BAJOS = [
      { x0: 600, x1: 1200, t: "Bajo 1 puerta", ref: "M01" },
      { x0: 1200, x1: 2100, t: "Bajo 3 cajones", ref: "M02" },
      { x0: 2100, x1: 2700, t: "Bajo 1 puerta", ref: "M04" },
      { x0: 2700, x1: 3600, t: "Fregadero", ref: "M05" },
    ].map(m => ({ ...m, y0: 100, y1: 820 }));          // patas 100 + cuerpo 720
    const ALTOS = [
      { x0: 1200, x1: 2100, t: "Alto 2 puertas", ref: "M06" },
      { x0: 2100, x1: 2700, t: "Alto 1 puerta", ref: "M07" },
      { x0: 2700, x1: 3600, t: "Campana", ref: "M08" },
    ].map(m => ({ ...m, y0: 1450, y1: 2150 }));
    const ENCIMERA = { x0: 600, x1: 3600, y0: 820, y1: 860 };

    /* El despiece de la columna: cuerpo de 19, trasera de 10,
       holgura de frente de 3. Sale de restar, no de inventar. */
    const PIEZAS = [
      { n: "Costado izq.", a: 2400, b: 560, g: 19 },
      { n: "Costado der.", a: 2400, b: 560, g: 19 },
      { n: "Techo",        a: 562,  b: 560, g: 19 },
      { n: "Suelo",        a: 562,  b: 560, g: 19 },
      { n: "Balda",        a: 562,  b: 540, g: 19 },
      { n: "Balda",        a: 562,  b: 540, g: 19 },
      { n: "Trasera",      a: 2370, b: 570, g: 10 },
      { n: "Puerta baja",  a: 1190, b: 594, g: 19 },
      { n: "Puerta alta",  a: 594,  b: 594, g: 19 },
      { n: "Zócalo",       a: 100,  b: 596, g: 19 },
    ];

    const tinta = () => leer("--tinta"), linea = () => leer("--linea2"),
          rojo = () => leer("--rojo"), flojo = () => leer("--apagado"),
          fondo = () => leer("--hoja");
    function leer(v) {
      return getComputedStyle(document.documentElement).getPropertyValue(v).trim() || "#000";
    }

    /* El encaje. Se recalcula al cambiar de tamaño porque el
       lienzo es fluido y una escala fija deja el dibujo fuera. */
    const MI = 66, MD = 34, MS = 40, MB = 74;   // márgenes: izq, der, sup, inf
    const esc = Math.min((ANCHO - MI - MD) / MURO, (ALTO - MS - MB) / TECHO);
    const anchoDib = MURO * esc;
    const X0 = MI + ((ANCHO - MI - MD) - anchoDib) / 2;
    const Y0 = ALTO - MB;                        // el suelo
    const px = mm => mm * esc;
    const X = mm => X0 + px(mm);
    const Y = mm => Y0 - px(mm);

    function tamano() {
      const dpr = Math.min(devicePixelRatio || 1, 2);
      cv.width = ANCHO * dpr; cv.height = ALTO * dpr;
      cv.style.aspectRatio = `${ANCHO} / ${ALTO}`;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }
    tamano();
    addEventListener("resize", () => { tamano(); pinta(fase, avance); });

    /* ---------- utilidades de dibujo ---------- */
    const rect = (m, tr = 1) => {
      const x = X(m.x0), y = Y(m.y1), w = px(m.x1 - m.x0), h = px(m.y1 - m.y0);
      if (tr >= 1) { ctx.strokeRect(x, y, w, h); return; }
      /* Se dibuja el perímetro como si lo trazara un lápiz: el
         recorrido entero, cortado por donde va. */
      const per = 2 * (w + h), hasta = per * tr;
      const puntos = [[x, y], [x + w, y], [x + w, y + h], [x, y + h], [x, y]];
      let and = 0;
      ctx.beginPath(); ctx.moveTo(x, y);
      for (let i = 1; i < puntos.length; i++) {
        const [ax, ay] = puntos[i - 1], [bx, by] = puntos[i];
        const d = Math.hypot(bx - ax, by - ay);
        if (and + d <= hasta) { ctx.lineTo(bx, by); and += d; }
        else { const k = Math.max(0, (hasta - and)) / d; ctx.lineTo(ax + (bx - ax) * k, ay + (by - ay) * k); break; }
      }
      ctx.stroke();
    };

    const mono = (t, x, y, tam = 10.5, col = flojo(), al = "center") => {
      ctx.font = `${tam}px "IBM Plex Mono", ui-monospace, monospace`;
      ctx.fillStyle = col; ctx.textAlign = al; ctx.textBaseline = "middle";
      ctx.fillText(t, x, y);
    };

    /* Una cota como la de un plano: dos topes, la línea y el
       número dentro de su hueco. */
    function cotaH(mm0, mm1, mmY, txt, op = 1) {
      const a = X(mm0), b = X(mm1), y = Y(mmY);
      ctx.save(); ctx.globalAlpha = op;
      ctx.strokeStyle = linea(); ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(a, y - 5); ctx.lineTo(a, y + 5);
      ctx.moveTo(b, y - 5); ctx.lineTo(b, y + 5);
      ctx.stroke();
      const m = (a + b) / 2;
      ctx.font = `10.5px "IBM Plex Mono", ui-monospace, monospace`;
      const w = ctx.measureText(txt).width / 2 + 6;
      ctx.beginPath();
      ctx.moveTo(a, y); ctx.lineTo(Math.max(a, m - w), y);
      ctx.moveTo(Math.min(b, m + w), y); ctx.lineTo(b, y);
      ctx.stroke();
      mono(txt, m, y, 10.5, flojo());
      ctx.restore();
    }
    function cotaV(mm0, mm1, mmX, txt, op = 1) {
      const a = Y(mm0), b = Y(mm1), x = X(mmX);
      ctx.save(); ctx.globalAlpha = op;
      ctx.strokeStyle = linea(); ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(x - 5, a); ctx.lineTo(x + 5, a);
      ctx.moveTo(x - 5, b); ctx.lineTo(x + 5, b);
      ctx.moveTo(x, a); ctx.lineTo(x, b);
      ctx.stroke();
      ctx.translate(x, (a + b) / 2); ctx.rotate(-Math.PI / 2);
      ctx.fillStyle = fondo();
      ctx.font = `10.5px "IBM Plex Mono", ui-monospace, monospace`;
      const w = ctx.measureText(txt).width;
      ctx.fillRect(-w / 2 - 5, -7, w + 10, 14);
      mono(txt, 0, 0, 10.5, flojo());
      ctx.restore();
    }

    /* ---------- las cuatro fases ---------- */
    const FASES = ["Trazado", "Cotas", "Despiece", "A máquina"];
    const DUR   = [1500, 1500, 2100, 1900];
    const ESPERA = 1500;
    let fase = 0, avance = 1, t0 = 0, corriendo = false, pedido = 0;
    const suave = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;

    function pinta(f, t) {
      ctx.clearRect(0, 0, ANCHO, ALTO);

      /* El suelo y la pared, siempre. */
      ctx.strokeStyle = linea(); ctx.lineWidth = 1;
      ctx.setLineDash([2, 4]);
      ctx.beginPath(); ctx.moveTo(X(0) - 26, Y(0)); ctx.lineTo(X(MURO) + 26, Y(0)); ctx.stroke();
      ctx.setLineDash([]);

      const traz = f === 0 ? t : 1;
      const desp = f === 2 ? suave(t) : f > 2 ? 1 : 0;
      const maq  = f === 3 ? t : 0;
      const opAlzado = 1 - desp * .86;

      /* --- los muebles --- */
      ctx.save();
      ctx.globalAlpha = opAlzado;
      ctx.lineWidth = 1.4; ctx.strokeStyle = tinta();
      const todos = [...BAJOS, ...ALTOS];
      todos.forEach((m, i) => {
        const p = Math.max(0, Math.min(1, traz * todos.length + 1 - i));
        if (p > 0) rect(m, p);
      });
      /* La encimera va rayada, que es como se marca lo que no se
         fabrica aquí: se pide fuera. */
      if (traz > .55) {
        ctx.save(); ctx.globalAlpha = opAlzado * Math.min(1, (traz - .55) / .3);
        const ex = X(ENCIMERA.x0), ey = Y(ENCIMERA.y1),
              ew = px(ENCIMERA.x1 - ENCIMERA.x0), eh = px(ENCIMERA.y1 - ENCIMERA.y0);
        ctx.strokeRect(ex, ey, ew, eh);
        ctx.beginPath();
        for (let x = ex - eh; x < ex + ew; x += 7) { ctx.moveTo(x, ey + eh); ctx.lineTo(x + eh, ey); }
        ctx.save(); ctx.rect(ex, ey, ew, eh); ctx.clip();
        ctx.lineWidth = .7; ctx.strokeStyle = linea(); ctx.stroke(); ctx.restore();
        ctx.restore();
      }
      ctx.restore();

      /* --- la columna, que es la que se despieza: en rojo --- */
      ctx.save();
      ctx.globalAlpha = traz > .8 ? Math.min(1, (traz - .8) / .2) * (1 - desp * .9) : 0;
      ctx.lineWidth = 1.8; ctx.strokeStyle = rojo();
      rect(COL, 1);
      if (desp < .2) {
        mono(`${COL.ref} · ${COL.t}`, X(COL.x0) + px(300), Y(COL.y1) - 13, 10.5, rojo());
      }
      ctx.restore();

      /* --- las cotas --- */
      if (f >= 1) {
        const c = f === 1 ? suave(t) : 1;
        const cop = c * (1 - desp);
        if (cop > .01) {
          cotaH(0, MURO, -260, "3600 mm", cop * Math.min(1, c * 3));
          if (c > .3) {
            cotaH(0, 600, -140, "600", cop * Math.min(1, (c - .3) * 4));
            cotaH(600, 1200, -140, "600", cop * Math.min(1, (c - .38) * 4));
            cotaH(1200, 2100, -140, "900", cop * Math.min(1, (c - .46) * 4));
            cotaH(2100, 2700, -140, "600", cop * Math.min(1, (c - .54) * 4));
            cotaH(2700, 3600, -140, "900", cop * Math.min(1, (c - .62) * 4));
          }
          if (c > .55) {
            cotaV(0, 2400, -190, "2400 mm", cop * Math.min(1, (c - .55) * 4));
            cotaV(100, 820, 3760, "720", cop * Math.min(1, (c - .68) * 4));
            cotaV(1450, 2150, 3900, "700", cop * Math.min(1, (c - .78) * 4));
          }
        }
      }

      /* --- el despiece --- */
      if (desp > 0) {
        const cols = 5, cw = (ANCHO - MI - MD) / cols;
        /* Todas a la misma escala entre ellas —no a la del alzado, donde la
           trasera no cabría y el zócalo no se vería— y apoyadas en una misma
           línea de base por fila, como en una hoja de despiece. Centrarlas
           dejaba la trasera comiéndose las filas de arriba y de abajo. */
        const k = 108 / 2400;
        const SUELO = [186, 396];               // la base de cada fila
        PIEZAS.forEach((p, i) => {
          const q = Math.max(0, Math.min(1, desp * 1.5 - i * .045));
          if (q <= 0) return;
          const w = Math.max(10, Math.min(cw - 30, p.b * k * 1.3));
          const h = Math.max(10, p.a * k);
          const fila = Math.floor(i / cols);
          const cx = MI + cw * (i % cols) + cw / 2;
          const cy = SUELO[fila] - h / 2;       // se apoya, no se centra
          /* Salen de dentro de la columna y van a su sitio. */
          const dx = X(COL.x0) + px(300), dy = Y(COL.y1 / 2);
          const ox = dx + (cx - dx) * suave(q), oy = dy + (cy - dy) * suave(q);
          ctx.save();
          ctx.globalAlpha = q;
          ctx.fillStyle = fondo(); ctx.fillRect(ox - w / 2, oy - h / 2, w, h);
          ctx.lineWidth = p.g === 10 ? 1 : 1.4;
          ctx.strokeStyle = p.g === 10 ? flojo() : tinta();
          ctx.strokeRect(ox - w / 2, oy - h / 2, w, h);

          /* En la fase de máquina, lo que la máquina va a hacer:
             el canal de la trasera y los taladros de bisagra. */
          if (maq > 0) {
            ctx.save(); ctx.globalAlpha = q * maq; ctx.strokeStyle = rojo();
            if (/Costado/.test(p.n)) {
              ctx.setLineDash([3, 3]); ctx.lineWidth = 1;
              ctx.beginPath();
              ctx.moveTo(ox + w / 2 - 5, oy - h / 2 + 3); ctx.lineTo(ox + w / 2 - 5, oy + h / 2 - 3);
              ctx.stroke(); ctx.setLineDash([]);
              [-.34, -.1, .16, .38].forEach(f2 => {
                ctx.beginPath(); ctx.arc(ox - w / 2 + 5, oy + h * f2, 2.1, 0, 7); ctx.stroke();
              });
            }
            if (/Puerta/.test(p.n)) {
              [-.3, .3].forEach(f2 => {
                ctx.beginPath(); ctx.arc(ox - w / 2 + 6, oy + h * f2, 3.4, 0, 7); ctx.stroke();
              });
            }
            ctx.restore();
          }
          mono(p.n, ox, oy + h / 2 + 13, 10, flojo());
          mono(`${p.a}×${p.b}×${p.g}`, ox, oy + h / 2 + 26, 9.5, p.g === 10 ? flojo() : tinta());
          ctx.restore();
        });

        if (maq > .25) {
          ctx.save(); ctx.globalAlpha = Math.min(1, (maq - .25) / .4);
          mono("PGMX · Biesse Rover · 10 piezas · 28,0 ml de canto", ANCHO / 2, ALTO - 26, 11, rojo());
          ctx.restore();
        }
      }
    }

    /* ---------- el reloj ---------- */
    function paso(ahora) {
      if (!t0) t0 = ahora;
      const d = ahora - t0;
      const dur = DUR[fase];
      if (d < dur) { avance = d / dur; pinta(fase, avance); }
      else if (d < dur + (fase === 3 ? ESPERA : 0)) { avance = 1; pinta(fase, 1); }
      else { fase = (fase + 1) % 4; t0 = ahora; avance = 0; marca(); pinta(fase, 0); }
      pedido = requestAnimationFrame(paso);
    }
    function marca() {
      $$("#fases i").forEach((n, i) => n.classList.toggle("on", i === fase));
      const r = $("#faseNombre"); if (r) r.textContent = FASES[fase];
    }
    function arranca(desde = 0) {
      cancelAnimationFrame(pedido);
      fase = desde; t0 = 0; corriendo = true; marca();
      pedido = requestAnimationFrame(paso);
    }

    /* En reposo: el alzado acotado, que es lo que la página tiene
       que enseñar en la primera pantalla. La secuencia empieza
       después y solo si a quien mira no le molesta el
       movimiento. */
    fase = 1; avance = 1; marca(); pinta(1, 1);
    if (!quieto) {
      const ojo = new IntersectionObserver(es => {
        es.forEach(e => {
          if (e.isIntersecting && !corriendo) arranca(2);
          else if (!e.isIntersecting && corriendo) { cancelAnimationFrame(pedido); corriendo = false; }
        });
      }, { threshold: .25 });
      ojo.observe(cv);
    }
    const btn = $("#replay");
    if (btn) btn.onclick = () => arranca(0);
  }

  /* ===========================================================
     2 · LA CUOTA
     -----------------------------------------------------------
     La MISMA regla que factura la aplicación. Los cuatro números
     de arriba son el plan; si cambian, cambian aquí y en la base
     —`planes` en supabase/suscripciones.sql— o esta página le
     dice a un cliente un precio que luego no es el suyo.
     ========================================================= */
  const PLAN = { base: 349.99, incluidos: 5, porUsuario: 60, pesoTaller: 0.5, iva: 0.21 };
  const dosDec = n => Math.round(n * 100) / 100;
  const eur = n => n.toLocaleString("es-ES", { style: "currency", currency: "EUR" });

  function cuota(editores, taller) {
    const computables = editores + taller * PLAN.pesoTaller;
    const extra = Math.max(0, computables - PLAN.incluidos);
    const recargo = dosDec(extra * PLAN.porUsuario);
    const base = dosDec(PLAN.base + recargo);
    const ivaImporte = dosDec(base * PLAN.iva);
    return { computables, extra, recargo, base, ivaImporte, total: dosDec(base + ivaImporte) };
  }
  window.ARC_cuota = cuota;   // la usa la prueba

  const calc = $("#calc");
  if (calc) {
    const sE = $("#nEdit"), sT = $("#nTaller");
    const pinta = () => {
      const e = +sE.value, t = +sT.value;
      const c = cuota(e, t);
      $("#vEdit").textContent = e;
      $("#vTaller").textContent = t;
      $("#eEdit").textContent = e === 1 ? "persona" : "personas";
      $("#eTaller").textContent = t === 1 ? "persona" : "personas";
      $("#dBase").textContent = eur(PLAN.base);
      const hayExtra = c.extra > 0;
      $("#filaExtra").hidden = !hayExtra;
      if (hayExtra) {
        $("#dExtra").textContent = eur(c.recargo);
        $("#dExtraNota").textContent =
          `${c.extra.toLocaleString("es-ES")} × ${eur(PLAN.porUsuario)} por encima de ${PLAN.incluidos}`;
      }
      $("#dImponible").textContent = eur(c.base);
      $("#dIva").textContent = eur(c.ivaImporte);
      $("#dTotal").textContent = eur(c.total);
      $("#dQuien").textContent = c.computables.toLocaleString("es-ES");
      $("#dPagina").hidden = !hayExtra;
    };
    [sE, sT].forEach(s => s.addEventListener("input", pinta));
    pinta();
  }

  /* ---------- el año del pie, para no dejarlo caducar ---------- */
  $$("[data-anio]").forEach(n => { n.textContent = new Date().getFullYear(); });
})();
