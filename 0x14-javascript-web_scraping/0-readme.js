#!/usr/bin/node
// Read from file

const filesys = require('fs');
const filename = process.argv[2];
filesys.readFile(filename, 'utf-8',
  (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });