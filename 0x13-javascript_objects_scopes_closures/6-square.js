#!/usr/bin/node
const OtherSquare = require('./5-square');

class Square extends OtherSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let index = 0; index < this.height; index++) {
      let Axis = '';
      let y = 0;
      while (y < this.width) {
        Axis += myChar;
        y++;
      }
      console.log(Axis);
    }
  }
}

module.exports = Square;
