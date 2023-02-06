#!/usr/bin/node

const fs = require('fs').promises;
const { argv } = require('process');

fs.readFile(argv[2], 'utf8')
  .then(data => fs.writeFile(argv[4], data, 'utf8'))
  .catch(err => console.error(err));

fs.readFile(argv[3], 'utf8')
  .then(data => fs.writeFile(argv[4], data, { flag: 'a' }, 'utf8'))
  .catch(err => console.error(err));
