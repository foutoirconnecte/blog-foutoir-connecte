module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("CNAME");
  eleventyConfig.addPassthroughCopy("images");
  
// Filtre pour limiter le nombre d'éléments d'un tableau
  eleventyConfig.addFilter("limit", (array, limit) => {
    return array.slice(0, limit);
  });

  // Filtre pour fusionner deux tableaux (au cas où Nunjucks rechigne)
  eleventyConfig.addFilter("concat", (array1, array2) => {
    return array1.concat(array2);
  });






// Filtre pour mélanger un tableau (Fisher-Yates shuffle)
  eleventyConfig.addFilter("shuffle", (array) => {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
  });

  // Filtre pour exclure des articles déjà sélectionnés par leur URL
  eleventyConfig.addFilter("excludeUsed", (collection, usedPosts) => {
    const usedUrls = usedPosts.map(p => p.url);
    return collection.filter(post => !usedUrls.includes(post.url));
  });

  // Filtre pour trouver des articles ayant au moins un tag en commun
  eleventyConfig.addFilter("similarTags", (collection, currentTags) => {
    if (!currentTags) return [];
    return collection.filter(post => {
      return post.data.tags && post.data.tags.some(tag => currentTags.includes(tag));
    });
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
