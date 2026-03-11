module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("CNAME");
  
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

  return {
    dir: {
      input: ".",
      output: "_site"
    }
  };
};
