/**
 * Search Intelligence Module
 * Advanced NLP, intent recognition, synonym handling, and smart ranking
 */

class SearchIntelligence {
  constructor() {
    // Multi-language synonym dictionary with regional variations
    this.synonyms = {
      // Floor types (all regional variations)
      'laminate': ['laminaat', 'laminat', 'laminated flooring', 'laminate floor', 'stratifié'],
      'vinyl': ['pvc', 'luxury vinyl', 'lvt', 'vinyl plank', 'vinyl planks', 'vinyle'],
      'parquet': ['parket', 'parkett', 'hardwood', 'wood flooring', 'houten vloer'],
      'wood': ['wooden', 'timber', 'hout', 'holz', 'bois', 'legno', 'madera'],
      'tile': ['tiles', 'tegel', 'tegels', 'fliese', 'fliesen', 'carrelage', 'piastrelle', 'azulejo'],
      'stone': ['steen', 'stein', 'natural stone', 'marble', 'granite', 'pierre', 'pietra', 'piedra'],
      
      // Products & care (regional differences)
      'cleaner': ['cleaning', 'clean', 'reiniger', 'reinigung', 'schoonmaakmiddel', 'schoonmaak', 'nettoyant', 'detergente', 'limpiador'],
      'sealer': ['sealing', 'seal', 'verzegeling', 'versiegelung', 'scellant', 'sigillante', 'sellador', 'protection'],
      'oil': ['olie', 'öl', 'wood oil', 'floor oil', 'huile', 'olio', 'aceite'],
      'wax': ['was', 'wachs', 'floor wax', 'cire', 'cera'],
      'polish': ['polisher', 'polijsten', 'polieren', 'polir', 'lucidare', 'pulir'],
      'adhesive': ['glue', 'lijm', 'kleber', 'colle', 'colla', 'pegamento', 'bonding'],
      'underlay': ['underlayment', 'ondervloer', 'unterlage', 'sous-couche', 'sottofondi'],
      'varnish': ['vernis', 'lak', 'lack', 'vernice', 'barniz'],
      
      // Characteristics (with regional spelling)
      'waterproof': ['water resistant', 'waterdicht', 'wasserdicht', 'water proof', 'étanche', 'impermeabile', 'impermeable'],
      'scratch resistant': ['scratch proof', 'krasbestendig', 'kratzfest', 'résistant aux rayures', 'antigraffio', 'resistente a los arañazos'],
      'easy to install': ['diy', 'click system', 'gemakkelijk te leggen', 'einfach zu verlegen', 'facile à poser', 'facile da installare', 'fácil de instalar'],
      'durable': ['strong', 'heavy duty', 'duurzaam', 'langlebig', 'robust', 'durable', 'durevole', 'duradero'],
      'eco friendly': ['ecological', 'sustainable', 'milieuvriendelijk', 'umweltfreundlich', 'écologique', 'ecologico', 'ecológico'],
      
      // Brands (normalize regional variations)
      'bona': ['bona floor care', 'bona products', 'bona vloeronderhoud'],
      'woca': ['woca denmark', 'woca oil', 'woca olie'],
      'lithofin': ['lithofin stone care', 'lithofin natuursteen'],
      'hmk': ['hmk moeller', 'hmk stone care'],
      'loba': ['loba wakol', 'loba vloeren'],
      'quick-step': ['quick step', 'quickstep'],
      'blue dolphin': ['bluedolphin', 'blue dolfijn'],
      
      // Colors/finishes (regional names)
      'oak': ['eik', 'eiche', 'oak wood', 'chêne', 'quercia', 'roble'],
      'walnut': ['noot', 'walnuss', 'walnut wood', 'noyer', 'noce', 'nogal'],
      'white': ['wit', 'weiss', 'whitewashed', 'blanc', 'bianco', 'blanco'],
      'grey': ['gray', 'grijs', 'grau', 'gris', 'grigio'],
      'brown': ['bruin', 'braun', 'brun', 'marrone', 'marrón'],
      'black': ['zwart', 'schwarz', 'noir', 'nero', 'negro'],
      'natural': ['naturel', 'natur', 'natural finish', 'naturale', 'natural'],
      'matt': ['matte', 'mat', 'matt finish'],
      'gloss': ['glossy', 'high gloss', 'glanzend', 'glänzend', 'brillant', 'lucido', 'brillante'],
      'beige': ['beige', 'crème', 'crema'],
      
      // Room-specific terms (Belgium has unique terms)
      'kitchen': ['keuken', 'küche', 'cuisine', 'cucina', 'cocina'],
      'bathroom': ['badkamer', 'bad', 'salle de bain', 'bagno', 'baño', 'douche', 'wc'],
      'living room': ['woonkamer', 'salon', 'wohnzimmer', 'soggiorno', 'sala de estar'],
      'bedroom': ['slaapkamer', 'schlafzimmer', 'chambre', 'camera da letto', 'dormitorio'],
      'hallway': ['gang', 'hal', 'flur', 'couloir', 'corridoio', 'pasillo', 'entree'],
      
      // Actions (regional verb forms)
      'install': ['installation', 'leggen', 'verlegen', 'installeren', 'poser', 'installare', 'instalar'],
      'maintain': ['maintenance', 'onderhoud', 'onderhouden', 'pflege', 'pflegen', 'entretien', 'manutenzione', 'mantenimiento'],
      'clean': ['cleaning', 'schoonmaken', 'reinigen', 'nettoyer', 'pulire', 'limpiar'],
      'protect': ['protection', 'beschermen', 'schützen', 'protéger', 'proteggere', 'proteger'],
      'restore': ['restoration', 'herstellen', 'wiederherstellen', 'restaurer', 'restaurare', 'restaurar']
    };

    // Question patterns for intent detection
    this.questionPatterns = {
      how: /^(how|hoe|wie)\s+(to|can|do|te)\s+/i,
      what: /^(what|wat|welke|welches?)\s+/i,
      which: /^(which|welke|welches?)\s+/i,
      where: /^(where|waar|wo)\s+/i,
      when: /^(when|wanneer|wann)\s+/i,
      why: /^(why|waarom|warum)\s+/i,
      best: /\b(best|beste|besten?)\b/i,
      cheap: /\b(cheap|goedkoop|billig|affordable|budget)\b/i,
      recommend: /\b(recommend|aanbevelen|empfehlen|suggestion)\b/i
    };

    // Problem keywords that indicate problem-solving intent
    this.problemKeywords = [
      'remove', 'fix', 'repair', 'clean', 'maintain', 'protect', 'prevent',
      'verwijder', 'herstel', 'repareer', 'schoon', 'onderhoud', 'bescherm',
      'entfernen', 'reparieren', 'reinigen', 'pflegen', 'schützen',
      'stain', 'scratch', 'damage', 'crack', 'squeak', 'water damage',
      'vlek', 'kras', 'schade', 'barst', 'piepen', 'waterschade'
    ];

    // Room types for contextual filtering
    this.roomTypes = {
      kitchen: ['keuken', 'küche', 'cuisine', 'cucina'],
      bathroom: ['badkamer', 'bad', 'salle de bain', 'bagno'],
      living: ['woonkamer', 'wohnzimmer', 'salon', 'soggiorno', 'living room'],
      bedroom: ['slaapkamer', 'schlafzimmer', 'chambre', 'camera da letto'],
      hallway: ['gang', 'flur', 'couloir', 'corridoio', 'entrance'],
      outdoor: ['buiten', 'außen', 'extérieur', 'esterno', 'terrace', 'balcony']
    };

    // Usage characteristics
    this.usageCharacteristics = {
      'pet-friendly': ['pet safe', 'huisdier', 'haustier', 'animal', 'dog', 'cat'],
      'underfloor heating': ['vloerverwarming', 'fußbodenheizung', 'chauffage sol', 'ufh'],
      'high traffic': ['commercial', 'heavy duty', 'zwaar gebruik', 'stark beansprucht'],
      'moisture resistant': ['waterproof', 'water resistant', 'vochtbestendig', 'feuchtigkeitsbeständig']
    };
  }

