#!/usr/bin/node

let cuantity = 0;

const logMe = (item) => {
  console.log(`${cuantity}: ${item}`);
  cuantity++;
};

module.exports = { logMe };
