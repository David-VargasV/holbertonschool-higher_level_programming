#!/usr/bin/python3
''' Script that takes in a URL send a POST '''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    x = {"email": sys.argv[2]}

    req = requests.post(url, data=x)
    print(req.text)
