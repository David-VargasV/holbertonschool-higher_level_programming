#!/usr/bin/node
const request = require('request');
const ApiUrl = process.argv[2];
request(ApiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let n = 0;
  for (const result of JSON.parse(body).results) {
    for (const Wedge of result.characters) {
      if (Wedge.includes(18)) {
        n++;
      }
    }
  }
  console.log(n);
});
