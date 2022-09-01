#!/bin/bash
# Script that takes in a URL, sends GET request, and displays the body
curl -s "$1"-X GET -H "X-HolbertonSchool-User-Id: 98"
