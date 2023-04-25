#!/usr/bin/node
// write string to file

const fs = require('fs');
const argv = process.argv;
let filePath = argv[2];
let string = argv[3];

fs.writeFile(filePath, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
