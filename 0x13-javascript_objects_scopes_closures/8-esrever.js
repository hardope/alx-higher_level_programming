#!/usr/bin/node

const esrever = (list) => {
  const reversedArray = [];
  list.forEach((element) => reversedArray.unshift(element));
  return (reversedArray);
};

module.exports = { esrever };
