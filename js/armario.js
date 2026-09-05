/* ===========================================================
   ARC · el armario que se despieza al bajar
   -----------------------------------------------------------
   El bloque que va debajo de la portada. Al bajar, un armario
   se abre en sus dieciséis piezas, cada pieza se tumba y enseña
   su mecanizado, y las piezas terminan colocadas en cuatro
   tableros con su programa de máquina al lado.

   Y no es una ilustración. Las medidas, los 248 taladros y la
   colocación en el tablero SALEN DEL NÚCLEO DE ARC ejecutado de
   verdad: `despieceArmario` y `nestTablero` sobre un armario de
   1800 × 600 × 2400 con el perfil de la casa. Están escritos
   abajo como datos porque la web no carga el núcleo —serían
   cientos de kilobytes para dibujar un mueble— pero no hay una
   sola cifra inventada. El día que cambie una holgura del
   perfil, se vuelven a sacar y este armario cambia solo.

   Se dibuja en un canvas y no con imágenes: son 27 KB con los
   datos dentro, se ve nítido en cualquier pantalla y no hay que
   precargar sesenta fotogramas para que el móvil no se atragante.

   Si el bloque no está en la página, esto no hace nada.
   =========================================================== */
if (document.getElementById("armLienzo")) (function () {
const DATOS = {"mueble":{"ancho":1800,"fondo":600,"alto":2400,"grueso":19,"patas":50},"tablero":{"largo":2800,"ancho":2070},"tableros":[{"n":1,"ap":90.4},{"n":2,"ap":71.8},{"n":3,"ap":84.3},{"n":4,"ap":48.8}],"piezas":[{"n":"Techo","l":1800,"w":581,"t":19,"canto":"4 lados","alz":{"x":0,"y":2381,"w":1800,"h":19},"tal":[[50,566.2,5],[617,566.2,5],[1183,566.2,5],[1750,566.2,5],[14.8,37,5],[14.8,281,5],[14.8,524,5],[905.3,37,5],[905.3,281,5],[905.3,524,5],[1785.2,37,5],[1785.2,281,5],[1785.2,524,5]],"nest":{"tb":3,"x":0,"y":909,"l":1800,"a":581,"g":false}},{"n":"Suelo","l":1800,"w":581,"t":19,"canto":"4 lados","alz":{"x":0,"y":50,"w":1800,"h":19},"tal":[[50,566.2,5],[617,566.2,5],[1183,566.2,5],[1750,566.2,5],[14.8,37,5],[14.8,281,5],[14.8,524,5],[905.3,37,5],[905.3,281,5],[905.3,524,5],[1785.2,37,5],[1785.2,281,5],[1785.2,524,5]],"nest":{"tb":4,"x":0,"y":573,"l":1800,"a":581,"g":false}},{"n":"Lateral izq","l":561,"w":2312,"t":19,"canto":"Canto izquierdo","alz":{"x":0,"y":69,"w":19,"h":2312},"tal":[[37,2308.4,15],[37,2297.2,15],[37,2286,15],[281,2308.4,15],[281,2297.2,15],[281,2286,15],[524,2308.4,15],[524,2297.2,15],[524,2286,15],[37,3.6,15],[37,14.8,15],[37,26,15],[281,3.6,15],[281,14.8,15],[281,26,15],[524,3.6,15],[524,14.8,15],[524,26,15],[557.4,2232,15],[546.2,2232,15],[535,2232,15],[557.4,1515,15],[546.2,1515,15],[535,1515,15],[557.4,797,15],[546.2,797,15],[535,797,15],[557.4,80,15],[546.2,80,15],[535,80,15],[37,1636.3,5],[281,1636.3,5],[524,1636.3,5],[37,1936.3,5],[281,1936.3,5],[524,1936.3,5]],"nest":{"tb":1,"x":0,"y":1482,"l":2312,"a":561,"g":true}},{"n":"Lateral der","l":561,"w":2312,"t":19,"canto":"Canto izquierdo","alz":{"x":1781,"y":69,"w":19,"h":2312},"tal":[[37,2308.4,15],[37,2297.2,15],[37,2286,15],[281,2308.4,15],[281,2297.2,15],[281,2286,15],[524,2308.4,15],[524,2297.2,15],[524,2286,15],[37,3.6,15],[37,14.8,15],[37,26,15],[281,3.6,15],[281,14.8,15],[281,26,15],[524,3.6,15],[524,14.8,15],[524,26,15],[557.4,2232,15],[546.2,2232,15],[535,2232,15],[557.4,1515,15],[546.2,1515,15],[535,1515,15],[557.4,797,15],[546.2,797,15],[535,797,15],[557.4,80,15],[546.2,80,15],[535,80,15],[37,1136.3,5],[281,1136.3,5],[524,1136.3,5]],"nest":{"tb":1,"x":0,"y":0,"l":2312,"a":561,"g":true}},{"n":"Divisor 1","l":561,"w":2312,"t":19,"canto":"Canto izquierdo","alz":{"x":890.5,"y":69,"w":19,"h":2312},"tal":[[37,2308.4,15],[37,2297.2,15],[37,2286,15],[281,2308.4,15],[281,2297.2,15],[281,2286,15],[524,2308.4,15],[524,2297.2,15],[524,2286,15],[37,3.6,15],[37,14.8,15],[37,26,15],[281,3.6,15],[281,14.8,15],[281,26,15],[524,3.6,15],[524,14.8,15],[524,26,15],[557.4,2232,15],[546.2,2232,15],[535,2232,15],[557.4,1515,15],[546.2,1515,15],[535,1515,15],[557.4,797,15],[546.2,797,15],[535,797,15],[557.4,80,15],[546.2,80,15],[535,80,15],[37,1636.3,5],[281,1636.3,5],[524,1636.3,5],[37,1936.3,5],[281,1936.3,5],[524,1936.3,5],[37,1136.3,5],[281,1136.3,5],[524,1136.3,5]],"nest":{"tb":4,"x":0,"y":0,"l":2312,"a":561,"g":true}},{"n":"Balda 1","l":871.5,"w":556,"t":19,"canto":"Canto de arriba","alz":{"x":19,"y":1690.5,"w":871.5,"h":19},"tal":[[3.6,524,15],[14.8,524,15],[26,524,15],[3.6,280,15],[14.8,280,15],[26,280,15],[3.6,37,15],[14.8,37,15],[26,37,15],[867.9,524,15],[856.7,524,15],[845.5,524,15],[867.9,280,15],[856.7,280,15],[845.5,280,15],[867.9,37,15],[856.7,37,15],[845.5,37,15]],"nest":{"tb":3,"x":1812,"y":1477,"l":872,"a":556,"g":false}},{"n":"Balda 2","l":871.5,"w":556,"t":19,"canto":"Canto de arriba","alz":{"x":19,"y":1990.5,"w":871.5,"h":19},"tal":[[3.6,524,15],[14.8,524,15],[26,524,15],[3.6,280,15],[14.8,280,15],[26,280,15],[3.6,37,15],[14.8,37,15],[26,37,15],[867.9,524,15],[856.7,524,15],[845.5,524,15],[867.9,280,15],[856.7,280,15],[845.5,280,15],[867.9,37,15],[856.7,37,15],[845.5,37,15]],"nest":{"tb":4,"x":0,"y":1166,"l":556,"a":872,"g":true}},{"n":"Balda 3","l":871.5,"w":556,"t":19,"canto":"Canto de arriba","alz":{"x":909.5,"y":1190.5,"w":871.5,"h":19},"tal":[[3.6,524,15],[14.8,524,15],[26,524,15],[3.6,280,15],[14.8,280,15],[26,280,15],[3.6,37,15],[14.8,37,15],[26,37,15],[867.9,524,15],[856.7,524,15],[845.5,524,15],[867.9,280,15],[856.7,280,15],[845.5,280,15],[867.9,37,15],[856.7,37,15],[845.5,37,15]],"nest":{"tb":3,"x":1812,"y":909,"l":872,"a":556,"g":false}},{"n":"Lateral porta-guias bloque 1 izquierdo","l":510,"w":710,"t":19,"canto":"Canto izquierdo","alz":{"x":909.5,"y":300,"w":19,"h":710},"tal":[],"nest":{"tb":3,"x":0,"y":1502,"l":710,"a":510,"g":true}},{"n":"Lateral porta-guias bloque 1 derecho","l":510,"w":710,"t":19,"canto":"Canto izquierdo","alz":{"x":1762,"y":300,"w":19,"h":710},"tal":[],"nest":{"tb":3,"x":722,"y":1502,"l":710,"a":510,"g":true}},{"n":"Frente cajon 1","l":818,"w":180,"t":19,"canto":"4 lados","alz":{"x":931.5,"y":310,"w":818,"h":180},"tal":[],"nest":{"tb":1,"x":2402,"y":830,"l":180,"a":818,"g":true}},{"n":"Frente cajon 2","l":818,"w":180,"t":19,"canto":"4 lados","alz":{"x":931.5,"y":520,"w":818,"h":180},"tal":[],"nest":{"tb":1,"x":2594,"y":830,"l":180,"a":818,"g":true}},{"n":"Frente cajon 3","l":818,"w":250,"t":19,"canto":"4 lados","alz":{"x":931.5,"y":725,"w":818,"h":250},"tal":[],"nest":{"tb":1,"x":2402,"y":0,"l":250,"a":818,"g":true}},{"n":"Puerta 1 hoja izq","l":897,"w":2390,"t":19,"canto":"4 lados","alz":{"x":1.5,"y":10,"w":897,"h":2390},"tal":[[28,125,35],[37.5,102.5,5],[37.5,147.5,5],[28,838,35],[37.5,815.5,5],[37.5,860.5,5],[28,1552,35],[37.5,1529.5,5],[37.5,1574.5,5],[28,2265,35],[37.5,2242.5,5],[37.5,2287.5,5]],"nest":{"tb":3,"x":0,"y":0,"l":2390,"a":897,"g":true}},{"n":"Puerta 2 hoja der","l":897,"w":2390,"t":19,"canto":"4 lados","alz":{"x":901.5,"y":10,"w":897,"h":2390},"tal":[[869,125,35],[859.5,102.5,5],[859.5,147.5,5],[869,838,35],[859.5,815.5,5],[859.5,860.5,5],[869,1552,35],[859.5,1529.5,5],[859.5,1574.5,5],[869,2265,35],[859.5,2242.5,5],[859.5,2287.5,5]],"nest":{"tb":1,"x":0,"y":573,"l":2390,"a":897,"g":true}},{"n":"Trasera","l":1800,"w":2312,"t":19,"canto":"—","alz":{"x":0,"y":69,"w":1800,"h":2312},"tal":[[50,2308.4,15],[50,2297.2,15],[50,2286,15],[50,3.6,15],[50,14.8,15],[50,26,15],[617,2308.4,15],[617,2297.2,15],[617,2286,15],[617,3.6,15],[617,14.8,15],[617,26,15],[1183,2308.4,15],[1183,2297.2,15],[1183,2286,15],[1183,3.6,15],[1183,14.8,15],[1183,26,15],[1750,2308.4,15],[1750,2297.2,15],[1750,2286,15],[1750,3.6,15],[1750,14.8,15],[1750,26,15],[14.8,2232,5],[14.8,1515,5],[14.8,797,5],[14.8,80,5],[1785.2,2232,5],[1785.2,1515,5],[1785.2,797,5],[1785.2,80,5],[905.3,2232,5],[905.3,1515,5],[905.3,797,5],[905.3,80,5]],"nest":{"tb":2,"x":0,"y":0,"l":2312,"a":1800,"g":true}}]};

/* ═══════════════════════════════════════════════════════════
   ARC · el armario que se despieza al bajar
   -----------------------------------------------------------
   Cuatro estados, y la pieza pasa por los cuatro:

     0  MONTADA      cada pieza es una caja en su sitio
     1  DESPIEZADA   la misma caja, apartada
     2  TUMBADA      la caja pierde el fondo y gira: se ve su
                     cara de verdad, con sus taladros
     3  EN EL TABLERO donde la pone la optimización

   Lo que se interpola son SEIS NÚMEROS por pieza —x, y, z,
   ancho, alto, fondo— y no rectángulos de pantalla. Por eso el
   paso de 2 a 3 no es un truco: el fondo se va a cero y el
   ancho crece hasta la cara real, que es exactamente lo que
   hace una pieza cuando la tumbas en la mesa.

   La proyección es una axonométrica de gabinete: lo que está
   más al fondo se dibuja más a la derecha y más arriba. No es
   3D de verdad —no hay cámara ni luces— y no hace falta: un
   armario son cajas rectas.
   ═══════════════════════════════════════════════════════════ */

const P = DATOS.piezas, MU = DATOS.mueble, TB = DATOS.tablero;

/* ---------- de cada pieza, su caja ----------
   El alzado da ancho y alto. El fondo es la medida de la pieza que el alzado
   NO enseña: un lateral de 561 × 2312 sale en el alzado como 19 × 2312, así
   que su fondo son 561. */
const casi = (a, b) => Math.abs(a - b) < 1.5;
function fondoDe(p){
  const r = p.alz;
  const dims = [p.l, p.w, p.t];
  const libre = dims.filter(d => !casi(d, r.w) && !casi(d, r.h));
  return libre.length ? libre[0] : p.t;
}
/* A qué profundidad empieza. La hoja va POR DELANTE de la caja, la trasera por
   detrás y la balda un poco metida: son los cinco milímetros de retranqueo. */
function zDe(p){
  if (/Puerta/.test(p.n)) return -p.t;
  if (p.n === "Trasera")  return MU.fondo - 19 - p.t;
  if (/^Balda/.test(p.n)) return 5;
  if (/porta-guias/.test(p.n)) return 20;
  return 0;
}
/* Hacia dónde se aparta al despiezarse. A mano y no con un radial desde el
   centro: un radial manda el divisor y la trasera al mismo sitio, y esto tiene
   que leerse como un despiece, no como unos fuegos artificiales. */
const FUERA = {
  "Techo":            [0, 1.05, 0],
  "Suelo":            [0, -1.05, 0],
  "Lateral izq":      [-1.15, 0, 0],
  "Lateral der":      [1.15, 0, 0],
  "Divisor 1":        [0.05, 0.55, 0],
  "Balda 1":          [-0.72, 0.06, 0],
  "Balda 2":          [-0.72, -0.14, 0],
  "Balda 3":          [0.72, 0.06, 0],
  "Frente cajon 1":   [0.62, -0.34, -1.5],
  "Frente cajon 2":   [0.62, -0.50, -1.5],
  "Frente cajon 3":   [0.62, -0.66, -1.5],
  "Puerta 1 hoja izq":[-1.55, 0, -2.6],
  "Puerta 2 hoja der":[1.55, 0, -2.6],
  "Trasera":          [0.35, 0.30, 1.5],
  "Lateral porta-guias bloque 1 izquierdo": [0.30, -0.60, 0],
  "Lateral porta-guias bloque 1 derecho":   [0.58, -0.60, 0],
};
const SALTO = 430;

const MONTADA = P.map(p => ({ x: p.alz.x, y: p.alz.y, z: zDe(p),
                              w: p.alz.w, h: p.alz.h, d: fondoDe(p) }));
const APARTE = P.map((p, i) => {
  const f = FUERA[p.n] || [0, 0, 0], m = MONTADA[i];
  return { x: m.x + f[0] * SALTO, y: m.y + f[1] * SALTO, z: m.z + f[2] * SALTO,
           w: m.w, h: m.h, d: m.d };
});

/* ---------- tumbadas ----------
   En filas, por alto, como se dejan en una mesa. Ya sin fondo: lo que se ve es
   la cara que va a mecanizar la máquina. */
function tumbadas(){
  const orden = P.map((p, i) => ({ i, l: p.l, a: p.w })).sort((a, b) => b.a - a.a || b.l - a.l);
  const ANCHO = 6600, HUECO = 110;
  const out = new Array(P.length);
  let x = 0, y = 0, fila = 0;
  orden.forEach(o => {
    if (x + o.l > ANCHO && x > 0) { x = 0; y -= fila + HUECO; fila = 0; }
    out[o.i] = { x, y: y - o.a, z: 0, w: o.l, h: o.a, d: 0 };
    x += o.l + HUECO;
    fila = Math.max(fila, o.a);
  });
  return out;
}
const TUMBADA = tumbadas();

/* ---------- en el tablero ----------
   Los cuatro tableros en dos columnas, y cada pieza donde la ha puesto la
   optimización, con su giro: una pieza girada va tumbada, que es como la
   corta la máquina. */
const SEP = 300;
const ENTABLERO = P.map(p => {
  const n = p.nest ? p.nest.tb - 1 : 0;
  const bx = (n % 2) * (TB.largo + SEP), by = -Math.floor(n / 2) * (TB.ancho + SEP);
  const q = p.nest || { x: 0, y: 0, l: p.l, a: p.w };
  return { x: bx + q.x, y: by - q.y - q.a, z: 0, w: q.l, h: q.a, d: 0,
           girada: !!(p.nest && p.nest.g) };
});
const CAJAS = [MONTADA, APARTE, TUMBADA, ENTABLERO];

/* ---------- la proyección ---------- */
const AX = 0.42, AY = 0.24;
const proy = (x, y, z) => [x + z * AX, -(y + z * AY)];


const cv = document.getElementById("armLienzo");
const cx = cv.getContext("2d");
let AN = 0, AL = 0, DPR = 1, MONO = "IBM Plex Mono, monospace";

function mide(){
  DPR = Math.min(2, window.devicePixelRatio || 1);
  const r = cv.getBoundingClientRect();
  AN = Math.max(1, Math.round(r.width)); AL = Math.max(1, Math.round(r.height));
  cv.width = Math.round(AN * DPR); cv.height = Math.round(AL * DPR);
  cx.setTransform(DPR, 0, 0, DPR, 0, 0);
  MONO = (getComputedStyle(document.body).getPropertyValue("--mono") || "monospace").trim();
}

/* La cámara NO es la de un estado: se calcula en cada fotograma con lo que hay
   de verdad en pantalla en ese momento.

   Encuadrar por estados parecía más barato y está mal: las piezas salen
   escalonadas, así que a mitad del despiece la hoja ya está fuera y el encuadre
   todavía es el del mueble montado — y la hoja se sale del papel. Y en un móvil
   estrecho se sale siempre. Midiendo lo que hay, no se puede salir nada. */
function encuadre(cajas, k){
  let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  cajas.forEach(c => {
    for (const dx of [0, c.w]) for (const dy of [0, c.h]) for (const dz of [0, c.d]) {
      const q = proy(c.x + dx, c.y + dy, c.z + dz);
      if (q[0] < x0) x0 = q[0]; if (q[0] > x1) x1 = q[0];
      if (q[1] < y0) y0 = q[1]; if (q[1] > y1) y1 = q[1];
    }
  });
  const m = .04 * Math.max(x1 - x0, y1 - y0);
  const M = { x0: x0 - m, y0: y0 - m, x1: x1 + m, y1: y1 + m };
  const ancho = AN > 860;
  /* Sitio para el rótulo, para el carril de fases y —en la primera— para las
     cotas, que se dibujan por fuera de la pieza. */
  const cota = k === 0 ? 52 : 0;
  const izq = (ancho ? Math.min(AN * .32, 400) : 0) + cota;
  const der = (ancho ? 185 : 14);
  const arr = (ancho ? 24 : 74) + cota;
  const aba = (ancho ? 24 : 210) + cota;
  const w = Math.max(40, AN - izq - der), h = Math.max(40, AL - arr - aba);
  const s = Math.min(w / (M.x1 - M.x0), h / (M.y1 - M.y0));
  return { s, M, ox: izq + (w - (M.x1 - M.x0) * s) / 2, oy: arr + (h - (M.y1 - M.y0) * s) / 2 };
}
const mez = (a, b, t) => a + (b - a) * t;
const clamp = (v, a, b) => v < a ? a : v > b ? b : v;
const tramo = (p, a, b) => clamp((p - a) / (b - a), 0, 1);
/* Smootherstep: 6t^5 - 15t^4 + 10t^3. Arranca y para con velocidad CERO y
   además con aceleración cero, que es la diferencia entre «se mueve» y «se
   desliza». La cúbica de antes paraba en seco: su aceleración da un salto al
   final y el ojo lo lee como un tirón, aunque no sepa por qué. */
const suave = t => t * t * t * (t * (t * 6 - 15) + 10);
const pt = (cam, x, y, z) => { const q = proy(x, y, z);
  return [cam.ox + (q[0] - cam.M.x0) * cam.s, cam.oy + (q[1] - cam.M.y0) * cam.s]; };

/* ---------- las cinco fases ---------- */
const FASES = [
  { n: "Alzado", t: "El alzado",
    d: "Un armario de 1800 × 600 × 2400. Es lo único que se dibuja: todo lo demás se deduce de aquí." },
  { n: "Despiece", t: "Se abre",
    d: "Dieciséis piezas con su medida de corte. El divisor de 19, las baldas al hueco exacto, las dos hojas repartiéndose el frente." },
  { n: "Mecanizado", t: "Y enseña la cara",
    d: "Cada pieza tumbada como la ve la máquina, con sus 248 taladros: Ø15 del cabineo, Ø5 del casquillo y Ø35 de la cazoleta." },
  { n: "Optimización", t: "Se coloca en el tablero",
    d: "Cuatro tableros de 2800 × 2070, con la fresa de 12 y el refile de 10. El primero aprovecha el 90,4 %." },
  { n: "CNC", t: "Y sale el programa",
    d: "El mismo modelo, ya en coordenadas de máquina. Sin volver a medir nada, sin volver a teclear nada." },
];
/* ---------- LA LÍNEA DE TIEMPO ----------
   Dos cosas distintas, y antes eran una sola:

     LIM     dónde empieza cada FASE. Es lo que enciende el carril y cambia
             el rótulo.
     TRAMOS  dónde se MUEVE cada pieza. Ocupa solo una parte de su fase.

   Confundirlas es lo que hacía que esto pareciera un vídeo acelerado: cada
   movimiento empezaba justo donde acababa el anterior, así que no había un
   solo momento en el que el armario estuviera quieto y se pudiera mirar. Ahora
   cada fase se mueve durante su tramo y SE QUEDA PARADA el resto —entre un
   tercio y un cuarto de la fase—, que es cuando se leen las medidas. */
const LIM = [0, .10, .38, .62, .84, 1];
const TRAMOS = [
  { de: .10, a: .32 },   // el mueble se abre
  { de: .38, a: .56 },   // las piezas se tumban y enseñan el mecanizado
  { de: .62, a: .78 },   // y se colocan en el tablero
];

const carril = document.getElementById("armCarril");
FASES.forEach((f, i) => {
  const d = document.createElement("div");
  d.innerHTML = "<b>0" + (i + 1) + "</b><span>" + f.n + "</span>";
  carril.appendChild(d);
});
const casillas = [...carril.children];
const $ = id => document.getElementById(id);
const rNum = $("armNum"), rTit = $("armTit"), rTxt = $("armTxt"), pista = $("armPista");
const cPiezas = $("armPiezas"), cM2 = $("armM2"), cTal = $("armTal");

const M2 = P.reduce((s, p) => s + p.l * p.w, 0) / 1e6;
const NTAL = P.reduce((s, p) => s + p.tal.length, 0);
const num = (v, d) => v.toLocaleString("es-ES", { minimumFractionDigits: d, maximumFractionDigits: d });

let faseVista = -1;
function rotulo(i){
  if (i === faseVista) return;
  faseVista = i;
  const f = FASES[i];
  rNum.textContent = "0" + (i + 1) + " / 05";
  [rTit, rTxt].forEach(n => { n.style.opacity = 0; n.style.transform = "translateY(8px)"; });
  setTimeout(() => {
    rTit.textContent = f.t; rTxt.textContent = f.d;
    [rTit, rTxt].forEach(n => { n.style.opacity = 1; n.style.transform = "none"; });
  }, 260);
  casillas.forEach((c, k) => { c.classList.toggle("on", k === i); c.classList.toggle("hecha", k < i); });
}

/* ═══════════════════════════════════════════════════════════
   Dibujar
   ═══════════════════════════════════════════════════════════ */
const TINTA = "#100E0D", APAG = "#6B645E", LIN = "#C3BBB3", ROJO = "#E00F16";

/* Las piezas se apartan UNA DETRÁS DE OTRA, no todas a la vez: un despiece que
   estalla de golpe no se lee. El retardo va por el orden en que se monta el
   mueble, que es el orden en que se desmonta al revés. */
const SALIDA = ["Puerta 1 hoja izq", "Puerta 2 hoja der", "Frente cajon 3", "Frente cajon 2",
  "Frente cajon 1", "Balda 3", "Balda 2", "Balda 1",
  "Lateral porta-guias bloque 1 derecho", "Lateral porta-guias bloque 1 izquierdo",
  "Divisor 1", "Trasera", "Techo", "Suelo", "Lateral der", "Lateral izq"];
const TURNO = P.map(p => { const k = SALIDA.indexOf(p.n); return (k < 0 ? 0 : k) / SALIDA.length; });
/* Cuánto del tramo se gasta en escalonar. Con .62 la última pieza arranca
   cuando la primera lleva casi dos tercios del camino: el mueble se abre como
   se desmonta, y no como estalla. */
const RETARDO = .62;

function faseDe(p){
  for (let k = 0; k < TRAMOS.length; k++) {
    if (p < TRAMOS[k].de) return [k, 0];
    if (p <= TRAMOS[k].a)  return [k, tramo(p, TRAMOS[k].de, TRAMOS[k].a)];
  }
  return [3, 0];
}

function pinta(p){
  cx.clearRect(0, 0, AN, AL);
  const [k, t] = faseDe(p);

  const vTab = k === 2 ? tramo(t, 0, .30) : (k === 3 ? 1 : 0);
  const vCota = 1 - tramo(p, TRAMOS[0].de - .04, TRAMOS[0].de + .05);
  const vTal = k === 1 ? tramo(t, .50, 1) : (k >= 2 ? 1 : 0);
  const vRot = k === 0 ? tramo(t, .22, .55) : (k === 1 ? 1 : k === 2 ? 1 - suave(t) * .5 : .5);


  /* Dónde está cada pieza AHORA. Las piezas salen escalonadas: la hoja primero
     y el lateral el último, porque un despiece que estalla de golpe no se lee. */
  const est = P.map((pieza, i) => {
    const a = CAJAS[k][i], b = CAJAS[Math.min(3, k + 1)][i];
    let u = suave(t);
    if (k === 0) u = suave(clamp((t - TURNO[i] * RETARDO) / (1 - RETARDO), 0, 1));
    return { i, x: mez(a.x, b.x, u), y: mez(a.y, b.y, u), z: mez(a.z, b.z, u),
             w: mez(a.w, b.w, u), h: mez(a.h, b.h, u), d: mez(a.d, b.d, u), u };
  });
  /* El encuadre, con lo que hay: las piezas y, cuando asoma, el tablero. */
  const paraEncuadrar = est.slice();
  if (vTab > .01) DATOS.tableros.forEach((tb, n) => {
    paraEncuadrar.push({ x: (n % 2) * (TB.largo + SEP),
                         y: -Math.floor(n / 2) * (TB.ancho + SEP) - TB.ancho,
                         z: 0, w: TB.largo, h: TB.ancho, d: 0 });
  });
  const cam = encuadre(paraEncuadrar, k);

  cx.save();
  if (vTab > .01) tableros(cam, vTab);
  if (vCota > .01) cotas(cam, vCota);

  /* De atrás hacia delante: la hoja que sale hacia delante pasa por encima. */
  est.sort((a, b) => (b.z + b.d) - (a.z + a.d) || a.y - b.y);
  est.forEach(e => caja(P[e.i], e, cam, vTal, vRot));
  cx.restore();

  if (p >= LIM[4]) codigo(tramo(p, LIM[4], LIM[4] + .05));
  contadores(p, k, t);
}

function caja(pieza, e, cam, vTal, vRot){
  const esFrente = /Puerta|Frente/.test(pieza.n), esTrasera = pieza.n === "Trasera";
  const A0 = pt(cam, e.x, e.y, e.z), A1 = pt(cam, e.x + e.w, e.y, e.z),
        A2 = pt(cam, e.x + e.w, e.y + e.h, e.z), A3 = pt(cam, e.x, e.y + e.h, e.z);
  const anchoPx = Math.hypot(A1[0] - A0[0], A1[1] - A0[1]);
  const altoPx  = Math.hypot(A3[0] - A0[0], A3[1] - A0[1]);
  if (anchoPx < .4 && altoPx < .4) return;

  cx.save();
  cx.lineJoin = "round";
  /* Las dos caras que da la profundidad: la de arriba y la del costado. Se
     dibujan más apagadas, que es lo que hace que se lea el volumen. */
  if (e.d > .5) {
    const B3 = pt(cam, e.x, e.y + e.h, e.z + e.d), B2 = pt(cam, e.x + e.w, e.y + e.h, e.z + e.d),
          B1 = pt(cam, e.x + e.w, e.y, e.z + e.d);
    quad(A3, A2, B2, B3, "rgba(16,14,13,.10)", "rgba(16,14,13,.30)");
    quad(A1, A2, B2, B1, "rgba(16,14,13,.06)", "rgba(16,14,13,.26)");
  }
  /* Con el mueble montado la hoja tapa el armario entero, y un armario que se
     ve por fuera no enseña nada: hasta que no se separa, la hoja es solo su
     contorno. `e.u` es lo que lleva recorrido hacia su sitio. */
  const abre = /Puerta/.test(pieza.n) ? clamp(e.u * 2.2, 0, 1) : 1;
  quad(A0, A1, A2, A3,
    esFrente ? "rgba(224,15,22," + (.10 * abre).toFixed(3) + ")"
             : esTrasera ? "rgba(16,14,13,.02)" : "rgba(16,14,13,.05)",
    esFrente ? "rgba(224,15,22,.60)" : "rgba(16,14,13,.45)", esTrasera);

  /* Los taladros, cuando la pieza ya enseña su cara. */
  if (vTal > .01 && pieza.tal.length && anchoPx > 24 && altoPx > 24) {
    const gir = (e.w > e.h) !== (pieza.l > pieza.w);
    const sx = e.w / (gir ? pieza.w : pieza.l), sy = e.h / (gir ? pieza.l : pieza.w);
    cx.globalAlpha = vTal;
    cx.fillStyle = "rgba(224,15,22,.8)";
    pieza.tal.forEach(hh => {
      const hx = gir ? hh[1] : hh[0], hy = gir ? hh[0] : hh[1];
      const q = pt(cam, e.x + hx * sx, e.y + hy * sy, e.z);
      const r = Math.max(1, hh[2] * cam.s * .5);
      cx.beginPath(); cx.arc(q[0], q[1], r, 0, 6.2832); cx.fill();
    });
    cx.globalAlpha = 1;
  }

  /* El rótulo, si hay sitio para leerlo. */
  /* El rótulo se mide en píxeles de pantalla, no en milímetros: en un móvil
     el mismo armario se dibuja a un tercio y un nombre de 11 px encima de una
     balda de 40 tapa la balda. */
  const tam = AN > 860 ? 11 : 9.5, minAncho = AN > 860 ? 96 : 78;
  if (vRot > .02 && anchoPx > minAncho && altoPx > tam * 2.6) {
    cx.globalAlpha = clamp((anchoPx - minAncho) / 50, 0, 1) * vRot;
    cx.font = "500 " + tam + "px " + MONO;
    cx.textBaseline = "top";
    const nom = pieza.n.replace("Lateral porta-guias bloque 1", "Porta-guías");
    const med = num(pieza.l, 0) + " × " + num(pieza.w, 0) + " × " + pieza.t;
    /* Se abre hueco debajo: un nombre sobre una pieza translúcida encima de
       otra pieza no se lee, y lo que hay que leer es la medida. */
    const anc = Math.max(cx.measureText(nom).width, cx.measureText(med).width) + 10;
    cx.save(); cx.globalCompositeOperation = "destination-out";
    cx.fillRect(A3[0] + 4, A3[1] + 4, anc, tam * 2.7); cx.restore();
    cx.fillStyle = TINTA; cx.fillText(nom, A3[0] + 7, A3[1] + 6);
    cx.fillStyle = APAG; cx.fillText(med, A3[0] + 7, A3[1] + 6 + tam * 1.25);
    cx.globalAlpha = 1;
  }
  cx.restore();

  function quad(a, b, c, d, relleno, borde, discontinuo){
    cx.beginPath();
    cx.moveTo(a[0], a[1]); cx.lineTo(b[0], b[1]); cx.lineTo(c[0], c[1]); cx.lineTo(d[0], d[1]);
    cx.closePath();
    cx.fillStyle = relleno; cx.fill();
    cx.lineWidth = 1; cx.strokeStyle = borde;
    if (discontinuo) cx.setLineDash([5, 4]);
    cx.stroke();
    cx.setLineDash([]);
  }
}

function tableros(cam, v){
  cx.save(); cx.globalAlpha = v;
  cx.font = "400 11px " + MONO; cx.textBaseline = "bottom";
  DATOS.tableros.forEach((t, n) => {
    const bx = (n % 2) * (TB.largo + SEP), by = -Math.floor(n / 2) * (TB.ancho + SEP);
    const a = pt(cam, bx, by - TB.ancho, 0), b = pt(cam, bx + TB.largo, by, 0);
    cx.fillStyle = "rgba(16,14,13,.028)";
    cx.fillRect(a[0], b[1], b[0] - a[0], a[1] - b[1]);
    cx.strokeStyle = LIN; cx.lineWidth = 1;
    cx.strokeRect(Math.round(a[0]) + .5, Math.round(b[1]) + .5,
                  Math.round(b[0] - a[0]), Math.round(a[1] - b[1]));
    cx.fillStyle = APAG;
    cx.fillText("TABLERO " + t.n + " · 2800 × 2070 · " + num(t.ap, 1) + " %", a[0], b[1] - 7);
  });
  cx.restore();
}

function cotas(cam, v){
  cx.save(); cx.globalAlpha = v;
  cx.strokeStyle = ROJO; cx.fillStyle = ROJO; cx.lineWidth = 1;
  cx.font = "400 11px " + MONO;
  const ai = pt(cam, 0, 0, 0), ad = pt(cam, MU.ancho, 0, 0), ar = pt(cam, MU.ancho, MU.alto, 0);
  raya(ai[0], ai[1] + 30, ad[0], ad[1] + 30, false);
  texto(num(MU.ancho, 0) + " mm", (ai[0] + ad[0]) / 2, ai[1] + 25);
  const ai2 = pt(cam, 0, MU.alto, 0);
  raya(ai[0] - 34, ai[1], ai2[0] - 34, ai2[1], true);
  cx.save(); cx.translate(ai[0] - 39, (ai[1] + ai2[1]) / 2); cx.rotate(-Math.PI / 2);
  texto(num(MU.alto, 0) + " mm", 0, 0); cx.restore();
  cx.restore();

  function raya(x0, y0, x1, y1, vert){
    cx.beginPath(); cx.moveTo(x0, y0); cx.lineTo(x1, y1); cx.stroke();
    cx.beginPath();
    if (vert) { cx.moveTo(x0 - 6, y0); cx.lineTo(x0 + 6, y0); cx.moveTo(x1 - 6, y1); cx.lineTo(x1 + 6, y1); }
    else      { cx.moveTo(x0, y0 - 6); cx.lineTo(x0, y0 + 6); cx.moveTo(x1, y1 - 6); cx.lineTo(x1, y1 + 6); }
    cx.stroke();
  }
  function texto(txt, x, y){
    cx.textAlign = "center"; cx.textBaseline = "bottom";
    const w = cx.measureText(txt).width + 12;
    cx.save(); cx.globalCompositeOperation = "destination-out";
    cx.fillRect(x - w / 2, y - 12, w, 15); cx.restore();
    cx.fillStyle = ROJO; cx.fillText(txt, x, y); cx.textAlign = "left";
  }
}

/* Las primeras líneas del programa, con coordenadas de verdad: las de los
   taladros de la primera pieza que los lleva. */
let LINEAS = null;
function codigo(v){
  if (!LINEAS) {
    const pz = P.find(x => x.tal.length);
    LINEAS = ["; ARC · " + pz.n.toUpperCase(), "; PANEL L=" + pz.l + " W=" + pz.w + " T=" + pz.t]
      .concat(pz.tal.slice(0, 8).map(h => "BG X=" + num(h[0], 1) + " Y=" + num(h[1], 1) + " D=" + h[2] + " P=11"))
      .concat(["; ...", "; " + NTAL + " taladros · 16 piezas · 4 tableros"]);
  }
  /* En la columna del rótulo, que está vacía, y no encima de los tableros: un
     recuadro tapando el patrón de corte es justo lo que no se quiere enseñar. */
  const ancho = AN > 860;
  const an = ancho ? Math.min(330, AN * .30) : AN - 40;
  const x = ancho ? 54 : 20, y = ancho ? AL * .46 : AL * .20;
  cx.save(); cx.globalAlpha = v;
  cx.fillStyle = "rgba(244,241,237,.95)";
  cx.fillRect(x - 16, y - 24, an, LINEAS.length * 19 + 32);
  cx.strokeStyle = LIN; cx.lineWidth = 1;
  cx.strokeRect(Math.round(x - 16) + .5, Math.round(y - 24) + .5, an, LINEAS.length * 19 + 32);
  cx.font = "400 12px " + MONO; cx.textBaseline = "top";
  LINEAS.forEach((l, i) => {
    cx.globalAlpha = v * clamp((v - i * .06) * 7, 0, 1);
    cx.fillStyle = l[0] === ";" ? APAG : TINTA;
    cx.fillText(l, x, y + i * 19);
  });
  cx.restore();
}

function contadores(p, k, t){
  const av = k === 0 ? suave(t) : 1;
  cPiezas.textContent = Math.round(av * P.length);
  cM2.textContent = num(av * M2, 2) + " m²";
  cTal.textContent = Math.round(clamp(tramo(p, TRAMOS[1].de + (TRAMOS[1].a - TRAMOS[1].de) * .5,
                                             TRAMOS[1].a), 0, 1) * NTAL);
  pista.style.opacity = p > .03 ? 0 : 1;
}

/* ═══════════════════════════════════════════════════════════
   El scroll. No se secuestra: se LEE.
   ═══════════════════════════════════════════════════════════ */
const acto = document.getElementById("armActo");
const quieto = matchMedia("(prefers-reduced-motion: reduce)").matches;
let objetivo = 0, actual = 0, vivo = false, pedido = false;

/* El recorrido útil es el alto del bloque menos lo que ocupa la pantalla
   pegada, que ya no es la ventana entera: se le ha quitado la barra. */
const BARRA = 65;
function progreso(){
  const r = acto.getBoundingClientRect();
  const rec = r.height - (window.innerHeight - BARRA);
  return rec <= 0 ? 0 : clamp((BARRA - r.top) / rec, 0, 1);
}
/* La entrada y la salida del bloque. Se le pone la opacidad A LA PANTALLA
   ENTERA —dibujo, cajetín, carril y contadores— y no solo al lienzo: fundiendo
   solo el dibujo, el carril de fases aparecía de golpe sobre un papel vacío, y
   el salto seguía estando, solo que en otro sitio. Tres centésimas del bloque
   a cada lado son unos 200 px de rueda: lo justo para que no aparezca de
   golpe y no tanto como para tener que esperar. */
const escenario = acto.querySelector(".escenario");
function fotograma(){
  pedido = false;
  objetivo = progreso();
  /* Un pelo de suavizado para que la rueda no dé saltos. Con
     «prefers-reduced-motion» se va al valor directamente. */
  /* La inercia. .09 y no .18: el dibujo va un pelo por detrás de la rueda y
     eso es lo que hace que se sienta pesado —un mueble— y no nervioso. Por
     debajo de .07 ya se nota como retraso. */
  actual = quieto ? objetivo : actual + (objetivo - actual) * .09;
  if (Math.abs(objetivo - actual) < .0004) actual = objetivo;
  pinta(actual);
  if (escenario) escenario.style.opacity =
    Math.min(tramo(actual, 0, .03), 1 - tramo(actual, .97, 1)).toFixed(3);
  let f = 0; for (let i = 0; i < 5; i++) if (actual >= LIM[i]) f = i;
  rotulo(f);
  if (vivo && Math.abs(objetivo - actual) > .0004) pide();
}
function pide(){ if (!pedido) { pedido = true; requestAnimationFrame(fotograma); } }

new IntersectionObserver(es => { vivo = es[0].isIntersecting; if (vivo) pide(); },
  { rootMargin: "150px" }).observe(acto);
addEventListener("scroll", pide, { passive: true });
addEventListener("resize", () => { mide(); pide(); });
mide(); pinta(0); rotulo(0);

})();
