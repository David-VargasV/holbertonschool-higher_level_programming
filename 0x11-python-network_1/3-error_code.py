#!/usr/bin/python3
''' Script that takes in a URL and displays the body of the response '''

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
