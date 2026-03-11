---
layout: layout.njk
title: Recherche
permalink: /pages/recherche/
---
<style>
  .search-page { max-width: 800px; margin: 0 auto; min-height: 50vh; }
  .search-page h1 { font-size: 2.5rem; text-align: center; margin-bottom: 40px; }
  /* Integration Pagefind CSS customizations */
  .pagefind-ui__search-input { border-radius: 8px !important; border: 1px solid #cbd5e1 !important; font-family: inherit !important; }
  .pagefind-ui__result-title { color: var(--primary-dark) !important; font-weight: bold !important; }
  .pagefind-ui__result-excerpt { color: var(--text-muted) !important; }
</style>

<div class="search-page">
  <h1>Rechercher un article</h1>
  
  <link href="/pagefind/pagefind-ui.css" rel="stylesheet">
  <script src="/pagefind/pagefind-ui.js"></script>
  
  <div id="search"></div>
  
  <script>
      window.addEventListener('DOMContentLoaded', (event) => {
          if (typeof PagefindUI !== 'undefined') {
            new PagefindUI({ 
              element: "#search", 
              showSubResults: true, 
              showImages: false,
              translations: {
                placeholder: "Rechercher (ex: Zigbee, Wi-Fi, Shelly...)",
                clear_search: "Effacer",
                load_more: "Voir plus de résultats",
                search_label: "Recherche sur le site",
                filters_label: "Filtres",
                zero_results: "Aucun résultat trouvé pour [SEARCH_TERM]",
                many_results: "[COUNT] résultats pour [SEARCH_TERM]",
                one_result: "[COUNT] résultat pour [SEARCH_TERM]"
              }
            });
          } else {
             document.getElementById('search').innerHTML = "<p style='text-align:center; color: #64748b;'><em>Le moteur de recherche est en cours d'indexation (disponible dans quelques instants).</em></p>";
          }
      });
  </script>
</div>
