(function () {
  var burger = document.querySelector('.burger'), menu = document.getElementById('menu'), toast = document.getElementById('toast'), timer;

  function setMenu(open) {
    menu.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Fermer le menu' : 'Ouvrir le menu');
  }
  if (burger && menu) {
    burger.addEventListener('click', function () { setMenu(!menu.classList.contains('open')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) { setMenu(false); burger.focus(); }
    });
    window.addEventListener('resize', function () { if (window.innerWidth > 980) setMenu(false); });
  }

  function say(t) {
    if (!toast) return;
    toast.textContent = t; toast.classList.add('on');
    clearTimeout(timer); timer = setTimeout(function () { toast.classList.remove('on'); }, 3200);
  }

  function copyText(text, node) {
    function fallback() {
      var r = document.createRange(); r.selectNodeContents(node);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
      try { if (document.execCommand('copy')) { say('Copié dans le presse-papiers.'); return; } } catch (e) {}
      say('Texte sélectionné : copiez-le avec Ctrl+C.');
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { say('Copié dans le presse-papiers.'); }, fallback);
    } else { fallback(); }
  }

  var cb = document.getElementById('copy');
  if (cb) cb.addEventListener('click', function () { copyText('06 10 93 16 46', document.getElementById('tel-txt')); });

  /* Formulaire de contact */
  var form = document.getElementById('form-contact');
  if (!form) return;
  var recap = document.getElementById('recap'), recapTxt = document.getElementById('recap-txt'),
      smsLink = document.getElementById('recap-sms'), copyBtn = document.getElementById('recap-copy');
  var PHONE = '+33610931646';
  var rules = {
    nom: function (v) { return v.trim().length >= 2 ? '' : 'Indiquez votre nom (2 caractères minimum).'; },
    tel: function (v) {
      var c = v.replace(/[\s.\-]/g, '');
      return /^(?:(?:\+|00)33|0)[1-9]\d{8}$/.test(c) ? '' : 'Indiquez un numéro français valide, par exemple 06 12 34 56 78.';
    },
    email: function (v) {
      if (!v.trim()) return '';
      return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()) ? '' : 'Cette adresse e-mail semble incorrecte, par exemple nom@exemple.fr.';
    },
    besoin: function (v) { return v ? '' : 'Choisissez le sujet de votre demande.'; },
    message: function (v) { return v.trim().length >= 10 ? '' : 'Décrivez votre projet en quelques mots (10 caractères minimum).'; }
  };

  function check(name) {
    var f = form.elements[name], e = document.getElementById('err-' + name), m = rules[name](f.value);
    e.textContent = m;
    if (m) f.setAttribute('aria-invalid', 'true'); else f.removeAttribute('aria-invalid');
    return !m;
  }
  Object.keys(rules).forEach(function (n) {
    form.elements[n].addEventListener('blur', function () { check(n); });
    form.elements[n].addEventListener('input', function () { if (form.elements[n].getAttribute('aria-invalid')) check(n); });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var first = null;
    Object.keys(rules).forEach(function (n) { if (!check(n) && !first) first = form.elements[n]; });
    if (first) { first.focus(); recap.hidden = true; return; }
    var f = form.elements, lines = ['Bonjour, je vous contacte depuis votre site.', 'Nom : ' + f.nom.value.trim(), 'Téléphone : ' + f.tel.value.trim()];
    if (f.email.value.trim()) lines.push('E-mail : ' + f.email.value.trim());
    if (f.commune.value.trim()) lines.push('Commune : ' + f.commune.value.trim());
    lines.push('Sujet : ' + f.besoin.value, 'Message : ' + f.message.value.trim());
    var text = lines.join('\n');
    recapTxt.textContent = text;
    smsLink.href = 'sms:' + PHONE + '?&body=' + encodeURIComponent(text);
    recap.hidden = false;
    recap.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    recap.querySelector('h3').focus();
  });
  if (copyBtn) copyBtn.addEventListener('click', function () { copyText(recapTxt.textContent, recapTxt); });
})();