  /**
   * Analyze search query and return enhanced search parameters
   */
  analyzeQuery(query) {
    const analysis = {
      original: query,
      normalized: this.normalizeQuery(query),
      intent: this.detectIntent(query),
      synonyms: this.expandSynonyms(query),
      room: this.detectRoom(query),
      characteristics: this.detectCharacteristics(query),
      isQuestion: this.isQuestion(query),
      isProblem: this.isProblem(query),
      brands: this.detectBrands(query),
      colors: this.detectColors(query),
      priceRange: this.extractPriceRange(query)
    };

    return analysis;
  }

  /**
   * Normalize query: lowercase, trim, remove special chars
   */
  normalizeQuery(query) {
    return query
      .toLowerCase()
      .trim()
      .replace(/[^\w\s€$-]/g, ' ')
      .replace(/\s+/g, ' ');
  }

  /**
   * Detect user intent
   */
  detectIntent(query) {
    const normalized = this.normalizeQuery(query);

    // Check for question words
    for (const [type, pattern] of Object.entries(this.questionPatterns)) {
      if (pattern.test(normalized)) {
        return type;
      }
    }

    // Check for problem-solving
    if (this.isProblem(normalized)) {
      return 'problem-solving';
    }

    // Check for comparison
    if (/\bvs\b|\bversus\b|\bor\b|\bof\b/.test(normalized)) {
      return 'comparison';
    }

    // Check for purchase intent
    if (/\bbuy\b|\bkoop\b|\bkaufen\b|\bpurchase\b/.test(normalized)) {
      return 'purchase';
    }

    return 'search';
  }

