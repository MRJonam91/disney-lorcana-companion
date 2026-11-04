(function (root) {
  'use strict';
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/’/g, "'").replace(/\s+[–—-]\s+/g, ' - ').trim().toLowerCase();
  function fullCardName(card) {
    return card.full_name || card.name + (card.sub ? ' - ' + card.sub : '');
  }
  function parseDeckList(text, cards) {
    const result = {};
    const lines = text.split(/\r?\n/).map(line => line.trim()).filter(Boolean);
    if (!lines.length) throw new Error('Lista vuota / Empty list');
    for (const line of lines) {
      const match = line.match(/^([1-4])x?\s+(.+)$/i);
      if (!match) throw new Error('Riga non valida / Invalid line: ' + line);
      const candidates = cards.filter(card => normalize(fullCardName(card)) === normalize(match[2]));
      const card = candidates.find(c => (c.setNum || c.set_num || 0) >= 9 && !['Enchanted','Iconic','Epic'].includes(c.rarity))
        || candidates.find(c => !['Enchanted','Iconic','Epic'].includes(c.rarity));
      if (!card) throw new Error('Carta non trovata / Unknown card: ' + match[2]);
      const quantity = (result[card.id] || 0) + Number(match[1]);
      if (quantity > 4) throw new Error('Massimo 4 copie / Maximum 4 copies: ' + match[2]);
      result[card.id] = quantity;
    }
    return result;
  }
  function shuffle(cards, random = Math.random) {
    for (let i = cards.length - 1; i > 0; i--) {
      const j = Math.floor(random() * (i + 1));
      [cards[i], cards[j]] = [cards[j], cards[i]];
    }
    return cards;
  }
  const api = {fullCardName, parseDeckList, shuffle};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.LorcanaDeckLists = api;
})(typeof window !== 'undefined' ? window : globalThis);
