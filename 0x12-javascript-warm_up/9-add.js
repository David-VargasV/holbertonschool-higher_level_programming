#!/usr/bin/node
const args = process.argv;
const arg1 = parseInt(args[2]);
const arg2 = parseInt(args[3]);
function add (arg1, arg2) {
    return arg1 + arg2;
}
console.log(add(arg1, arg2));
