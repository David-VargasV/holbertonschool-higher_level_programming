#!/usr/bin/node
const request = require('request');
const ApiUrl = process.argv[2];
request(ApiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const completed = {};
  for (const task of JSON.parse(body)) {
    if (task.complete === true) {
      if (completed[task.userId]) {
        completed[task.userId]++;
      } else {
        completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
