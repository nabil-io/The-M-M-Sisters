# The M&M Sisters — site vitrine

Portfolio one-page pour **Moudjanat & Moufidath Zime**, mannequins jumelles, ambassadrices de
marque et créatrices de contenu basées au Bénin.

Design éditorial sombre (encre + or), typographie Bodoni Moda / DM Sans, animations discrètes,
galerie photos avec visionneuse accessible, et contact direct par Instagram.

**En ligne : <https://nabil-io.github.io/The-M-M-Sisters/>**
**Dépôt : <https://github.com/nabil-io/The-M-M-Sisters>**

---

## Contenu du dossier

```
index.html            ← le site (source de référence)
standalone.html       ← version 1 seul fichier, images intégrées (~490 Ko)
build-standalone.py   ← régénère standalone.html depuis index.html
site.webmanifest      ← nom, icônes, couleur de thème
sitemap.xml           ← plan du site (une seule page)
robots.txt            ← indexation ouverte + référence au sitemap
llms.txt              ← résumé lisible par les moteurs IA (GEO)
.nojekyll             ← évite le traitement Jekyll sur GitHub Pages
assets/               ← photos WebP optimisées, icônes, image de partage og-cover.jpg
```

## Ouvrir le site

**En local (recommandé)** — l'ouverture par double-clic fonctionne aussi, mais un petit serveur
évite les restrictions de fichiers locaux :

```powershell
python -m http.server 8000
```

Puis ouvrir <http://localhost:8000>.

**Version portable** : `standalone.html` contient tout (photos, icônes) dans un seul fichier.
Pratique pour envoyer par mail ou WhatsApp. Pour la régénérer après une modification :

```powershell
python build-standalone.py
```

## Mise en ligne

### GitHub Pages (actif)

Le site est publié automatiquement depuis la branche **`gh-pages`** à chaque `git push` :

<https://nabil-io.github.io/The-M-M-Sisters/>

```powershell
git add -A
git commit -m "Mise à jour du site"
git push origin main
git push origin main:gh-pages   # ← déclenche la publication
```

Réglage côté GitHub (déjà fait) : *Settings → Pages → Source : Deploy from a branch →
Branche `gh-pages` / dossier `/ (root)`*. Le déploiement prend 30 à 90 secondes ; l'état est
visible dans l'onglet **Actions** du dépôt.

### Autres hébergeurs

N'importe quel hébergement statique convient : Netlify, Vercel, Cloudflare Pages, ou un simple
dossier FTP. Il suffit d'envoyer `index.html`, `assets/`, `site.webmanifest`, `robots.txt`,
`sitemap.xml` et `llms.txt`.

---

## Ce qui a été corrigé

### Structure & validité

- Le fichier d'origine était **invalide** : un `<head>` fermé trop tôt, puis `<title>`, `<style>`,
  `<header>` et `<main>` déclarés à l'intérieur du `<body>` ; `<meta charset=utf8>` non quotée ;
  pas de `lang`. Tout est réécrit en HTML5 propre (`<!doctype html>`, `lang="en"`, charset UTF-8).
- Un bloc CSS injecté au tout début forçait `background:#fff`, `font:14px`, du `padding` sur `:root`
  et `color-scheme:light` — il cassait le thème sombre. Supprimé.
- La logique « pleine largeur » du ticker reposait sur `margin-inline: calc(50% - 50vw)` avec un
  `body` paddingé : remplacée par une structure `.wrap` propre, plus de risque de débordement.
- `overflow-x: hidden` sur `body` masquait les vrais débordements : vérifié à 390 / 768 / 1280 px,
  aucun débordement horizontal.

### Bugs d'interface

- **Navigation mobile** : sous 520 px, le lien « About » était purement supprimé. Remplacé par un
  vrai menu plein écran (bouton accessible, `aria-expanded`, fermeture par Échap, retour du focus,
  blocage du scroll, contenu arrière en `inert`).
- **Visionneuse** : le focus n'était pas déplacé (la visionneuse restait `visibility:hidden` au
  moment du `.focus()`), pas de piège à focus, pas de blocage du scroll de fond, clic extérieur
  partiellement inopérant, flèches qui débordaient sur petit écran. Tout est corrigé : focus rendu
  au bon moment, `Tab` piégé, Échap/flèches, swipe tactile, compteur `01 / 04`, clic sur le fond,
  focus restitué à la vignette d'origine.
- **Bouton « Copier »** : le fallback par sélection de texte était fragile. Remplacé par un
  `textarea` + `execCommand`, avec confirmation visuelle et annonce `aria-live`.
- **Phrase d'accroche** : `Two sisters.One creative vision.` sans espace pour les lecteurs d'écran
  → corrigé.
- **Scrollspy** : ajout de l'état actif `aria-current` sur la navigation au défilement.
- **Barre de progression** de lecture et en-tête qui se densifie au scroll (avant : rien).

