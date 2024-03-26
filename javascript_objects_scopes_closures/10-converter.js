#!/usr/bin/node

let convertToBinary = exports.converter(2);
console.log(convertToBinary(10));

let convertToHex = exports.converter(16);
console.log(convertToHex(255));
