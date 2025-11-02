/**
 * Query Normalizer & Deduplication Detector
 * Prevents collection spam by normalizing search queries and detecting duplicates
 * 
 * Features:
 * - Normalizes similar queries to same collection
 * - Detects semantic duplicates
 * - Multi-language support
 * - Spam detection
 * - Query quality scoring
 */

class QueryNormalizer {
  constructor() {
    // Common words to remove (stop words) - multilingual
    this.stopWords = {
      en: ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'best', 'top', 'cheap', 'affordable'],
      nl: ['de', 'het', 'een', 'en', 'of', 'maar', 'in', 'op', 'aan', 'voor', 'van', 'met', 'door', 'beste', 'goedkope'],
      de: ['der', 'die', 'das', 'ein', 'eine', 'und', 'oder', 'aber', 'in', 'auf', 'an', 'zu', 'für', 'von', 'mit', 'beste', 'günstig'],
      fr: ['le', 'la', 'les', 'un', 'une', 'et', 'ou', 'mais', 'dans', 'sur', 'à', 'pour', 'de', 'avec', 'par', 'meilleur', 'pas cher'],
      es: ['el', 'la', 'los', 'las', 'un', 'una', 'y', 'o', 'pero', 'en', 'sobre', 'a', 'para', 'de', 'con', 'mejor', 'barato'],
      it: ['il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una', 'e', 'o', 'ma', 'in', 'su', 'a', 'per', 'di', 'con', 'migliore', 'economico'],
      pt: ['o', 'a', 'os', 'as', 'um', 'uma', 'e', 'ou', 'mas', 'em', 'sobre', 'para', 'de', 'com', 'melhor', 'barato'],
      da: ['den', 'det', 'de', 'en', 'et', 'og', 'eller', 'men', 'i', 'på', 'til', 'for', 'af', 'med', 'bedste', 'billig']
    };

    // Common synonyms for deduplication
    this.synonymGroups = [
      ['waterproof', 'waterresistant', 'water-resistant', 'water-proof'],
      ['flooring', 'floor', 'floors', 'vloer', 'vloeren', 'boden', 'böden', 'sol', 'pavimento', 'gulv'],
      ['vinyl', 'pvc', 'lvt', 'luxury-vinyl'],
      ['laminate', 'laminaat', 'laminat'],
      ['wood', 'wooden', 'timber', 'hout', 'houten', 'holz', 'bois', 'madera', 'legno', 'madeira'],
      ['kitchen', 'keuken', 'küche', 'cuisine', 'cocina', 'cucina', 'cozinha', 'køkken'],
      ['bathroom', 'badkamer', 'badezimmer', 'salle-de-bain', 'baño', 'bagno', 'casa-de-banho', 'badeværelse']
    ];

