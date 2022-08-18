#!/usr/bin/node
const request = require('request');
const ApiUrl = process.argv[2];
request(ApiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = {};
  for (const task of JSON.parse(body)) {
    if (task.data === true) {
      if (data[task.userId]) {
        data[task.userId]++;
      } else {
        data[task.userId] = 1;
      }
    }
  }
  console.log(data);
});
