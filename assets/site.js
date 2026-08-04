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
