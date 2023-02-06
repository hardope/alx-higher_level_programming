#!/usr/bin/node

const addMeMaybe = (number, theFunction) => {
  theFunction(number + 1);
};

module.exports = { addMeMaybe };
