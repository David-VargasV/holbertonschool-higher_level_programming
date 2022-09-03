#!/usr/bin/python3
# Script that takes in a URL and displays the value of the X-Request-Id

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
