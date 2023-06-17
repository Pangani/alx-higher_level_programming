#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const num1 = process.argv[2];
const num2 = process.argv[3];

console.log(add(parseInt(num1), parseInt(num2)));
