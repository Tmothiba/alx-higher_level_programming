#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter for occurrences
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
