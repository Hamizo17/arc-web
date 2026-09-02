/* ===========================================================
   ARC · el fondo de la portada
   -----------------------------------------------------------
   Va DETRÁS de todo: detrás del titular y detrás del plano.
   El plano —el alzado que se acota y se despieza— es el que
   cuenta la historia y no se toca; esto es el papel sobre el
   que pasa.

   Son DOS cosas moviéndose en la misma pantalla, y si las dos
   piden atención no gana ninguna: el plano tiene su tarjeta
   blanca y su borde, y el fondo se queda en el margen. Cuánto
   se sube depende del dibujo —una retícula con dos rectas
   aguanta mucho más que un trazo negro cruzando la hoja— y por
   eso la fuerza va junto a la elección, no repartida.

   Se elige con `?fondo=` en la barra de direcciones, para poder
   compararlos sin tocar código:
       ?fondo=0  ninguno      ?fondo=3  cotas
       ?fondo=1  escuadra     ?fondo=4  mecanizado
       ?fondo=2  lápiz        ?fondo=5  mapa de corte

   Nada de lo que se lee depende de esto. Sin JavaScript, con
   «reducir movimiento» puesto o si el lienzo no cabe, la
   portada se ve igual: lo único que se pierde es el papel.
   =========================================================== */
(() => {
  "use strict";
  const cv = document.getElementById("fondoPortada");
  if (!cv) return;
  const ctx = cv.getContext("2d");
  if (!ctx) return;

  const quieto = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const leer = v => getComputedStyle(document.documentElement).getPropertyValue(v).trim() || "#000";

  /* Cuál, y con cuánta fuerza.

     La ESCUADRA: una regla T recorriendo el papel, con sus marcas cada 64 px
     y el cruce señalado en rojo. Es la más callada de las cinco —dos líneas y
     un cruce— y aquí eso es una virtud, no una carencia: en esta pantalla ya
     hay algo moviéndose, el plano, y es el plano el que cuenta la historia.
     Un fondo que compita con él deja a la portada sin foco.

     La fuerza va al 150 %: la escuadra son dos líneas finas y un cruce, y al
     55 % —que era lo prudente cuando se comparaban las cinco— apenas se veía.
     Aquí subir no es gritar: sigue siendo una retícula y dos rectas, y aun al
     150 % la línea más marcada se queda por debajo del borde de la tarjeta
     del plano. Con el lápiz o el mapa de corte este número sería otro.

     Las otras cuatro siguen en el fichero y se prueban con `?fondo=` sin
     tocar nada; cambiar de idea no tiene que costar un despliegue. */
  const ELEGIDO = 1, FUERZA = 1.50;
  const q = new URLSearchParams(location.search).get("fondo");
  const op = q === null ? ELEGIDO : Math.max(0, Math.min(5, +q || 0));
  const fuerza = FUERZA * (+(new URLSearchParams(location.search).get("fuerza") || 100) / 100);
  if (!op) return;

  let W = 0, H = 0;
  function medir() {
    const r = cv.parentElement.getBoundingClientRect();
    const dpr = Math.min(devicePixelRatio || 1, 2);
    W = Math.round(r.width); H = Math.round(r.height);
    if (!W || !H) return false;
    cv.width = W * dpr; cv.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return true;
  }

  /* La retícula del papel milimetrado. En el CSS ya hay una en el `body`;
     ésta la repite dentro del lienzo para que las líneas del fondo caigan
     encima de ella y no al lado. */
  const PASO = 64;
  function reticula(a) {
    ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = leer("--linea"); ctx.lineWidth = 1;
    ctx.beginPath();
    for (let x = 0; x <= W; x += PASO) { ctx.moveTo(x + .5, 0); ctx.lineTo(x + .5, H); }
    for (let y = 0; y <= H; y += PASO) { ctx.moveTo(0, y + .5); ctx.lineTo(W, y + .5); }
    ctx.stroke(); ctx.restore();
  }
  const mono = (t, x, y, tam, col, a) => {
    ctx.save(); ctx.globalAlpha = a; ctx.fillStyle = col;
    ctx.font = tam + 'px "IBM Plex Mono", ui-monospace, monospace';
    ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.fillText(t, x, y); ctx.restore();
  };

  /* ---------- A · la escuadra ---------- */
  function escuadra(t) {
    reticula(.45 * fuerza);
    const x = (Math.sin(t / 9000) * .5 + .5) * W, y = (Math.sin(t / 13000 + 1.7) * .5 + .5) * H;
    ctx.save(); ctx.globalAlpha = .45 * fuerza;
    ctx.strokeStyle = leer("--linea2"); ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.moveTo(x, 0); ctx.lineTo(x, H);
    for (let i = 0; i <= W; i += PASO) { ctx.moveTo(i, y - 4); ctx.lineTo(i, y + 4); }
    for (let i = 0; i <= H; i += PASO) { ctx.moveTo(x - 4, i); ctx.lineTo(x + 4, i); }
    ctx.stroke(); ctx.restore();
    ctx.save(); ctx.globalAlpha = .5 * fuerza; ctx.strokeStyle = leer("--rojo"); ctx.lineWidth = 1.2;
    ctx.beginPath(); ctx.arc(x, y, 7, 0, 7); ctx.stroke(); ctx.restore();
  }

  /* ---------- B · el lápiz ----------
     Tramos rectos, giros de noventa grados y el trazo viejo perdiéndose. El
     olvido no es un adorno: sin él, a los dos minutos el fondo es una maraña
     y el texto deja de leerse. */
  let trazo = [], lapiz = null;
  function reiniciaLapiz() {
    lapiz = { x: Math.round(W * .5 / PASO) * PASO, y: Math.round(H * .5 / PASO) * PASO,
              dir: 0, resta: PASO * 2 };
    trazo = [];
  }
  function lapizPinta(t, dt) {
    reticula(.45 * fuerza);
    if (!lapiz) reiniciaLapiz();
    let avance = 0.075 * dt;                       // px por ms: el paso de una mano
    while (avance > 0) {
      const paso = Math.min(avance, lapiz.resta);
      const dx = [1, 0, -1, 0][lapiz.dir], dy = [0, 1, 0, -1][lapiz.dir];
      const nx = lapiz.x + dx * paso, ny = lapiz.y + dy * paso;
      trazo.push({ x0: lapiz.x, y0: lapiz.y, x1: nx, y1: ny, n: t });
      lapiz.x = nx; lapiz.y = ny; lapiz.resta -= paso; avance -= paso;
      if (lapiz.resta <= 0) {
        const r = Math.random();
        if (r < .42) lapiz.dir = (lapiz.dir + 1) % 4;
        else if (r < .84) lapiz.dir = (lapiz.dir + 3) % 4;
        lapiz.resta = PASO * (1 + Math.floor(Math.random() * 3));
        if (lapiz.x < -PASO || lapiz.x > W + PASO || lapiz.y < -PASO || lapiz.y > H + PASO) {
          lapiz.x = Math.round(Math.random() * W / PASO) * PASO;
          lapiz.y = Math.round(Math.random() * H / PASO) * PASO;
        }
      }
    }
    const VIDA = 9000;
    trazo = trazo.filter(s => t - s.n < VIDA);
    ctx.save(); ctx.strokeStyle = leer("--tinta"); ctx.lineCap = "round"; ctx.lineWidth = 1.6;
    trazo.forEach(s => {
      const e = 1 - (t - s.n) / VIDA;
      ctx.globalAlpha = Math.min(1, e * 1.6) * .26 * fuerza;
      ctx.beginPath(); ctx.moveTo(s.x0, s.y0); ctx.lineTo(s.x1, s.y1); ctx.stroke();
    });
    ctx.restore();
    ctx.save(); ctx.globalAlpha = .6 * fuerza; ctx.fillStyle = leer("--rojo");
    ctx.beginPath(); ctx.arc(lapiz.x, lapiz.y, 2.6, 0, 7); ctx.fill(); ctx.restore();
  }

  /* ---------- C · las cotas ----------
     Los números son de verdad: el cuerpo, la trasera, el canto, el alto de
     un bajo, el tablero. Quien es del oficio los reconoce. */
  const MEDIDAS = ["3600", "2400", "900", "720", "600", "560", "19", "10", "0,8", "40/20", "2850×2100"];
  let cotas = [];
  function cotasPinta(t) {
    reticula(.45 * fuerza);
    if (cotas.length < 4 && Math.random() < .012) {
      const vert = Math.random() < .35, largo = PASO * (2 + Math.floor(Math.random() * 4));
      cotas.push({ vert, n: t, vida: 5200, l: largo,
        x: Math.round(Math.random() * Math.max(0, W - largo) / PASO) * PASO,
        y: Math.round(Math.random() * Math.max(0, H - largo) / PASO) * PASO,
        txt: MEDIDAS[Math.floor(Math.random() * MEDIDAS.length)] });
    }
    cotas = cotas.filter(c => t - c.n < c.vida);
    cotas.forEach(c => {
      const e = (t - c.n) / c.vida;
      const a = (e < .18 ? e / .18 : e > .78 ? (1 - e) / .22 : 1) * .65 * fuerza;
      const L = c.l * Math.min(1, e / .18);        // se traza, no aparece
      ctx.save(); ctx.globalAlpha = a; ctx.strokeStyle = leer("--linea2"); ctx.lineWidth = 1;
      ctx.beginPath();
      if (c.vert) {
        ctx.moveTo(c.x - 5, c.y); ctx.lineTo(c.x + 5, c.y);
        ctx.moveTo(c.x - 5, c.y + c.l); ctx.lineTo(c.x + 5, c.y + c.l);
        ctx.moveTo(c.x, c.y); ctx.lineTo(c.x, c.y + L);
      } else {
        ctx.moveTo(c.x, c.y - 5); ctx.lineTo(c.x, c.y + 5);
        ctx.moveTo(c.x + c.l, c.y - 5); ctx.lineTo(c.x + c.l, c.y + 5);
        ctx.moveTo(c.x, c.y); ctx.lineTo(c.x + L, c.y);
      }
      ctx.stroke(); ctx.restore();
      if (e > .2) mono(c.txt, c.vert ? c.x + 22 : c.x + c.l / 2,
        c.vert ? c.y + c.l / 2 : c.y - 11, 11, leer("--apagado"), a);
    });
  }

  /* ---------- D · el mecanizado ---------- */
  let marcas = [];
  function mecanizado(t) {
    reticula(.45 * fuerza);
    if (marcas.length < 12 && Math.random() < .06) {
      marcas.push({ x: Math.round(Math.random() * W / PASO) * PASO,
        y: Math.round(Math.random() * H / PASO) * PASO,
        tipo: Math.random() < .45 ? "copa" : Math.random() < .6 ? "canal" : "clavija",
        n: t, vida: 4200 + Math.random() * 2600 });
    }
    marcas = marcas.filter(m => t - m.n < m.vida);
    marcas.forEach(m => {
      const e = (t - m.n) / m.vida;
      const a = (e < .12 ? e / .12 : e > .72 ? (1 - e) / .28 : 1) * .5 * fuerza;
      const k = e < .12 ? .6 + .4 * (e / .12) : 1;
      ctx.save(); ctx.globalAlpha = a; ctx.lineWidth = 1.2;
      if (m.tipo === "copa") {
        ctx.strokeStyle = leer("--rojo");
        ctx.beginPath(); ctx.arc(m.x, m.y, 11 * k, 0, 7); ctx.stroke();
        ctx.beginPath(); ctx.arc(m.x, m.y, 2, 0, 7); ctx.stroke();
      } else if (m.tipo === "canal") {
        ctx.strokeStyle = leer("--tinta"); ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(m.x, m.y - PASO * k); ctx.lineTo(m.x, m.y + PASO * k);
        ctx.stroke(); ctx.setLineDash([]);
      } else {
        ctx.strokeStyle = leer("--tinta");
        [-32, 0, 32].forEach(d => { ctx.beginPath(); ctx.arc(m.x + d, m.y, 3 * k, 0, 7); ctx.stroke(); });
      }
      ctx.restore();
    });
  }

  /* ---------- E · el mapa de corte ---------- */
  const PIEZAS = [[2400,560],[2400,560],[562,560],[562,560],[562,540],[562,540],
                  [1190,594],[594,594],[900,720],[900,720],[562,540],[100,596]];
  function mapaCorte(t) {
    reticula(.45 * fuerza);
    const esc = Math.min(W / 1.55 / 2850, H / 1.15 / 2100);
    const bw = 2850 * esc, bh = 2100 * esc, ox = W - bw - 40, oy = H / 2 - bh / 2;
    ctx.save(); ctx.globalAlpha = .3 * fuerza; ctx.strokeStyle = leer("--tinta"); ctx.lineWidth = 1.4;
    ctx.strokeRect(ox, oy, bw, bh); ctx.restore();
    mono("2850 × 2100", ox + bw / 2, oy - 13, 11, leer("--apagado"), .45 * fuerza);
    const CICLO = 15000, e = (t % CICLO) / CICLO, cuantas = Math.floor(e * (PIEZAS.length + 3));
    let cx = 0, cy = 0, altoTira = 0;
    PIEZAS.forEach(([a, b], i) => {
      if (cx + a > 2850) { cx = 0; cy += altoTira + 20; altoTira = 0; }
      if (cy + b <= 2100 && i < cuantas) {
        const q2 = Math.min(1, (e * (PIEZAS.length + 3)) - i);
        ctx.save(); ctx.globalAlpha = Math.min(1, q2 * 2) * .48 * fuerza;
        ctx.strokeStyle = i === cuantas - 1 ? leer("--rojo") : leer("--tinta"); ctx.lineWidth = 1;
        ctx.strokeRect(ox + cx * esc, oy + cy * esc, a * esc * q2, b * esc);
        ctx.restore();
      }
      cx += a + 20; altoTira = Math.max(altoTira, b);
    });
  }

  /* ---------- el reloj ---------- */
  const PINTORES = [null, escuadra, lapizPinta, cotasPinta, mecanizado, mapaCorte];
  const pinta = PINTORES[op];
  let ultimo = 0, pedido = 0, dentro = true;
  function marco(t) {
    const dt = Math.min(60, t - ultimo || 16); ultimo = t;
    ctx.clearRect(0, 0, W, H);
    pinta(t, dt);
    pedido = requestAnimationFrame(marco);
  }
  function arranca() { if (!pedido) { ultimo = 0; pedido = requestAnimationFrame(marco); } }
  function para() { cancelAnimationFrame(pedido); pedido = 0; }

  if (!medir()) return;
  reiniciaLapiz();
  /* En reposo, el primer fotograma. Con «reducir movimiento» se queda ahí:
     hay papel, pero no se mueve nada. */
  pinta(performance.now(), 16);
  if (quieto) return;

  addEventListener("resize", () => { if (medir()) reiniciaLapiz(); }, { passive: true });
  /* Se para sola cuando la pestaña no está delante y cuando la portada se ha
     ido por arriba: nadie tiene que gastar batería en un dibujo que no ve. */
  document.addEventListener("visibilitychange", () =>
    document.hidden ? para() : (dentro && arranca()));
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(es => es.forEach(x => {
      dentro = x.isIntersecting;
      dentro && !document.hidden ? arranca() : para();
    }), { threshold: 0 }).observe(cv.parentElement);
  } else arranca();
})();
