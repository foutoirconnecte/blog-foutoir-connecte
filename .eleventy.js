module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("CNAME");
  eleventyConfig.addPassthroughCopy("images");
  
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
    const slugify = (text) => text.toString().toLowerCase()
      .replace(/[àáâãäå]/g, 'a')
      .replace(/[éèêë]/g, 'e')
      .replace(/[íìîï]/g, 'i')
      .replace(/[óòôõö]/g, 'o')
      .replace(/[úùûü]/g, 'u')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '');

    const tags = new Map();
    collectionApi.getAll().forEach(item => {
      if (item.data.tags) {
        item.data.tags.forEach(tag => {
          const slug = slugify(tag);
          if (!tags.has(slug)) {
            tags.set(slug, tag);
          }
        });
      }
    });
    // On retourne une liste d'objets pour pouvoir accéder au slug et à la forme originale
    return Array.from(tags.entries())
      .filter(([slug, tag]) => !["article", "post", "all"].includes(tag.toLowerCase()))
      .map(([slug, tag]) => ({ slug, tag }));
  });

  return {
    dir: {
      input: ".",
      output: "_site"
    }
  };
};
