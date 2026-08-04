/* CLEGAR — contact form + footer year.
   Navigation and language switching are plain links: no JS required. */
(function () {
  'use strict';
  var y = document.getElementById('yr');
  if (y) y.textContent = new Date().getFullYear();

  var lang = (document.documentElement.lang === 'en') ? 'en' : 'it';

  /* ============================================================
     Paste your form endpoint below and messages are delivered
     straight to info@clegar.it.
       Formspree  https://formspree.io  ->  https://formspree.io/f/xxxxxxxx
       Web3Forms  https://web3forms.com ->  https://api.web3forms.com/submit
     Left empty, the button opens the visitor's mail client instead.
     ============================================================ */
  var FORM_ENDPOINT = '';
  var WEB3FORMS_KEY = '';

  var MSG = {
    missing: {it:'Servono un indirizzo email valido e una descrizione.', en:'A valid email address and a description are required.'},
    sending: {it:'Invio in corso…', en:'Sending…'},
    sent:    {it:'Messaggio inviato. Vi rispondiamo entro due giorni lavorativi.', en:'Message sent. We will reply within two working days.'},
    failed:  {it:'Invio non riuscito. Scrivete direttamente a info@clegar.it.', en:'Could not send. Please email info@clegar.it directly.'},
    opening: {it:'Apertura del client di posta in corso…', en:'Opening your email client…'},
    subject: {it:'Richiesta – ', en:'Enquiry – '},
    fName:   {it:'Nome', en:'Name'},
    fOrg:    {it:'Azienda', en:'Company'},
    fMail:   {it:'Email', en:'Email'},
    fArea:   {it:'Ambito', en:'Area'}
  };




  /* La scelta manuale della lingua vince sempre sul rilevamento
     automatico: appena l'utente tocca IT/EN, la memorizziamo e il
     redirect della home non si attiva piu. */
  (function () {
    var sw = document.querySelectorAll('.langsw a');
    if (!sw.length) return;
    Array.prototype.forEach.call(sw, function (a) {
      a.addEventListener('click', function () {
        try { localStorage.setItem('clegar_lang', a.getAttribute('hreflang') || lang); } catch (e) {}
      });
    });
    /* chi arriva direttamente su una pagina inglese ha gia espresso una preferenza */
    if (lang === 'en') { try { localStorage.setItem('clegar_lang', 'en'); } catch (e) {} }
  })();

  /* ============================================================
     GOOGLE ANALYTICS 4 — attivato solo dopo il consenso
     (il Garante Privacy richiede l'opt-in prima di qualunque
     cookie di tracciamento).

     >>> INCOLLA QUI IL TUO ID: sostituisci G-XXXXXXXXXX con il
         Measurement ID che trovi su analytics.google.com.
         È l'unica riga da modificare in tutto il sito.
     ============================================================ */
  var GA_ID = 'G-XL4B4Y4DY1';

  (function () {
    if (GA_ID.indexOf('XXXX') !== -1) return;   // non ancora configurato
    var KEY = 'clegar_consent';

    function loadGA() {
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { dataLayer.push(arguments); };
      gtag('js', new Date());
      gtag('config', GA_ID, { anonymize_ip: true });
    }

    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (e) { return; }
    if (stored === 'granted') { loadGA(); return; }
    if (stored === 'denied') return;

    var TXT = {
      it: { msg: 'Questo sito utilizza cookie analitici per misurare l\'utilizzo delle pagine e migliorarne i contenuti. Vengono installati esclusivamente previo consenso e non sono impiegati per finalit\u00e0 pubblicitarie o di profilazione.',
            accept: 'Accetta', reject: 'Rifiuta' },
      en: { msg: 'This site uses analytics cookies to measure how its pages are used and to improve its content. They are set only with your consent and are never used for advertising or profiling.',
            accept: 'Accept', reject: 'Decline' }
    }[lang];

    var bar = document.createElement('div');
    bar.setAttribute('role', 'region');
    bar.setAttribute('aria-label', lang === 'it' ? 'Consenso cookie' : 'Cookie consent');
    bar.style.cssText = 'position:fixed;left:0;right:0;bottom:0;z-index:1100;background:#0B2545;'
      + 'color:#DCE7F1;padding:1rem clamp(1.1rem,4vw,2.75rem);display:flex;gap:1rem;'
      + 'flex-wrap:wrap;align-items:center;justify-content:space-between;'
      + 'font-family:Georgia,serif;font-size:.92rem;line-height:1.5;'
      + 'box-shadow:0 -2px 18px rgba(0,0,0,.18)';
    bar.innerHTML =
      '<p style="margin:0;max-width:46rem;flex:1 1 18rem">' + TXT.msg + '</p>'
      + '<div style="display:flex;gap:.6rem;flex:none">'
      + '<button id="cc-reject" style="font-family:monospace;font-size:.7rem;letter-spacing:.1em;'
      + 'text-transform:uppercase;background:none;color:#DCE7F1;border:1px solid rgba(220,231,241,.4);'
      + 'padding:.7rem 1.1rem;min-height:44px;cursor:pointer">' + TXT.reject + '</button>'
      + '<button id="cc-accept" style="font-family:monospace;font-size:.7rem;letter-spacing:.1em;'
      + 'text-transform:uppercase;background:#009AA6;color:#fff;border:0;'
      + 'padding:.7rem 1.1rem;min-height:44px;cursor:pointer">' + TXT.accept + '</button></div>';
    document.body.appendChild(bar);

    document.getElementById('cc-accept').onclick = function () {
      try { localStorage.setItem(KEY, 'granted'); } catch (e) {}
      bar.remove(); loadGA();
    };
    document.getElementById('cc-reject').onclick = function () {
      try { localStorage.setItem(KEY, 'denied'); } catch (e) {}
      bar.remove();
    };
  })();

  /* ============================================================
     FIGURE VIEWER
     Charts fit the page width; at that size their labels would be
     2-4px. A tap opens the figure full-screen, rendered large
     enough to read and pannable.
     ============================================================ */
  (function () {
    var figs = document.querySelectorAll('figure[data-zoomable]');
    if (!figs.length) return;
    if (!window.matchMedia || !window.matchMedia('(max-width: 900px)').matches) return;

    var TXT = {
      it: { close: 'Chiudi', hint: 'Scorri per esplorare il grafico' },
      en: { close: 'Close',  hint: 'Scroll to explore the chart' }
    }[lang];

    var modal = document.createElement('div');
    modal.className = 'figmodal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.innerHTML =
      '<div class="figmodal-bar"><span>' + TXT.hint + '</span>'
      + '<button class="figmodal-close" type="button">' + TXT.close + '</button></div>'
      + '<div class="figmodal-body"></div>';
    document.body.appendChild(modal);

    var body = modal.querySelector('.figmodal-body');
    var closeBtn = modal.querySelector('.figmodal-close');
    var lastFocus = null;

    function open(fig) {
      var chart = fig.querySelector('svg, .datafig');
      if (!chart) return;
      body.innerHTML = '';
      body.appendChild(chart.cloneNode(true));
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
      lastFocus = document.activeElement;
      closeBtn.focus();
    }

    function close() {
      modal.classList.remove('open');
      document.body.style.overflow = '';
      body.innerHTML = '';
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }

    Array.prototype.forEach.call(figs, function (fig) {
      var target = fig.querySelector('svg, .datafig');
      if (!target) return;
      target.style.cursor = 'zoom-in';
      target.addEventListener('click', function () { open(fig); });
      fig.setAttribute('tabindex', '0');
      fig.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(fig); }
      });
    });

    closeBtn.addEventListener('click', close);
    modal.addEventListener('click', function (e) { if (e.target === modal) close(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('open')) close();
    });
  })();

  var send = document.getElementById('f-send');
  if (!send) return;
  var statusEl = document.getElementById('f-status');

  function say(t, c) { if (statusEl) { statusEl.textContent = t; statusEl.style.color = c || 'var(--steel)'; } }
  function val(id) { var el = document.getElementById(id); return el ? (el.value || '').trim() : ''; }

  function fields() {
    var sel = document.getElementById('f-svc-' + lang) || document.getElementById('f-svc');
    return { name: val('f-nome'), company: val('f-org'), email: val('f-mail'),
             area: sel ? sel.value : '', message: val('f-msg'), trap: val('f-hp') };
  }

  function mailtoFallback(f) {
    var body = MSG.fName[lang] + ': ' + f.name + '\n'
             + MSG.fOrg[lang]  + ': ' + f.company + '\n'
             + MSG.fMail[lang] + ': ' + f.email + '\n'
             + MSG.fArea[lang] + ': ' + f.area + '\n\n' + f.message;
    window.location.href = 'mailto:info@clegar.it?subject='
      + encodeURIComponent(MSG.subject[lang] + f.area) + '&body=' + encodeURIComponent(body);
    say(MSG.opening[lang]);
  }

  send.addEventListener('click', function () {
    var f = fields();
    if (f.trap) return;
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]{2,}$/.test(f.email) || !f.message) { say(MSG.missing[lang], '#C9821E'); return; }
    if (!FORM_ENDPOINT) { mailtoFallback(f); return; }

    var payload = { name:f.name, company:f.company, email:f.email, area:f.area,
                    message:f.message, subject:MSG.subject[lang]+f.area,
                    _subject:MSG.subject[lang]+f.area, language:lang };
    if (WEB3FORMS_KEY) payload.access_key = WEB3FORMS_KEY;

    send.disabled = true;
    say(MSG.sending[lang]);
    fetch(FORM_ENDPOINT, { method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body: JSON.stringify(payload) })
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        say(MSG.sent[lang], 'var(--teal)');
        ['f-nome','f-org','f-mail','f-msg'].forEach(function (id) {
          var el = document.getElementById(id); if (el) el.value = '';
        });
      })
      .catch(function () { say(MSG.failed[lang], '#C9821E'); })
      .then(function () { send.disabled = false; });
  });
})();
