#!/usr/bin/node
/**
 * Represents a rectangle class with width and height attributes
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let Axis = '';
      let y = 0;
      while (y < this.width) {
        Axis += 'X';
        y++;
      }
      console.log(Axis);
    }
  }
}
module.exports = Rectangle;
