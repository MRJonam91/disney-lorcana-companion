const fs = require('fs');

// 1. Test data/lorcana-cards.js
try {
  const content = fs.readFileSync('data/lorcana-cards.js', 'utf8');
  const window = {};
  eval(content);
  console.log('✓ data/lorcana-cards.js syntax OK! Sets loaded:', window.LORCANA_SETS_DB ? window.LORCANA_SETS_DB.length : 0);
} catch (e) {
  console.error('✗ Error in data/lorcana-cards.js:', e);
  process.exit(1);
}

// 2. Test data/lorcana-i18n.js
try {
  const i18nCode = fs.readFileSync('data/lorcana-i18n.js', 'utf8');
  new Function(i18nCode);
  console.log('✓ data/lorcana-i18n.js syntax OK! (IT, EN, FR, DE, ES + 3D Foil Controller)');
} catch (e) {
  console.error('✗ Error in data/lorcana-i18n.js:', e);
  process.exit(1);
}

// 3. Test scripts in all 8 HTML files
const htmlFiles = [
  'deck-lab.html',
  'collector-vault.html',
  'index.html',
  'guide/guida-lorcana-it.html',
  'guide/lorcana-guide-en.html',
  'guide/lorcana-guide-fr.html',
  'guide/lorcana-guide-de.html',
  'guide/lorcana-guide-es.html'
];
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
console.log('🎉 ALL 8 HTML & JS FILES PASSED SYNTAX CHECKS!');
