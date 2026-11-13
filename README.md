# The M&M Sisters — site vitrine

Portfolio one-page pour **Moudjanat & Moufidath Zime**, mannequins jumelles, ambassadrices de
marque et créatrices de contenu basées au Bénin.

Design éditorial sombre (encre + or), typographie Bodoni Moda / DM Sans, animations discrètes,
galerie photos avec visionneuse accessible, et contact direct par Instagram.

---

## Contenu du dossier

```
index.html            ← le site (source de référence)
standalone.html       ← version 1 seul fichier, images intégrées (~490 Ko)
build-standalone.py   ← régénère standalone.html depuis index.html
site.webmanifest      ← nom, icônes, couleur de thème
robots.txt            ← indexation ouverte
llms.txt              ← résumé lisible par les moteurs IA (GEO)
assets/               ← photos WebP optimisées, icônes, image de partage og-cover.jpg
```

## Ouvrir le site

**En local (recommandé)** — l'ouverture par double-clic fonctionne aussi, mais un petit serveur
évite les restrictions de fichiers locaux :

```powershell
cd "C:\Bruillon\moudja ma femme"
python -m http.server 8000
```

Puis ouvrir <http://localhost:8000>.

**Version portable** : `standalone.html` contient tout (photos, icônes) dans un seul fichier.
Pratique pour envoyer par mail ou WhatsApp. Pour la régénérer après une modification :

```powershell
python build-standalone.py
```

## Mise en ligne

N'importe quel hébergement statique convient : Netlify, Vercel, GitHub Pages, Cloudflare Pages,
ou un simple dossier FTP. Il suffit d'envoyer `index.html`, `assets/`, `site.webmanifest`,
`robots.txt` et `llms.txt`.

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
- `robots.txt`, `llms.txt` (résumé pour les moteurs IA) et liens internes explicites.

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

## À personnaliser avant mise en ligne

1. **Domaine** — dès que l'URL définitive est connue, ajouter dans `<head>` :
   ```html
   <link rel="canonical" href="https://VOTRE-DOMAINE/">
   <meta property="og:url" content="https://VOTRE-DOMAINE/">
   <meta property="og:image" content="https://VOTRE-DOMAINE/assets/og-cover.jpg">
   <meta name="twitter:image" content="https://VOTRE-DOMAINE/assets/og-cover.jpg">
   ```
   Les URLs actuelles de `og:image` sont relatives (volontairement) : la plupart des réseaux
   sociaux exigent une URL absolue.
2. **Sitemap** — créer `sitemap.xml` une fois le domaine connu :
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
     <url><loc>https://VOTRE-DOMAINE/</loc><lastmod>2026-11-13</lastmod></url>
   </urlset>
   ```
   puis ajouter `Sitemap: https://VOTRE-DOMAINE/sitemap.xml` à la fin de `robots.txt`.
3. **Photos** — pour remplacer une image, garder le même nom de fichier dans `assets/`
   (ratio 3:4 conseillé) puis relancer `python build-standalone.py`.
4. **Contenus** — les textes sont en anglais (le site d'origine l'était). Si une version française
   est souhaitée, prévoir deux pages ou un sélecteur de langue.
5. **Contact** — Instagram uniquement pour l'instant. Si une adresse e-mail ou WhatsApp doit être
   ajoutée, créer une carte supplémentaire dans `#contact`.

## Vérifications effectuées

- Rendu et mesures de mise en page à 390 / 768 / 1000 / 1280 px : aucun débordement, aucune
  troncature de texte, grilles et titres corrects.
- Parcours testés : menu mobile (ouverture, Échap, focus), visionneuse (ouverture, flèches,
  Échap, restitution du focus, blocage du scroll), copie d'un handle, image de partage.
- Console navigateur : aucune erreur ; toutes les images se chargent (version dossier et version
  autonome).
- Contrastes calculés, attributs `alt`/`aria` contrôlés, un seul `h1`, pas d'ID dupliqué.
