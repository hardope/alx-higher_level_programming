#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);

console.log(Number.isInteger(num) ? `My number: ${num}` : 'Not a number');
