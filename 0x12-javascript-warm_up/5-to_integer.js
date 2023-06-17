#!/usr/bin/node
const num = parseInt(process.argv[2]) ? `My number: ${parseInt(process.argv[2])}` : 'Not a number';
console.log(num);
