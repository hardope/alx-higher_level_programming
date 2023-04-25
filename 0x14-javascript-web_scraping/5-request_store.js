#!/usr/bin/node
// lorem ipsum

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
