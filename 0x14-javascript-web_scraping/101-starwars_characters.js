#!/usr/bin/node
// web scraper

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    // console.log(characters);
    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
