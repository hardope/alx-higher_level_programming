#!/usr/bin/node

const { argv } = require('process');

function factorial (num) {
  if (num <= 1) return (1);

  return (factorial(num - 1) * num);
}

const parsed = parseInt(argv[2]);
console.log(Number.isNaN(parsed) ? 1 : factorial(parsed));
