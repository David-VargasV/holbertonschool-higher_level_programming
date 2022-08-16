#!/usr/bin/node
const list = process.argv.slice(2).map(n => parseInt(n));
const sortList = list.sort((a,b) => a < b);
if (sortList.length <= 1) {
    console.log(0);
} else {
    console.log(sortList[1]);
}
