#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  for (let n = 0; n < list.length; n++) {
    if (list[n] === searchElement) {
      x += 1;
    }
  }
  return x;
};
