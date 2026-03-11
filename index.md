---
layout: layout.njk
title: Accueil - Le Foutoir Connecté
---

<style>
.hero-banner {
  width: 100%;
  height: 380px;
  border-radius: 16px;
  object-fit: cover;
  margin-bottom: 50px;
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
}
.intro-text {
  max-width: 850px;
  margin: 0 auto 50px auto;
  font-size: 1.15rem;
  line-height: 1.8;
}
.intro-text h2 { font-size: 2rem; }
.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 35px;
  margin-top: 40px;
}
.article-card {
  background: var(--bg-card);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
}
.article-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 25px -5px rgba(0,0,0,0.1);
  border-color: #cbd5e1;
}
.article-card-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
.article-card-content {
  padding: 25px;
  flex: 1;
  display: flex;
  flex-direction: column;
}
.article-card-content h3 {
  margin: 0 0 15px 0;
  font-size: 1.35rem;
  line-height: 1.4;
}
.article-card-meta {
  font-size: 0.85rem;
  color: var(--text-muted);
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  gap: 12px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 500;
}
.article-card-meta svg { width: 14px; height: 14px; fill: currentColor; }
.article-card-summary {
  font-size: 0.95rem;
  color: #475569;
  margin-top: auto;
  line-height: 1.6;
}
</style>

<img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1200&auto=format&fit=crop" class="hero-banner" alt="Maison connectée moderne">

<div class="intro-text" data-pagefind-ignore>
  <h2>Votre maison est devenue un enfer numérique ? Rassurez-vous, c'est normal.</h2>
  <p>Tout commence généralement par une simple ampoule colorée ou une prise Wi-Fi en promotion. C'est amusant, facile à installer, et on a l'impression de vivre dans le futur. Puis, sans vraiment s'en rendre compte, on ajoute un thermostat, des caméras, des détecteurs d'ouverture sur les fenêtres... </p>
  <p>Quelques mois plus tard, la réalité technique vous rattrape : vous avez six applications différentes sur votre smartphone, votre routeur Wi-Fi est à l'agonie, et votre famille s'énerve parce la lumière du couloir refuse de s'allumer quand la box internet décide de faire une mise à jour. Félicitations, vous êtes l'heureux propriétaire d'un <strong>foutoir connecté</strong>.</p>

  <h3>Reprenez le contrôle de votre installation</h3>
  <p>J'ai passé ces dernières années à faire exactement les mêmes erreurs d'architecture. J'ai acheté du matériel incompatible, j'ai saturé mon réseau avec des gadgets dépendants du Cloud, et j'ai subi les foudres de mon entourage quand la domotique compliquait notre quotidien au lieu de le simplifier.</p>
  <p><strong>Le Foutoir Connecté</strong> est né d'une volonté très simple : vous aider à construire des fondations fiables. Ici, pas de jargon d'ingénieur incompréhensible ni de tests de gadgets sponsorisés. L'objectif est de vous fournir des <strong>guides de référence et des solutions de dépannage concrètes</strong> pour construire une vraie maison intelligente. </p>

  <p>Une installation domotique réussie doit respecter trois règles d'or :</p>
  <ol>
    <li><strong>Elle doit être invisible</strong> (le bouton mural physique doit toujours fonctionner).</li>
    <li><strong>Elle doit être locale</strong> (elle ne doit pas dépendre de serveurs en Chine ou aux États-Unis).</li>
    <li><strong>Elle doit résoudre de vrais problèmes</strong> (et non en créer de nouveaux).</li>
  </ol>
  <p>Que vous soyez un débutant cherchant à comprendre pourquoi votre ampoule clignote, ou un utilisateur régulier voulant migrer vers Home Assistant, vous trouverez ici de quoi ranger votre installation.</p>
</div>

<h2 style="text-align:center; font-size: 2.2rem; margin-top: 60px; margin-bottom: 20px;">Dossiers & Guides de Référence</h2>

<div class="articles-grid">
{% for post in collections.article | reverse %}
  <div class="article-card">
    {% if post.data.image %}
    <a href="{{ post.url }}"><img src="{{ post.data.image }}" alt="{{ post.data.title }}" class="article-card-img"></a>
    {% endif %}
    <div class="article-card-content">
      <h3><a href="{{ post.url }}">{{ post.data.title }}</a></h3>
      <div class="article-card-meta">
        <span style="display:flex; align-items:center; gap:5px;"><svg viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 0 0 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2z"/></svg> {{ post.data.date | readableDate }}</span>
        <span style="display:flex; align-items:center; gap:5px;"><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg> {{ post.content | readingTime }} min</span>
      </div>
      {% if post.data.summary %}
      <div class="article-card-summary">{{ post.data.summary }}</div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
