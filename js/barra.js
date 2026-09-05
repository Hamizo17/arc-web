/* ===========================================================
   ARC · el cabezal de la barra
   -----------------------------------------------------------
   La barra deja de ser cuatro palabras y pasa a comportarse
   como el visor de posición de un centro de mecanizado: una
   cruz recorre la barra hasta lo que estás señalando, la
   lectura de la izquierda cambia con ella, y al pulsar entra
   la broca antes de irse.

   ── DÓNDE DESCANSA ──
   Cuando sueltas el ratón la cruz NO se queda donde la
   dejaste: vuelve a la sección en la que estás. Es lo que hace
   una máquina —descansa en la última posición ordenada, no
   donde la dejó el operario— y de paso convierte un adorno en
   información: de un vistazo sabes por dónde vas.

   Para eso hace falta saber en qué sección estás, y eso NO
   estaba: `arc.js` marcaba como actual cualquier enlace cuya
   ruta coincidiera, y en la portada los tres enlaces con
   almohadilla apuntan a «/», así que se marcaban los tres a la
   vez. Aquí se marca UNO: el de la sección que ocupa la
   pantalla.

   ── DÓNDE NO SE PONE ──
   En un móvil no hay ratón que seguir: sin `hover` fino, ni la
   cruz ni la lectura existen —lo decide el CSS— y esto ni se
   arranca. Y con «reducir movimiento», la cruz va sin
   transición: se pone donde toca y ya.
   =========================================================== */
(function () {
  const barra = document.querySelector(".barra .hoja");
  const cruz  = document.getElementById("barraCruz");
  const lect  = document.getElementById("barraPos");
  if (!barra || !cruz || !lect) return;
  /* El CSS es quien decide si esto pinta algo. Si la cruz no se dibuja
     —móvil, pantalla táctil— no se mueve nada ni se escucha nada. */
  if (getComputedStyle(cruz).display === "none") return;

  const enlaces = [...barra.querySelectorAll("nav a")];
  if (!enlaces.length) return;
  const quieto = matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (quieto) cruz.style.transition = "none";

  const num = v => v.toLocaleString("es-ES",
    { minimumFractionDigits: 1, maximumFractionDigits: 1 });

  let encasa = null;          // el enlace donde descansa
  function lleva(a, suave) {
    /* Sin posición no se inventa una: la máquina no pone un cero cuando no
       tiene orden, pone rayas. */
    if (!a) { cruz.classList.remove("puesta"); lect.textContent = "X ——"; return; }
    const r = a.getBoundingClientRect(), b = barra.getBoundingClientRect();
    const x = r.left + r.width / 2 - b.left;
    if (!suave) cruz.style.transition = "none";
    cruz.style.transform = "translateX(" + x + "px)";
    if (!suave) { void cruz.offsetWidth; cruz.style.transition = ""; }
    lect.textContent = "X " + num(x);
    cruz.classList.add("puesta");
  }
  const acasa = () => lleva(encasa, true);

  enlaces.forEach(a => {
    a.addEventListener("pointerenter", () => lleva(a, true));
    a.addEventListener("focus", () => lleva(a, true));
    /* La broca. No se para la navegación para que entre: un menú que te hace
       esperar medio segundo a que acabe una animación es un menú peor. Se
       lanza y el navegador hace lo suyo; si es un enlace de la misma página,
       se ve entera. */
    a.addEventListener("click", () => {
      cruz.classList.remove("entra");
      void cruz.offsetWidth;
      cruz.classList.add("entra");
    });
  });
  barra.addEventListener("pointerleave", acasa);
  addEventListener("resize", () => lleva(encasa, false));

  /* ---------- en qué sección estamos ----------
     Se mira qué sección ocupa la franja de en medio de la pantalla. La franja
     y no un punto: con un punto, una sección más corta que la ventana no llega
     a cruzarlo nunca y no se marca jamás. */
  const deLaPagina = a => {
    const u = new URL(a.getAttribute("href"), location.href);
    const aqui = location.pathname.replace(/\/index\.html$/, "/").replace(/\.html$/, "");
    const suya = u.pathname.replace(/\/index\.html$/, "/").replace(/\.html$/, "");
    return suya === aqui ? u.hash.slice(1) : null;
  };
  const conAncla = enlaces.map(a => ({ a, id: deLaPagina(a) }))
                          .filter(x => x.id && document.getElementById(x.id));
  const sinAncla = enlaces.find(a => a.hasAttribute("aria-current") && !deLaPagina(a));

  function marca(a) {
    if (a === encasa) return;
    enlaces.forEach(x => { if (x !== sinAncla) x.removeAttribute("aria-current"); });
    if (a) a.setAttribute("aria-current", "true");
    encasa = a || sinAncla || null;
    acasa();
  }

  if (conAncla.length) {
    const mira = () => {
      const medio = innerHeight * .45;
      let elegido = null;
      conAncla.forEach(({ a, id }) => {
        const r = document.getElementById(id).getBoundingClientRect();
        if (r.top <= medio && r.bottom > medio) elegido = a;
      });
      marca(elegido);
    };
    addEventListener("scroll", mira, { passive: true });
    addEventListener("resize", mira);
    mira();
  }
  encasa = encasa || sinAncla || null;
  acasa();
})();
