const {test} = require('node:test');
const assert = require('node:assert/strict');
const {parseDeckList, fullCardName, shuffle} = require('../data/deck-list-tools.js');
const cards = [
  {id:'old', name:'Judy Hopps', sub:'Lead Detective',setNum:3},
  {id:'lead', name:'Judy Hopps', sub:'Lead Detective',setNum:10,rarity:'Rare'},
  {id:'clues', name:'Judy Hopps', sub:'Uncovering Clues',setNum:10},
  {id:'song', name:'Strength of a Raging Fire', sub:'',setNum:9},
];
test('imports full subtitle and chooses a Core printing',()=>{
  assert.deepEqual(parseDeckList('4 Judy Hopps - Lead Detective\n3 Judy Hopps - Uncovering Clues',cards),{lead:4,clues:3});
});
test('exports action names without a dangling separator',()=>{
  assert.equal(fullCardName(cards[3]),'Strength of a Raging Fire');
});
test('rejects unknown cards instead of quietly discarding lines',()=>{
  assert.throws(()=>parseDeckList('4 Missing Card',cards),/Missing Card/);
});
test('rejects five combined copies of one full card name',()=>{
  assert.throws(()=>parseDeckList('3 Judy Hopps - Lead Detective\n2 Judy Hopps - Lead Detective',cards),/4/);
});
test('rejects malformed and empty lists',()=>{
  for(const text of ['', 'Judy Hopps - Lead Detective','0 Judy Hopps - Lead Detective'])assert.throws(()=>parseDeckList(text,cards));
});
test('shuffle preserves every card exactly once',()=>{
  const input=[1,2,3,4,5]; shuffle(input,()=>0);
  assert.deepEqual([...input].sort(),[1,2,3,4,5]);
  assert.notDeepEqual(input,[1,2,3,4,5]);
});
