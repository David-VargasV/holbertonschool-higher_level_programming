#!/usr/bin/python3
''' Script that takes in a URL, sends and displays the body of the response '''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
