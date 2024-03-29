#!/usr/bin/python3
''' script that takes in a letter and sends a POST request '''

from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_dict = response.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except:
        print("Not a valid JSON")