    // Spam patterns
    this.spamPatterns = [
      /^test$/i,
      /^asdf/i,
      /^qwerty/i,
      /^\d+$/,           // Only numbers
      /^[a-z]{1,2}$/i,   // Single/double letters
      /(.)\1{4,}/,       // Repeated characters (aaaaa)
      /^[^a-z0-9\s]{3,}/i // Only special characters
    ];
  }

  /**
   * Main normalization function
   * @param {string} query - Raw search query
   * @param {string} locale - Language code (e.g., 'nl', 'en', 'de')
   * @returns {Object} Normalized query data
   */
  normalize(query, locale = 'en') {
    const lang = locale.split('-')[0]; // 'nl-NL' -> 'nl'

    // Step 1: Basic cleanup
    let normalized = query
      .toLowerCase()
      .trim()
      .replace(/[^\w\s-]/g, ' ')  // Remove special chars except hyphen
      .replace(/\s+/g, ' ');       // Collapse multiple spaces

    // Step 2: Remove stop words
    const stopWords = this.stopWords[lang] || this.stopWords.en;
    const words = normalized.split(' ');
    const filteredWords = words.filter(word => !stopWords.includes(word));
    normalized = filteredWords.join(' ');

    // Step 3: Replace synonyms with canonical form
    normalized = this.canonicalizeSynonyms(normalized);

    // Step 4: Sort words alphabetically (order doesn't matter)
    const sortedWords = normalized.split(' ').sort().join(' ');

    // Step 5: Generate collection handle (URL-safe)
    const handle = this.generateHandle(sortedWords);

    // Step 6: Calculate quality score
    const qualityScore = this.calculateQualityScore(query, normalized);

    // Step 7: Check for spam
    const isSpam = this.isSpam(query);

    return {
      original: query,
      normalized: sortedWords,
      handle: handle,
      qualityScore: qualityScore,
      isSpam: isSpam,
      shouldCreateCollection: qualityScore >= 0.5 && !isSpam,
      reason: this.getRecommendationReason(qualityScore, isSpam)
    };
  }

  /**
   * Replace synonyms with canonical form
   */
  canonicalizeSynonyms(text) {
    let canonicalized = text;

    this.synonymGroups.forEach(group => {
      const canonical = group[0]; // First word is canonical
      const pattern = new RegExp(`\\b(${group.join('|')})\\b`, 'gi');
      canonicalized = canonicalized.replace(pattern, canonical);
    });

    return canonicalized;
  }

  /**
   * Generate URL-safe collection handle
   */
  generateHandle(normalizedQuery) {
    return normalizedQuery
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^a-z0-9-]/g, '')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '')
      .substring(0, 50); // Shopify handle limit
  }

  /**
   * Calculate query quality score (0-1)
   * Higher = better quality, more likely to create collection
   */
  calculateQualityScore(original, normalized) {
    let score = 0.5; // Start at neutral

    // Factor 1: Word count (sweet spot: 2-4 words)
    const wordCount = normalized.split(' ').length;
    if (wordCount >= 2 && wordCount <= 4) {
      score += 0.2;
    } else if (wordCount === 1 || wordCount > 6) {
      score -= 0.2;
    }

    // Factor 2: Length (sweet spot: 10-30 chars)
    const length = original.length;
    if (length >= 10 && length <= 30) {
      score += 0.1;
    } else if (length < 5 || length > 50) {
      score -= 0.2;
    }

    // Factor 3: Contains meaningful product terms
    const productTerms = ['waterproof', 'vinyl', 'laminate', 'wood', 'kitchen', 'bathroom', 'floor', 'tile'];
    const containsProductTerm = productTerms.some(term => normalized.includes(term));
    if (containsProductTerm) {
      score += 0.2;
    }

    // Factor 4: Not too generic
    const genericTerms = ['product', 'item', 'thing', 'stuff'];
    const isGeneric = genericTerms.some(term => normalized.includes(term));
    if (isGeneric) {
      score -= 0.3;
    }

    // Factor 5: Has specificity (brand, color, feature)
    if (this.hasSpecificity(normalized)) {
      score += 0.1;
    }

    return Math.max(0, Math.min(1, score)); // Clamp 0-1
  }

  /**
   * Check if query has specific attributes
   */
  hasSpecificity(query) {
    const specificAttributes = [
      // Colors
      'black', 'white', 'grey', 'gray', 'brown', 'beige', 'oak', 'walnut',
      // Features
      'waterproof', 'scratch-resistant', 'pet-friendly', 'eco-friendly',
      // Sizes
      'large', 'small', 'wide', 'narrow',
      // Rooms
      'kitchen', 'bathroom', 'living', 'bedroom'
    ];

    return specificAttributes.some(attr => query.includes(attr));
  }

  /**
   * Check if query is spam
   */
  isSpam(query) {
    return this.spamPatterns.some(pattern => pattern.test(query));
  }

  /**
   * Get human-readable reason for recommendation
   */
  getRecommendationReason(score, isSpam) {
    if (isSpam) {
      return 'Query appears to be spam';
    }

    if (score >= 0.7) {
      return 'High-quality search query, excellent collection candidate';
    } else if (score >= 0.5) {
      return 'Good search query, suitable for collection';
    } else if (score >= 0.3) {
      return 'Low-quality query, consider improving search terms';
    } else {
      return 'Poor query quality, not suitable for collection';
    }
  }

  /**
   * Check if two queries would create duplicate collections
   * @param {string} query1 
   * @param {string} query2 
   * @param {string} locale 
   * @returns {boolean} True if duplicates
   */
  areDuplicates(query1, query2, locale = 'en') {
    const norm1 = this.normalize(query1, locale);
    const norm2 = this.normalize(query2, locale);

    // Exact match after normalization
    if (norm1.normalized === norm2.normalized) {
      return true;
    }

    // Handles match
    if (norm1.handle === norm2.handle) {
      return true;
    }

    // Similarity check (Levenshtein distance)
    const similarity = this.calculateSimilarity(norm1.normalized, norm2.normalized);
    
    // If 80%+ similar, consider duplicates
    return similarity >= 0.8;
  }

  /**
   * Calculate similarity between two strings (0-1)
   * Uses Levenshtein distance
   */
  calculateSimilarity(str1, str2) {
    const longer = str1.length > str2.length ? str1 : str2;
    const shorter = str1.length > str2.length ? str2 : str1;

    if (longer.length === 0) {
      return 1.0;
    }

    const editDistance = this.levenshteinDistance(longer, shorter);
    return (longer.length - editDistance) / longer.length;
  }

  /**
   * Levenshtein distance (edit distance between strings)
   */
  levenshteinDistance(str1, str2) {
    const matrix = [];

    for (let i = 0; i <= str2.length; i++) {
      matrix[i] = [i];
    }

    for (let j = 0; j <= str1.length; j++) {
      matrix[0][j] = j;
    }

    for (let i = 1; i <= str2.length; i++) {
      for (let j = 1; j <= str1.length; j++) {
        if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
          matrix[i][j] = matrix[i - 1][j - 1];
        } else {
          matrix[i][j] = Math.min(
            matrix[i - 1][j - 1] + 1, // Substitution
            matrix[i][j - 1] + 1,     // Insertion
            matrix[i - 1][j] + 1      // Deletion
          );
        }
      }
    }

    return matrix[str2.length][str1.length];
  }

  /**
   * Find existing collection that matches this query
   * @param {string} query 
   * @param {Array} existingCollections - Array of collection objects with handle/title
   * @param {string} locale 
   * @returns {Object|null} Matching collection or null
   */
  findMatchingCollection(query, existingCollections, locale = 'en') {
    const normalized = this.normalize(query, locale);

    // Check for exact handle match
    const exactMatch = existingCollections.find(c => 
      c.handle === normalized.handle
    );

    if (exactMatch) {
      return {
        collection: exactMatch,
        matchType: 'exact',
        confidence: 1.0
      };
    }

    // Check for similar handles
    for (const collection of existingCollections) {
      const similarity = this.calculateSimilarity(
        normalized.normalized,
        collection.handle.replace(/-/g, ' ')
      );

      if (similarity >= 0.8) {
        return {
          collection: collection,
          matchType: 'similar',
          confidence: similarity
        };
      }

      // Also check title
      const titleNorm = this.normalize(collection.title, locale);
      if (titleNorm.normalized === normalized.normalized) {
        return {
          collection: collection,
          matchType: 'title',
          confidence: 1.0
        };
      }
    }

    return null;
  }

  /**
   * Batch normalize multiple queries and detect duplicates
   * @param {Array} queries - Array of query strings
   * @param {string} locale 
   * @returns {Object} Grouped and deduplicated queries
   */
  batchNormalize(queries, locale = 'en') {
    const normalized = queries.map(q => ({
      original: q,
      ...this.normalize(q, locale)
    }));

    // Group by handle (duplicates)
    const groups = {};
    
    normalized.forEach(item => {
      if (!groups[item.handle]) {
        groups[item.handle] = [];
      }
      groups[item.handle].push(item.original);
    });

    // Find canonical query for each group (shortest one usually)
    const canonical = Object.entries(groups).map(([handle, originals]) => ({
      handle: handle,
      canonical: originals.sort((a, b) => a.length - b.length)[0],
      variants: originals,
      count: originals.length
    }));

    return {
      total: queries.length,
      unique: canonical.length,
      duplicates: queries.length - canonical.length,
      groups: canonical
    };
  }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = QueryNormalizer;
}

// Browser global
if (typeof window !== 'undefined') {
  window.QueryNormalizer = QueryNormalizer;
}
