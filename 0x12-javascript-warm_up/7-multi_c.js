#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x);
if (isNaN(x)) {
    console.log('Missing number of occurrences');
} else {
    for (let n = 0; n < x; n++) {
        console.log('C is fun');
    }
}
