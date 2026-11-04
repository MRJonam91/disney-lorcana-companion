const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync, readdirSync } = require('node:fs');
const { join } = require('node:path');
const vm = require('node:vm');

// Run the actual embedded calculator in every downloadable guide.
for (const file of readdirSync(join(__dirname, '../guide')).filter(f => f.endsWith('.html'))) {
  const html = readFileSync(join(__dirname, '../guide', file), 'utf8');
  const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
  const context = vm.createContext({});
  vm.runInContext(script.slice(script.indexOf('function hypergeom'), script.indexOf('function updateCalc')), context);
  const odds = (...args) => vm.runInContext(`calculateOdds(${args.join(',')})`, context);
  const near = (actual, expected) => assert.ok(Math.abs(actual - expected) < 1e-12, `${actual} != ${expected}`);

  test(`${file}: no mulligan equals ordinary nine-card draw by turn three`, () => {
    const result = odds(60, 4, 0);
    near(result.opening, 1 - (53 * 52 * 51 * 50) / (60 * 59 * 58 * 57));
    near(result.turn3, vm.runInContext('hypergeom(60, 4, 9)', context));
  });
  test(`${file}: full mulligan excludes the initial seven, then reshuffles`, () => {
    // With one target, opening miss is 53/60, replacements miss 46/53,
    // then two draws miss 51/53 after the returned cards are shuffled in.
    const result = odds(60, 1, 7);
    near(result.mulligan, 14 / 60);
    near(result.turn3, 1 - (53 / 60) * (46 / 53) * (51 / 53));
  });
  test(`${file}: invalid deck sizes fail rather than display plausible odds`, () => {
    for (const deck of [0, 39, 101, 60.5, NaN, Infinity]) {
      assert.throws(() => odds(deck, 4, 4), /Invalid/);
    }
  });
  test(`${file}: rejects impossible target counts and replacement counts`, () => {
    for (const args of [[60, 61, 4], [60, -1, 4], [60, 4, 8], [60, 4, -1]]) {
      assert.throws(() => odds(...args), /Invalid/);
    }
  });
  test(`${file}: zero targets and guaranteed hits stay within bounds`, () => {
    near(odds(60, 0, 7).turn3, 0);
    near(odds(60, 60, 7).opening, 1);
    near(vm.runInContext('hypergeom(60, 4, 0)', context), 0);
    near(vm.runInContext('hypergeom(60, 4, 60)', context), 1);
  });
}
