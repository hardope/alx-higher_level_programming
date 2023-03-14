#!/usr/bin/node

const { argv } = require('process');
const args = argv.slice(2);
let result = 0;
let finalArray = [];

if (args.length > 1) {
  finalArray = [...new Set(args.map((e) => parseInt(e)).sort((a, b) => b - a))];
  result = finalArray.length > 1 ? finalArray[1] : finalArray[0];
}

console.log(result);
