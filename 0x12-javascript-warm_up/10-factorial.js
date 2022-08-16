#!/usr/bin/node
const arg = process.argv[2];
const n = parseInt(arg);
const x = (function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else if (n < 0) {
    return 'does not exist';
  } else {
    return (n * factorial(n - 1));
  }
})(n);
console.log(x);
