#!/usr/bin/node
let arg = 0;
process.argv.forEach(element => { arg++; });
if (arg === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
