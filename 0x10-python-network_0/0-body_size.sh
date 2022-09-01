#!/bin/bash
# Script that takes in a URL, sends a request and displays the size of the body
curl -si "$1" | grep -i Content-Length | cut -d " " -f2
