"""Redimensionne et compresse les images retenues. Usage : python3 optimiser_images.py DOSSIER_SOURCES [DOSSIER_SORTIE]"""
import os, sys
from PIL import Image

SRC = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "..", "images")
# nom de sortie : (fichier source, largeur max, qualité)
MAP = {
    "hero-jardin-allee": ("7-entretien-jardin.jpg", 1408, 76),
    "creation-espace-vert": ("4-creation-espace-vert.jpg", 800, 78),
    "tonte-pelouse": ("2-tonte.jpg", 800, 78),
    "elagage-chene": ("1-hero-elagage-chene.jpg", 800, 78),
    "elagage-cordiste": ("1-elagage-chene.jpg", 800, 78),
    "muret-pierre-escalier": ("maconerie-paysagere.jpg", 1000, 78),
    "terrasse-bois": ("chantier-terrasse-en-bois.jpg", 800, 78),
    "allee-pierre-muret": ("allee-paves-carrelage-exterieure.jpg", 800, 78),
    "allee-dallee-soir": ("chantier-allee-dallee.jpg", 800, 78),
    "conception-tablette": ("conception-chantier.jpg", 1000, 78),
    "plantation": ("6-plantation.jpg", 800, 78),
    "nivellement-terrain": ("8-nivellement.jpg", 800, 78),
    "terrassement-fouille": ("7-terrassement.jpg", 800, 78),
    "entretien-massif": ("4-desherbage.jpg", 800, 78),
    "tondeuse-rouge": ("3-entretien-general.jpg", 800, 78),
    "ramassage-feuilles": ("5-feuilles.jpg", 800, 78),
    "dechets-verts": ("7-dechets-verts.jpg", 800, 78),
    "dessouchage": ("3-dessouchage.jpg", 800, 78),
    "taille-haie": ("4-taille-haies.jpg", 800, 78),
    "robot-tonte": ("robot-tonte-de-pelouse.jpg", 1000, 78),
    "nettoyage-jardin": ("10-nettoyage.jpg", 800, 78),
}
os.makedirs(OUT, exist_ok=True)
tot = 0
for name, (f, w, q) in MAP.items():
    im = Image.open(os.path.join(SRC, f)).convert("RGB")
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    p = os.path.join(OUT, name + ".jpg")
    im.save(p, quality=q, optimize=True, progressive=True)
    s = os.path.getsize(p)
    tot += s
    print(f"{name}.jpg {im.size[0]}x{im.size[1]} {s // 1024} Ko")
print("total", tot // 1024, "Ko")