### Performance & images

- 8 photos en base64 JPEG dans le HTML : **607 Ko** → **317 Ko** en WebP (qualité 76–80,
  redimensionnées pour l'affichage réel, léger étalonnage chaud pour homogénéiser les sources).
- Attributs `width`/`height` (pas de saut de mise en page), `loading="lazy"` + `decoding="async"`
  hors héros, `fetchpriority="high"` sur les deux portraits du héros.
- Version autonome : **855 Ko → 490 Ko**.
- Aucune dépendance JS, aucun framework, aucune police en local : deux requêtes Google Fonts
  (`display=swap`).

### Référencement & partage (SEO / GEO)

- `<title>` et meta description rédigés, `robots`, `theme-color`, `lang`.
- Open Graph + Twitter Card complets, avec une image de partage **1200 × 630** générée
  (`assets/og-cover.jpg`).
- Données structurées **JSON-LD** (`WebSite` + `ProfilePage` + deux `Person` avec leurs profils
  Instagram).
- Favicon SVG inline, icônes 180/192/512, `site.webmanifest`.
- `canonical`, `og:url` et image de partage en **URL absolue**, `sitemap.xml`, `robots.txt`
  (avec la ligne `Sitemap:`) et `llms.txt` (résumé pour les moteurs IA).

### Accessibilité

- Lien d'évitement « Skip to content », focus visibles, contrastes vérifiés :
  crème/encre **16,5:1**, texte secondaire **8,4:1**, or **7,9:1**.
- Titres hiérarchisés (un seul `h1`), textes alternatifs, décorations en `aria-hidden`,
  boutons avec libellés explicites, dialogue `aria-modal`, région `aria-live`.
- Respect de `prefers-reduced-motion` (animations et parallaxe désactivés) et styles d'impression.

---

## Améliorations de rendu

- **Héros repensé en deux colonnes** : accroche, promesse et boutons visibles dès le premier écran
  (avant, les CTA passaient sous la ligne de flottaison), portraits jumelés à droite avec les
  Initiales « M » en filigrane et un médaillon « & ».
- Composition éditoriale : numérotation des sections (`01 → 04`), filets or, légendes, badges,
  bandeau défilant avec masque et pause au survol.
- Cartes de profil, frise de faits (Bénin / duo ou solo / beauty-fashion-lifestyle), galerie
  décalée avec compteurs, parcours de collaboration en 3 étapes, cartes de contact avec compte
  partagé mis en avant.
- Micro-interactions : révélation au scroll, zoom photo, soulignés animés, boutons à remplissage
  progressif, grain photographique très léger, parallaxe limitée aux pointeurs fins.
- Pied de page structuré, année automatique, retour en haut.

## Personnalisation

1. **Domaine personnalisé** — le site vit déjà sur `https://nabil-io.github.io/The-M-M-Sisters/`.
   Pour utiliser un domaine propre :
   - créer un fichier `CNAME` à la racine contenant le domaine (ex. `themmsisters.com`) ;
   - chez le registrar : `CNAME` pour `www` → `nabil-io.github.io`, et 4 enregistrements `A`
     pour le domaine racine → `185.199.108.153`, `.109.153`, `.110.153`, `.111.153` ;
   - *Settings → Pages → Custom domain*, puis cocher **Enforce HTTPS** ;
   - remplacer `https://nabil-io.github.io/The-M-M-Sisters/` par la nouvelle URL dans
     `index.html` (`canonical`, `og:url`, `og:image`, `twitter:image`, JSON-LD), `sitemap.xml`
     et la ligne `Sitemap:` de `robots.txt`, puis relancer `python build-standalone.py`.

2. **Photos** — pour remplacer une image, garder le même nom de fichier dans `assets/`
   (ratio 3:4 conseillé) puis relancer `python build-standalone.py`.

3. **Contenus** — les textes sont en anglais (le site d'origine l'était). Si une version française
   est souhaitée, prévoir deux pages ou un sélecteur de langue.

4. **Contact** — Instagram uniquement pour l'instant. Si une adresse e-mail ou WhatsApp doit être
   ajoutée, créer une carte supplémentaire dans `#contact`.

## Vérifications effectuées

- Rendu et mesures de mise en page à 390 / 768 / 1000 / 1280 px : aucun débordement, aucune
  troncature de texte, grilles et titres corrects.
- Parcours testés : menu mobile (ouverture, Échap, focus), visionneuse (ouverture, flèches,
  Échap, restitution du focus, blocage du scroll), copie d'un handle, image de partage.
- Console navigateur : aucune erreur ; toutes les images se chargent (version dossier et version
  autonome).
- Contrastes calculés, attributs `alt`/`aria` contrôlés, un seul `h1`, pas d'ID dupliqué.
- Site en ligne vérifié sur GitHub Pages : HTTP 200, titre et 8 photos servis correctement,
  `Content-Type: image/webp` sur les visuels.
