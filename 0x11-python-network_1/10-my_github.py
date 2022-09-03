#!/usr/bin/python3
''' script that takes your GitHub credentials and display your id '''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = requests.get("https://api.github.com/user",
                           auth=(url, sys.argv[2]))
        print(req.json()["id"])
    except:
        print("None")
