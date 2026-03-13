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

  eleventyConfig.addCollection("tagList", function(collectionApi) {
    const tags = new Set();
    const slugify = (text) => text.toString().toLowerCase().replace(/\s+/g, '-').replace(/[^\w\-]+/g, '').replace(/\-\-+/g, '-').replace(/^-+/, '').replace(/-+$/, '');
    collectionApi.getAll().forEach(item => {
      if (item.data.tags) {
        item.data.tags.forEach(tag => tags.add(slugify(tag)));
      }
    });
    return Array.from(tags).filter(t => !["article", "post", "all"].includes(t));
  });

  return {
    dir: {
      input: ".",
      output: "_site"
    }
  };
};
