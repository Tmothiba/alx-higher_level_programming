#!/usr/bin/node

exports.esrever = function (list) {
  // Initialize an empty array to store the reversed list
  const reversed = [];

  for (let i = list.length - 1; i >= 0; i--) {
    // Add each element to the reversed array
    reversed.push(list[i]);
  }
  return reversed;
};
