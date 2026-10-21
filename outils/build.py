"""Génère les pages HTML du site ALL GARDEN (maquette). Usage : python3 outils/build.py  (depuis la racine du dépôt)"""
import os
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = "https://webaunet.github.io/all-garden/"
TEL = "06 10 93 16 46"
TELH = "+33610931646"
ADR = "55 rue Alfred Dubois, 91460 Marcoussis"
NAV = [("index.html", "Accueil"), ("prestations.html", "Prestations"), ("realisations.html", "Réalisations"), ("contact.html", "Contact")]

ALT = {
    "hero-jardin-allee": "Allée de gravier sinueuse bordée de pelouse et de massifs fleuris devant une maison en pierre",
    "creation-espace-vert": "Massif de graminées et de vivaces planté le long d'une pelouse à bordure courbe, devant une maison contemporaine",
    "tonte-pelouse": "Jardinier tondant la pelouse d'un jardin devant une maison en pierre aux volets bleus",
    "elagage-chene": "Élagueur encordé, casqué, travaillant à la tronçonneuse dans un grand chêne au-dessus d'un jardin",
    "elagage-cordiste": "Élagueur en tenue orange et casque, encordé dans un grand chêne au-dessus de maisons et de jardins",
    "muret-pierre-escalier": "Muret de pierres et escalier de pierre en construction dans un jardin, avec une maison en briques au fond",
    "terrasse-bois": "Pose d'une terrasse en bois devant une maison en pierre",
    "allee-pierre-muret": "Allée dallée de pierre claire longeant un muret de pierres et des massifs fleuris",
    "allee-dallee-soir": "Allée dallée éclairée par des balises, menant à une maison en pierre au crépuscule",
    "conception-tablette": "Deux personnes consultant un plan de jardin en 3D sur une tablette, avec un massif bordé d'un muret de pierre en arrière-plan",
    "plantation": "Jardinier à genoux plantant un arbuste dans un massif fraîchement ameubli",
    "nivellement-terrain": "Jardinier ratissant une terre fraîchement nivelée, avec un massif de graviers courbe et une maison au fond",
    "terrassement-fouille": "Jardinier creusant la terre à la pelle près d'une brouette, devant une maison en briques",
    "entretien-massif": "Jardinier agenouillé entretenant un massif de fleurs et de vivaces, avec une brouette, le long d'une allée de gravier",
    "tondeuse-rouge": "Jardinier en gilet vert poussant une tondeuse rouge sur une pelouse, devant une maison en pierre",
    "ramassage-feuilles": "Jardinier ramassant des feuilles mortes près d'un massif, avec un sac de déchets verts posé sur l'allée de gravier",
    "dechets-verts": "Jardinier chargeant des branchages dans une camionnette blanche au milieu d'un jardin",
    "dessouchage": "Dessouchage d'un tronc d'arbre avec une rogneuse de souche jaune, dans un jardin soigné",
    "taille-haie": "Jardinier taillant une haie dense au taille-haie thermique, une bâche posée au sol pour recueillir les coupes",
    "robot-tonte": "Robot tondeuse sur une pelouse rayée, avec une allée dallée, une terrasse en bois et un massif au pied d'un muret de pierre",
    "nettoyage-jardin": "Jardinier ratissant des branches et des feuilles dans une brouette devant une maison en pierre",
}


def img(name, lazy=True, style="", cls=""):
    p = os.path.join(ROOT, "images", name + ".jpg")
    w, h = Image.open(p).size
    return ('<img src="images/%s.jpg" width="%d" height="%d" alt="%s"%s%s%s>' % (
        name, w, h, ALT[name], ' loading="lazy"' if lazy else "",
        ' style="%s"' % style if style else "", ' class="%s"' % cls if cls else ""))


def fig(name, cap=None, style=""):
    return "<figure>%s%s</figure>" % (img(name, style=style), '<figcaption class="cap">%s</figcaption>' % cap if cap else "")


