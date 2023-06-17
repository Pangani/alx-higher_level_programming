#!/usr/bin/node

const size = process.argv[2];

if (parseInt(size)) {
  for (let i = 0; i < size; i++) {
    let y = 0;
    let mySpace = '';

    while (y < size) {
      mySpace = mySpace + 'X';
      y++;
    }
    console.log(mySpace);
  }
} else {
  console.log('Missing size');
}
