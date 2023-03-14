#!/usr/bin/node

const nbOccurences = (list, searchElement) => list.filter((element) => searchElement === element).length;

module.exports = { nbOccurences };
