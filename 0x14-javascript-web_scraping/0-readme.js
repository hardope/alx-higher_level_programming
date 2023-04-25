#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf-8',
  (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });