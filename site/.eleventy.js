module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("CNAME");
  eleventyConfig.addPassthroughCopy("images");
  


// FILTRE pour selectionner les articles à placer sous l'article en cours de lecture 
  eleventyConfig.addFilter("getRelatedPosts", (collection, currentUrl, currentTags) => {
    if (!collection) return [];

    // 1. On exclut l'article en cours de lecture
    const otherPosts = collection.filter(post => post.url !== currentUrl);

    // 2. Les 5 plus récents (11ty trie du plus vieux au plus récent par défaut, donc on inverse)
    const recentPosts = [...otherPosts].reverse().slice(0, 5);
    const recentUrls = recentPosts.map(p => p.url);

    // 3. Les 5 similaires (par tags)
    let similarPosts = [];
    if (currentTags) {
      // On s'assure d'avoir un tableau et on ignore le tag générique 'article'
      const tagsArray = Array.isArray(currentTags) ? currentTags : [currentTags];
      const meaningfulTags = tagsArray.filter(t => t !== 'article'); 

      const remainingForSimilar = otherPosts.filter(p => !recentUrls.includes(p.url));
      
      similarPosts = remainingForSimilar.filter(post => {
        const pTags = post.data.tags || [];
        const pTagsArray = Array.isArray(pTags) ? pTags : [pTags];
        return pTagsArray.some(tag => meaningfulTags.includes(tag));
      });
      
      // Mélange aléatoire (Fisher-Yates simplifié)
      similarPosts = similarPosts.sort(() => Math.random() - 0.5).slice(0, 5);
    }
    const similarUrls = similarPosts.map(p => p.url);

    // 4. Les 5 aléatoires dans ce qu'il reste
    const usedUrls = [...recentUrls, ...similarUrls];
    const remainingForRandom = otherPosts.filter(p => !usedUrls.includes(p.url));
    const randomPosts = remainingForRandom.sort(() => Math.random() - 0.5).slice(0, 5);

    // 5. On fusionne tout et on renvoie à Nunjucks
    return [...recentPosts, ...similarPosts, ...randomPosts];
  });









  // Filtre de date
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return new Intl.DateTimeFormat('fr-FR', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    }).format(new Date(dateObj));
  });

  // Filtre de temps de lecture
  eleventyConfig.addFilter("readingTime", (content) => {
    const textOnly = content.replace(/(<([^>]+)>)/gi, "");
    const wordCount = textOnly.split(/\s+/).length;
    const readingTime = Math.ceil(wordCount / 220); // 220 mots par minute
    return readingTime;
  });

  eleventyConfig.addFilter("slugify", (text) => {
    return text.toString().toLowerCase()
      .replace(/[àáâãäå]/g, 'a')
      .replace(/[éèêë]/g, 'e')
      .replace(/[íìîï]/g, 'i')
      .replace(/[óòôõö]/g, 'o')
      .replace(/[úùûü]/g, 'u')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '');
  });

  eleventyConfig.addCollection("tagList", function(collectionApi) {
    const slugifyFilter = eleventyConfig.getFilter("slugify");
    const uniqueTags = new Map();
    collectionApi.getAll().forEach(item => {
      if (item.data.tags) {
        item.data.tags.forEach(tag => {
          const slug = slugifyFilter(tag);
          if (!uniqueTags.has(slug)) {
            uniqueTags.set(slug, tag.toLowerCase());
          }
        });
      }
    });
    return Array.from(uniqueTags.values()).filter(t => !["article", "post", "all"].includes(t.toLowerCase()));
  });

  return {
    dir: {
      input: ".",
      output: "_site"
    }
  };
};