  /**
   * Check if query is a question
   */
  isQuestion(query) {
    return Object.values(this.questionPatterns).some(pattern => pattern.test(query)) ||
           query.includes('?');
  }

  /**
   * Check if query indicates a problem
   */
  isProblem(query) {
    const normalized = this.normalizeQuery(query);
    return this.problemKeywords.some(keyword => normalized.includes(keyword));
  }

  /**
   * Expand query with synonyms
   */
  expandSynonyms(query) {
    const normalized = this.normalizeQuery(query);
    const expanded = new Set([normalized]);

    for (const [base, syns] of Object.entries(this.synonyms)) {
      // Check if query contains base term or any synonym
      if (normalized.includes(base) || syns.some(syn => normalized.includes(syn))) {
        expanded.add(base);
        syns.forEach(syn => expanded.add(syn));
      }
    }

    return Array.from(expanded);
  }

  /**
   * Detect room type from query
   */
  detectRoom(query) {
    const normalized = this.normalizeQuery(query);

    for (const [room, keywords] of Object.entries(this.roomTypes)) {
      if (keywords.some(keyword => normalized.includes(keyword)) || 
          normalized.includes(room)) {
        return room;
      }
    }

    return null;
  }

  /**
   * Detect usage characteristics
   */
  detectCharacteristics(query) {
    const normalized = this.normalizeQuery(query);
    const characteristics = [];

    for (const [char, keywords] of Object.entries(this.usageCharacteristics)) {
      if (keywords.some(keyword => normalized.includes(keyword)) ||
          normalized.includes(char)) {
        characteristics.push(char);
      }
    }

    return characteristics;
  }

  /**
   * Detect brand mentions
   */
  detectBrands(query) {
    const normalized = this.normalizeQuery(query);
    const brands = [
      'lithofin', 'hmk', 'lecol', 'woca', 'bona', 'loba', 
      'floorservice', 'blue dolphin', 'dr. schutz', 'blanchon',
      'quick-step', 'pergo', 'berry alloc', 'parador', 'haro',
      'osmo', 'treatex', 'rubio monocoat', 'pallmann'
    ];

    return brands.filter(brand => normalized.includes(brand));
  }

  /**
   * Detect color/finish mentions
   */
  detectColors(query) {
    const normalized = this.normalizeQuery(query);
    const colors = [];

    const colorMap = {
      'oak': ['eik', 'eiche'],
      'walnut': ['noot', 'walnuss'],
      'white': ['wit', 'weiss'],
      'grey': ['grijs', 'grau', 'gray'],
      'brown': ['bruin', 'braun'],
      'black': ['zwart', 'schwarz'],
      'natural': ['naturel', 'natur']
    };

    for (const [color, variants] of Object.entries(colorMap)) {
      if (normalized.includes(color) || variants.some(v => normalized.includes(v))) {
        colors.push(color);
      }
    }

    return colors;
  }

