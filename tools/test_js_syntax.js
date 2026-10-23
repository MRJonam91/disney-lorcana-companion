const fs = require('fs');

// 1. Test data/lorcana-cards.js
try {
  const content = fs.readFileSync('data/lorcana-cards.js', 'utf8');
  // simulate window object
  const window = {};
  eval(content);
  console.log('✓ data/lorcana-cards.js syntax OK! Sets loaded:', window.LORCANA_SETS_DB ? window.LORCANA_SETS_DB.length : 0);
  
  // Check cards in sets
  let totalCards = 0;
  let epicCount = 0;
  let iconicCount = 0;
  window.LORCANA_SETS_DB.forEach(s => {
    totalCards += (s.cards || []).length;
    (s.cards || []).forEach(c => {
      if (c.rarity === 'Epic') epicCount++;
      if (c.rarity === 'Iconic') iconicCount++;
    });
  });
  console.log(`✓ Total cards in DB: ${totalCards}, Epic: ${epicCount}, Iconic: ${iconicCount}`);
} catch (e) {
  console.error('✗ Error in data/lorcana-cards.js:', e);
  process.exit(1);
}

// 2. Test scripts in HTML files
const htmlFiles = ['deck-lab.html', 'collector-vault.html', 'index.html'];
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, 'utf8');
  const scriptRegex = /<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/gi;
  let match;
  let idx = 0;
  while ((match = scriptRegex.exec(html)) !== null) {
    idx++;
    const code = match[1];
    try {
      new Function(code);
      console.log(`✓ ${file} inline script #${idx} syntax OK`);
    } catch (e) {
      console.error(`✗ Syntax error in ${file} script #${idx}:`, e.message);
      process.exit(1);
    }
  }
}
console.log('🎉 ALL HTML & JS SYNTAX CHECKS PASSED!');