def header(active):
    items = "".join('<li><a href="%s"%s>%s</a></li>' % (h, ' aria-current="page"' if h == active else "", t) for h, t in NAV)
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="{BASE}" aria-label="ALL GARDEN, accueil">
      <svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="12" fill="#12372a"/><path d="M20 30V19" stroke="#b9dc4a" stroke-width="2.6" stroke-linecap="round"/><path d="M20 21c-6 0-9-3.4-9-8.5 6 0 9 3 9 8.5Z" fill="#b9dc4a"/><path d="M20 24c5 0 8-3 8-7.5-5.2 0-8 2.6-8 7.5Z" fill="#6fae4a"/></svg>
      <span><b>ALL GARDEN</b><small>Paysagiste · Marcoussis</small></span>
    </a>
    <nav id="menu" aria-label="Navigation principale"><ul>{items}</ul></nav>
    <a class="call" href="tel:{TELH}" aria-label="Appeler le {TEL}">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
      <span>{TEL}</span>
    </a>
    <button class="burger" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu"><span></span></button>
  </div>
</header>'''


def footer(active):
    pl = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in NAV[1:])
    return f'''<footer>
  <div class="wrap">
    <div class="row">
      <div class="id"><b>ALL GARDEN</b><address>{ADR}</address></div>
      <ul aria-label="Liens du pied de page"><li class="t"><a href="tel:{TELH}">{TEL}</a></li>{pl}<li class="m"><a href="mentions-legales.html">Mentions légales</a></li></ul>
    </div>
    <div class="legal">© ALL GARDEN SARL · Maquette de site</div>
  </div>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="script.js"></script>'''


def page(fname, title, desc, body, active=None):
    html = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#12372a">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&amp;family=Figtree:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
{header(active or fname)}
<main id="contenu">
{body}
</main>
{footer(active or fname)}
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), "w", encoding="utf8") as f:
        f.write(html)


# ---------------------------------------------------------------- ACCUEIL
accueil = f'''
  <section class="hero" aria-labelledby="t-hero">
    {img("hero-jardin-allee", lazy=False)}
    <div class="wrap">
      <span class="eyebrow">Paysagiste à Marcoussis, Essonne</span>
      <h1 id="t-hero">Des jardins <em>créés</em>, entretenus et élagués.</h1>
      <p class="lead">ALL GARDEN conçoit, réalise et entretient les parcs et jardins des particuliers comme des structures publiques, avec une équipe qui s'occupe aussi de vos arbres.</p>
      <div class="actions">
        <a class="btn btn-lime" href="contact.html">Parler de votre projet</a>
        <a class="btn btn-line" href="#metiers">Voir nos métiers</a>
      </div>
      <ul class="facts"><li>Entreprise créée en 2012</li><li>Jardins privés et publics</li><li>Basés à Marcoussis (91)</li></ul>
    </div>
  </section>

  <section class="band metiers bg-paper" id="metiers" aria-labelledby="t-metiers">
    <div class="wrap">
      <div class="head">
        <span class="eyebrow">Nos métiers</span>
        <h2 id="t-metiers">Du plan du jardin jusqu'à la cime des arbres</h2>
        <p>Un seul interlocuteur pour imaginer l'espace, le réaliser, l'entretenir et s'occuper des arbres.</p>
      </div>
      <div class="cards">
        <article class="card">{img("creation-espace-vert")}<div class="in"><span class="pill p1">Concevoir</span><h3>Création de jardins</h3><p>Nous dessinons votre jardin avec vous, puis nous le réalisons.</p><ul><li>Conception du projet</li><li>Réalisation des aménagements</li></ul></div></article>
        <article class="card">{img("tonte-pelouse")}<div class="in"><span class="pill p2">Entretenir</span><h3>Entretien de parcs et jardins</h3><p>Un jardin soigné toute l'année, chez les particuliers comme pour le public.</p><ul><li>Jardins privés</li><li>Parcs et espaces publics</li></ul></div></article>
        <article class="card">{img("elagage-chene")}<div class="in"><span class="pill p3">Les arbres</span><h3>Élagage et abattage</h3><p>Intervention sur les arbres, avec un regard sur leur état de santé.</p><ul><li>Élagage</li><li>Abattage</li><li>État sanitaire des arbres</li></ul></div></article>
      </div>
      <div class="actions" style="margin-top:28px"><a class="btn btn-dark" href="prestations.html">Toutes nos prestations</a></div>
    </div>
  </section>

  <section class="band dur" id="amenagements" aria-labelledby="t-dur">
    <div class="wrap grid">
      <div class="txt">
        <span class="eyebrow">Aménagements extérieurs</span>
        <h2 id="t-dur">Maçonnerie paysagère et clôtures</h2>
        <p>Murets, escaliers de pierre, limites de propriété : la structure du jardin se construit aussi avec la pierre et la clôture.</p>
        <p>Chaque ouvrage est pensé avec le reste du jardin pour que l'ensemble tienne visuellement.</p>
        <div class="actions"><a class="btn btn-lime" href="contact.html">Décrire mon projet</a><a class="btn btn-line" href="realisations.html">Voir les réalisations</a></div>
      </div>
      <div class="mosaic">
        <figure>{img("muret-pierre-escalier", style="object-position:25% 60%")}<figcaption>Muret et escalier de pierre</figcaption></figure>
        <figure>{img("terrasse-bois")}<figcaption>Terrasse en bois</figcaption></figure>
        <figure>{img("allee-pierre-muret")}<figcaption>Allée dallée</figcaption></figure>
        <figure>{img("allee-dallee-soir")}<figcaption>Allée éclairée</figcaption></figure>
      </div>
    </div>
  </section>

  <section class="band apropos" id="apropos" aria-labelledby="t-apropos">
    <div class="wrap">
      <div class="about">
        <div class="copy">
          <span class="eyebrow">L'entreprise</span>
          <h2 id="t-apropos">Une équipe de paysagistes installée à Marcoussis</h2>
          <p>ALL GARDEN est une SARL créée en 2012, installée à Marcoussis dans l'Essonne. Elle conçoit, réalise et entretient des parcs et jardins privés ou publics, et intervient sur les arbres : élagage, abattage et état sanitaire.</p>
          <p>Vous avez un jardin à imaginer, à reprendre ou à entretenir ? Racontez-nous votre projet par téléphone.</p>
          <div class="ident"><span>SARL · SIREN 788 893 477</span><span>{ADR}</span></div>
        </div>
        <div class="visual">
          {img("conception-tablette")}
          <div class="stamp"><span><b>2012</b>année de création</span><span><b>6 à 9</b>salariés (registre, 2024)</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="band contact" id="contact" aria-labelledby="t-contact">
    <div class="wrap grid">
      <div>
        <span class="eyebrow">Contact</span>
        <h2 id="t-contact">Un jardin à créer, à entretenir, un arbre à voir ?</h2>
        <p>Le plus simple est d'appeler : présentez votre projet à l'équipe d'ALL GARDEN.</p>
        <span class="tel" id="tel-txt">{TEL}</span>
        <div class="loc">Marcoussis (91460) · Essonne</div>
        <div class="actions">
          <a class="btn btn-lime" href="tel:{TELH}">Appeler</a>
          <a class="btn btn-line" href="contact.html">Écrire un message</a>
          <button class="btn btn-line" type="button" id="copy">Copier le numéro</button>
        </div>
      </div>
      <figure>{img("plantation")}</figure>
    </div>
  </section>'''
page("index.html", "ALL GARDEN, paysagiste à Marcoussis (91) | Création, entretien et élagage",
     "ALL GARDEN, paysagiste à Marcoussis (91) : conception, réalisation et entretien de parcs et jardins, élagage et abattage, maçonnerie paysagère et clôtures.", accueil)

# ------------------------------------------------------------ PRESTATIONS
prest = f'''
  <section class="ph bg-forest" aria-labelledby="t-ph">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Nos prestations</span>
        <h1 id="t-ph">Aménager, entretenir, s'occuper des arbres</h1>
        <p class="lead">Les parcs et jardins privés ou publics sont notre terrain. Choisissez par où commencer.</p>
        <div class="actions"><a class="btn btn-lime" href="#amenager">Aménager</a><a class="btn btn-line" href="#entretenir">Entretenir</a></div>
      </div>
      <div class="trio">
        <figure>{img("creation-espace-vert", lazy=False)}</figure>
        <figure>{img("tonte-pelouse", lazy=False)}</figure>
        <figure>{img("elagage-chene", lazy=False)}</figure>
      </div>
    </div>
  </section>

  <section class="band amenager bg-paper" id="amenager" aria-labelledby="t-am">
    <div class="wrap">
      <div class="head"><span class="eyebrow">Aménager</span><h2 id="t-am">Un jardin pensé, puis construit</h2><p>De la conception à la réalisation, y compris les ouvrages en pierre et les limites de propriété.</p></div>
      <div class="grid">
        <article class="card wide">{img("conception-tablette")}<div class="in"><span class="pill p1">Conception et réalisation</span><h3>Création de jardins</h3><p>Nous concevons le jardin avec vous, puis nous réalisons les aménagements prévus.</p></div></article>
        <div class="stack">
          <article class="card row">{img("muret-pierre-escalier", style="object-position:25% 60%")}<div class="in"><span class="pill p3">Pierre</span><h3>Maçonnerie paysagère</h3><p>Murets, escaliers et ouvrages de pierre intégrés au jardin.</p></div></article>
          <article class="card ico"><div class="in"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 40V12l4-4 4 4v28M20 40V12l4-4 4 4v28M32 40V12l4-4 4 4v28M4 20h40M4 32h40"/></svg><span class="pill p2">Limites</span><h3>Clôtures</h3><p>Des clôtures pour délimiter et protéger votre propriété.</p></div></article>
        </div>
      </div>
    </div>
  </section>

  <section class="band bg-mist" id="entretenir" aria-labelledby="t-en">
    <div class="wrap g2" style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center">
      <div>
        <span class="eyebrow" style="color:var(--leaf)">Entretenir</span>
        <h2 class="sect-h" id="t-en">L'entretien des parcs et jardins, privés ou publics</h2>
        <p class="sect-p">ALL GARDEN entretient les espaces verts de ses clients tout au long de l'année. Parlez-nous de votre jardin, nous vous dirons ce qu'il demande.</p>
        <div class="aud"><div><b>Particuliers</b><span>Jardins de maisons individuelles.</span></div><div><b>Structures publiques</b><span>Parcs et espaces verts publics.</span></div></div>
        <div class="actions"><a class="btn btn-dark" href="contact.html">Demander un entretien</a></div>
      </div>
      <div class="duo">
        <figure>{img("entretien-massif")}</figure>
        <figure>{img("tondeuse-rouge")}</figure>
      </div>
    </div>
  </section>

  <section class="band arbres bg-leaf" id="arbres" aria-labelledby="t-ar">
    <div class="wrap g2">
      <figure>{img("elagage-cordiste")}</figure>
      <div>
        <span class="eyebrow">Les arbres</span>
        <h2 class="sect-h" id="t-ar">Élagage, abattage et suivi de l'état des arbres</h2>
        <p class="sect-p">Un arbre qui gêne, penche ou vieillit mérite un avis. ALL GARDEN intervient sur les arbres et regarde leur état sanitaire.</p>
        <div class="tiles">
          <div class="tile"><h3>Élagage</h3><p>Intervention sur les branches des arbres de votre jardin ou de votre parc.</p></div>
          <div class="tile"><h3>Abattage</h3><p>Abattage d'arbres lorsque la situation le demande.</p></div>
          <div class="tile"><h3>État sanitaire</h3><p>Un regard sur la santé de vos arbres pour décider s'il faut intervenir.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="band cta-band bg-lime" aria-labelledby="t-cta">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Votre projet</span>
        <h2 id="t-cta">Un terrain, une idée, un devis à envisager ?</h2>
        <p>Décrivez votre besoin en quelques lignes ou appelez directement l'équipe.</p>
        <span class="tel2">{TEL}</span>
        <div class="actions"><a class="btn btn-dark" href="contact.html">Écrire à ALL GARDEN</a><a class="btn btn-ghost" href="tel:{TELH}">Appeler</a></div>
      </div>
      <figure>{img("nivellement-terrain")}</figure>
    </div>
  </section>'''
page("prestations.html", "Prestations d'un paysagiste à Marcoussis | ALL GARDEN",
     "Création de jardins, entretien de parcs et jardins, élagage, abattage, maçonnerie paysagère et clôtures : les prestations d'ALL GARDEN à Marcoussis (91).", prest)

# ----------------------------------------------------------- RÉALISATIONS
real = f'''
  <section class="ph bg-mist" aria-labelledby="t-ph">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Réalisations</span>
        <h1 id="t-ph">Jardins, pierre et arbres en images</h1>
        <p class="lead">Un aperçu des chantiers et des savoir-faire d'ALL GARDEN : aménagements, plantations, entretien et travaux sur les arbres.</p>
        <div class="actions"><a class="btn btn-dark" href="#amenagements">Aménagements</a><a class="btn btn-ghost" href="#entretien">Entretien et arbres</a></div>
      </div>
      <div class="fan">
        <figure>{img("creation-espace-vert", lazy=False)}</figure>
        <figure>{img("allee-pierre-muret", lazy=False)}</figure>
        <figure>{img("terrasse-bois", lazy=False)}</figure>
      </div>
    </div>
  </section>

  <section class="band bg-forest" id="amenagements" aria-labelledby="t-a">
    <div class="wrap">
      <div class="head"><span class="eyebrow">Aménagements</span><h2 id="t-a">Pierre, bois et allées</h2><p>Des ouvrages qui structurent le jardin.</p></div>
      <div class="gal gal-a">
        {fig("muret-pierre-escalier", "Muret et escalier de pierre", "object-position:25% 60%")}
        {fig("terrasse-bois", "Terrasse en bois")}
        {fig("allee-pierre-muret", "Allée dallée et muret")}
        {fig("allee-dallee-soir", "Allée éclairée")}
        {fig("conception-tablette", "Étude du projet sur plan 3D")}
      </div>
    </div>
  </section>

  <section class="band bg-paper" id="jardins" aria-labelledby="t-j">
    <div class="wrap split">
      <div>
        <span class="eyebrow" style="color:var(--leaf)">Jardins et plantations</span>
        <h2 class="sect-h" id="t-j">Du terrain nu au massif planté</h2>
        <p class="sect-p">Préparation du sol, nivellement, plantation : chaque jardin commence par la terre.</p>
        <div class="actions"><a class="btn btn-dark" href="contact.html">Parler de mon terrain</a></div>
      </div>
      <div class="gal gal-b">
        {fig("terrassement-fouille", "Creusement de la terre")}
        {fig("nivellement-terrain", "Terre nivelée")}
        {fig("plantation", "Plantation d'un arbuste")}
        {fig("robot-tonte", "Jardin avec robot tondeuse")}
      </div>
    </div>
  </section>

  <section class="band bg-leaf" id="entretien" aria-labelledby="t-e">
    <div class="wrap">
      <div class="head"><span class="eyebrow">Entretien et arbres</span><h2 id="t-e">Le geste quotidien du jardinier</h2><p>Taille, nettoyage, évacuation, et interventions sur les arbres.</p></div>
      <div class="gal gal-c">
        {fig("elagage-cordiste", "Élagage dans un chêne")}
        {fig("dessouchage", "Dessouchage")}
        {fig("taille-haie", "Taille de haie")}
        {fig("ramassage-feuilles", "Ramassage des feuilles")}
        {fig("dechets-verts", "Évacuation des déchets verts")}
        {fig("nettoyage-jardin", "Nettoyage du jardin")}
      </div>
    </div>
  </section>

  <section class="band cta-band bg-lime" aria-labelledby="t-cta">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">À vous de jouer</span>
        <h2 id="t-cta">Et si on parlait de votre jardin ?</h2>
        <p>Envoyez-nous quelques lignes sur ce que vous imaginez, nous vous rappelons.</p>
        <div class="actions"><a class="btn btn-dark" href="contact.html">Écrire à ALL GARDEN</a><a class="btn btn-ghost" href="tel:{TELH}">{TEL}</a></div>
      </div>
      <figure>{img("hero-jardin-allee", style="object-position:50% 60%")}</figure>
    </div>
  </section>'''
page("realisations.html", "Réalisations en images | ALL GARDEN, paysagiste à Marcoussis",
     "Aménagements en pierre et en bois, plantations, entretien et travaux sur les arbres : un aperçu en images des savoir-faire d'ALL GARDEN, paysagiste à Marcoussis (91).", real)

# ---------------------------------------------------------------- CONTACT
contact = f'''
  <section class="ph bg-paper" aria-labelledby="t-ph">
    <div class="wrap g2">
      <div>
        <span class="eyebrow" style="color:var(--leaf)">Contact</span>
        <h1 id="t-ph">Parlons de votre jardin</h1>
        <p class="lead" style="color:var(--ink-soft)">Le plus rapide est d'appeler. Vous pouvez aussi remplir le formulaire plus bas : il prépare un message prêt à envoyer par SMS.</p>
        <a class="bigtel" href="tel:{TELH}">{TEL}</a>
        <div class="info"><div><b>Adresse</b><br>{ADR}</div></div>
        <div class="actions"><a class="btn btn-dark" href="tel:{TELH}">Appeler</a><a class="btn btn-ghost" href="#formulaire">Écrire un message</a><a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&amp;query=55+rue+Alfred+Dubois+91460+Marcoussis" target="_blank" rel="noopener">Voir sur la carte</a></div>
      </div>
      <figure class="cfig">{img("hero-jardin-allee", lazy=False, style="object-position:50% 60%")}</figure>
    </div>
  </section>

  <section class="band bg-mist" id="formulaire" aria-labelledby="t-f">
    <div class="wrap">
      <div class="formcard">
        <span class="eyebrow" style="color:var(--leaf)">Formulaire</span>
        <h2 class="sect-h" id="t-f">Décrire votre demande</h2>
        <form id="form-contact" novalidate>
          <div class="row2">
            <div class="fld"><label for="nom">Nom <span aria-hidden="true">*</span></label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="err-nom"><div class="err" id="err-nom" aria-live="polite"></div></div>
            <div class="fld"><label for="tel">Téléphone <span aria-hidden="true">*</span></label><input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="err-tel"><div class="err" id="err-tel" aria-live="polite"></div></div>
          </div>
          <div class="row2">
            <div class="fld"><label for="email">E-mail <span class="opt">(facultatif)</span></label><input id="email" name="email" type="email" autocomplete="email" aria-describedby="err-email"><div class="err" id="err-email" aria-live="polite"></div></div>
            <div class="fld"><label for="commune">Commune <span class="opt">(facultatif)</span></label><input id="commune" name="commune" type="text" autocomplete="address-level2"><div class="err" aria-hidden="true"></div></div>
          </div>
          <div class="fld"><label for="besoin">Sujet <span aria-hidden="true">*</span></label><select id="besoin" name="besoin" required aria-describedby="err-besoin"><option value="">Choisir…</option><option>Création de jardin</option><option>Entretien de parc ou de jardin</option><option>Élagage ou abattage</option><option>Maçonnerie paysagère ou clôture</option><option>Autre demande</option></select><div class="err" id="err-besoin" aria-live="polite"></div></div>
          <div class="fld"><label for="message">Votre projet <span aria-hidden="true">*</span></label><textarea id="message" name="message" required aria-describedby="err-message"></textarea><div class="err" id="err-message" aria-live="polite"></div></div>
          <button class="btn btn-dark" type="submit">Préparer mon message</button>
        </form>
        <div class="recap" id="recap" hidden>
          <h3 tabindex="-1">Votre message est prêt</h3>
          <pre id="recap-txt"></pre>
          <div class="actions">
            <a class="btn btn-dark" id="recap-sms" href="sms:{TELH}">Envoyer par SMS</a>
            <button class="btn btn-ghost" type="button" id="recap-copy">Copier</button>
            <a class="btn btn-ghost" href="tel:{TELH}">Appeler</a>
          </div>
          <p class="note">Rien n'est envoyé automatiquement : choisissez SMS, copie ou appel.</p>
        </div>
      </div>
    </div>
  </section>'''
page("contact.html", "Contacter ALL GARDEN, paysagiste à Marcoussis",
     "Contactez ALL GARDEN, paysagiste à Marcoussis (91460) : téléphone 06 10 93 16 46 ou formulaire pour préparer votre message.", contact)

# ------------------------------------------------------- MENTIONS LÉGALES
ment = f'''
  <section class="ph bg-mist" aria-labelledby="t-ph">
    <div class="wrap g2">
      <div>
        <span class="eyebrow">Informations légales</span>
        <h1 id="t-ph">Mentions légales</h1>
        <p class="lead">Qui édite ce site, et comment il fonctionne.</p>
      </div>
      <section class="doc" aria-labelledby="t-ed">
        <h2 id="t-ed">Éditeur</h2>
        <dl>
          <div><dt>Dénomination</dt><dd>ALL GARDEN</dd></div>
          <div><dt>Forme juridique</dt><dd>Société à responsabilité limitée (SARL)</dd></div>
          <div><dt>SIREN</dt><dd>788 893 477</dd></div>
          <div><dt>TVA intracommunautaire</dt><dd>FR44 788 893 477</dd></div>
          <div><dt>Capital social</dt><dd>8 000 €</dd></div>
          <div><dt>Dirigeant</dt><dd>Julien Roger Raymond VERMOND</dd></div>
          <div><dt>Adresse</dt><dd>{ADR}</dd></div>
          <div><dt>Téléphone</dt><dd><a href="tel:{TELH}">{TEL}</a></dd></div>
        </dl>
      </section>
    </div>
  </section>

  <section class="band bg-forest" aria-labelledby="t-si">
    <div class="wrap">
      <div class="doc doc-wide">
        <h2 id="t-si">Ce site</h2>
        <p>Ce site est une maquette de présentation. Il est hébergé sur GitHub Pages (GitHub, Inc.).</p>
        <p>Il n'utilise ni cookie, ni outil de mesure d'audience. Le formulaire de contact fonctionne dans votre navigateur : les informations saisies ne sont transmises à aucun serveur et servent uniquement à préparer un message que vous envoyez vous-même par SMS ou que vous copiez.</p>
        <p>Les photographies sont des illustrations des domaines d'intervention d'ALL GARDEN.</p>
        <p>Pour toute question, contactez ALL GARDEN par téléphone au {TEL}.</p>
      </div>
    </div>
  </section>'''
page("mentions-legales.html", "Mentions légales | ALL GARDEN, paysagiste à Marcoussis",
     "Mentions légales du site d'ALL GARDEN, paysagiste à Marcoussis (91) : éditeur, immatriculation et fonctionnement du site.", ment, active="")

with open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf8") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="12" fill="#12372a"/><path d="M20 30V19" stroke="#b9dc4a" stroke-width="2.6" stroke-linecap="round"/><path d="M20 21c-6 0-9-3.4-9-8.5 6 0 9 3 9 8.5Z" fill="#b9dc4a"/><path d="M20 24c5 0 8-3 8-7.5-5.2 0-8 2.6-8 7.5Z" fill="#6fae4a"/></svg>\n')
print("ok")