  /**
   * Extract price range from query
   */
  extractPriceRange(query) {
    const pricePatterns = [
      /(?:under|below|less than|max|maximum)\s*€?\s*(\d+)/i,
      /€?\s*(\d+)\s*(?:to|-|tot)\s*€?\s*(\d+)/i,
      /(?:over|above|more than|min|minimum)\s*€?\s*(\d+)/i
    ];

    for (const pattern of pricePatterns) {
      const match = query.match(pattern);
      if (match) {
        if (pattern.source.includes('under|below')) {
          return { max: parseInt(match[1]) };
        } else if (pattern.source.includes('to|-|tot')) {
          return { min: parseInt(match[1]), max: parseInt(match[2]) };
        } else if (pattern.source.includes('over|above')) {
          return { min: parseInt(match[1]) };
        }
      }
    }

    return null;
  }

  /**
   * Rank search results based on relevance
   */
  rankResults(results, query, analysis) {
    return results.map(product => {
      let score = 0;

      // Exact match in title (highest priority)
      if (product.title.toLowerCase().includes(query.toLowerCase())) {
        score += 100;
      }

      // Synonym match in title
      if (analysis.synonyms.some(syn => 
        product.title.toLowerCase().includes(syn.toLowerCase())
      )) {
        score += 80;
      }

      // Brand match
      if (analysis.brands.length > 0 && 
          analysis.brands.some(brand => 
            product.vendor?.toLowerCase().includes(brand.toLowerCase())
          )) {
        score += 60;
      }

      // Tag matches
      const productTags = product.tags || [];
      if (analysis.characteristics.some(char => 
        productTags.some(tag => tag.toLowerCase().includes(char.toLowerCase()))
      )) {
        score += 50;
      }

      // Room match
      if (analysis.room && 
          productTags.some(tag => tag.toLowerCase().includes(analysis.room))) {
        score += 40;
      }

      // Price range match
      if (analysis.priceRange) {
        const price = product.price / 100;
        const inRange = (!analysis.priceRange.min || price >= analysis.priceRange.min) &&
                       (!analysis.priceRange.max || price <= analysis.priceRange.max);
        if (inRange) score += 30;
      }

      // Availability boost
      if (product.available) {
        score += 20;
      }

      // New product boost (if has "new" tag)
      if (productTags.some(tag => tag.toLowerCase() === 'new')) {
        score += 10;
      }

      return { ...product, relevanceScore: score };
    }).sort((a, b) => b.relevanceScore - a.relevanceScore);
  }

  /**
   * Generate smart search suggestions
   */
  generateSmartSuggestions(query, analysis) {
    const suggestions = [];

    // If it's a question, suggest switching to product search
    if (analysis.isQuestion) {
      suggestions.push({
        type: 'info',
        text: 'Looking for how-to guides? Check our learning center',
        action: '/pages/learning-center'
      });
    }

    // If problem-solving, suggest care products
    if (analysis.isProblem) {
      suggestions.push({
        type: 'category',
        text: 'Browse all floor care products',
        action: '/collections/floor-care'
      });
    }

    // If room detected, suggest room-specific collection
    if (analysis.room) {
      suggestions.push({
        type: 'category',
        text: `See all ${analysis.room} flooring options`,
        action: `/collections/${analysis.room}-flooring`
      });
    }

    // If brand detected, suggest brand collection
    if (analysis.brands.length > 0) {
      analysis.brands.forEach(brand => {
        suggestions.push({
          type: 'brand',
          text: `View all ${brand} products`,
          action: `/collections/vendor-${brand.toLowerCase().replace(/\s+/g, '-')}`
        });
      });
    }

    return suggestions;
  }

