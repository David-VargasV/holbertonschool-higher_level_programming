#!/usr/bin/node
exports.esrever = function (list) {
  const rList = [];
  for (let n = list.length - 1; n >= 0; n--) {
    rList.push(list[n]);
  }
  return rList;
};