  /**
   * Get search query variations for better matching
   */
  getQueryVariations(query) {
    const analysis = this.analyzeQuery(query);
    const variations = new Set([query, analysis.normalized]);

    // Add all synonym variations (multilingual)
    analysis.synonyms.forEach(syn => {
      if (syn !== query && syn.length >= 2) {
        variations.add(syn);
      }
    });

    // Add without price mentions
    const withoutPrice = query.replace(/€?\s*\d+(?:\s*(?:to|-|tot)\s*€?\s*\d+)?/gi, '').trim();
    if (withoutPrice !== query && withoutPrice.length >= 2) {
      variations.add(withoutPrice);
    }

    // Add brand-focused variation
    if (analysis.brands.length > 0) {
      analysis.brands.forEach(brand => variations.add(brand));
    }

    // Add color variations
    if (analysis.colors.length > 0) {
      analysis.colors.forEach(color => variations.add(color));
    }

    // Add room-specific variations
    if (analysis.room) {
      variations.add(analysis.room);
      variations.add(`${analysis.room} flooring`);
    }

    return Array.from(variations).filter(v => v.length >= 2);
  }

  /**
   * Get related products based on multilingual context
   */
  getRelatedProductsQuery(product, currentLanguage = 'en') {
    const queries = [];

    // Product type variations
    if (product.product_type) {
      queries.push(product.product_type);
      // Add multilingual variations of product type
      const type = product.product_type.toLowerCase();
      if (this.synonyms[type]) {
        queries.push(...this.synonyms[type]);
      }
    }

    // Vendor/Brand
    if (product.vendor) {
      queries.push(product.vendor);
    }

    // Extract characteristics from tags
    if (product.tags) {
      product.tags.forEach(tag => {
        const tagLower = tag.toLowerCase();
        // Check if tag matches any characteristic
        for (const [char, keywords] of Object.entries(this.usageCharacteristics)) {
          if (keywords.some(k => tagLower.includes(k)) || tagLower.includes(char)) {
            queries.push(char);
          }
        }
      });
    }

    // Extract colors from title
    const titleWords = product.title.toLowerCase().split(/\s+/);
    titleWords.forEach(word => {
      // Check color synonyms
      for (const [color, variants] of Object.entries(this.getColorMap())) {
        if (word === color || variants.some(v => word.includes(v))) {
          queries.push(color);
        }
      }
    });

    return queries.filter((v, i, a) => a.indexOf(v) === i).slice(0, 3); // Unique, max 3
  }

  /**
   * Get color map for related products
   */
  getColorMap() {
    return {
      'oak': ['eik', 'eiche', 'chêne'],
      'walnut': ['noot', 'walnuss', 'noyer'],
      'white': ['wit', 'weiss', 'blanc', 'bianco'],
      'grey': ['grijs', 'grau', 'gris', 'grigio', 'gray'],
      'brown': ['bruin', 'braun', 'brun', 'marrone'],
      'black': ['zwart', 'schwarz', 'noir', 'nero'],
      'natural': ['naturel', 'natur', 'naturale'],
      'beige': ['beige'],
      'red': ['rood', 'rot', 'rouge', 'rosso']
    };
  }

  /**
   * Detect current language from locale or URL
   */
  detectLanguage() {
    // Try to get from HTML lang attribute
    const htmlLang = document.documentElement.lang;
    if (htmlLang) {
      return htmlLang.split('-')[0].toLowerCase();
    }

    // Try to get from URL path
    const pathLang = window.location.pathname.match(/^\/([a-z]{2})\//);
    if (pathLang) {
      return pathLang[1].toLowerCase();
    }

    // Try to get from Shopify locale
    if (window.Shopify?.locale) {
      return window.Shopify.locale.split('-')[0].toLowerCase();
    }

    return 'en'; // Default fallback
  }

  /**
   * Get localized search placeholder based on current language
   */
  getLocalizedPlaceholder() {
    const lang = this.detectLanguage();
    const placeholders = {
      'nl': 'Zoek naar producten, merken of categorieën...',
      'de': 'Suchen Sie nach Produkten, Marken oder Kategorien...',
      'fr': 'Rechercher des produits, marques ou catégories...',
      'es': 'Buscar productos, marcas o categorías...',
      'it': 'Cerca prodotti, marchi o categorie...',
      'pt': 'Pesquisar produtos, marcas ou categorias...',
      'da': 'Søg efter produkter, mærker eller kategorier...',
      'en': 'Search for products, brands, or categories...'
    };

    return placeholders[lang] || placeholders['en'];
  }
}

// Export for use in search-engine.js
window.SearchIntelligence = SearchIntelligence;
