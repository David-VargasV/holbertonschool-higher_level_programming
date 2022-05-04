#!/usr/bin/python3
def uppercase(str):
    for l in str:
        letter = ord(l)
        if letter > 96 and letter < 123:
            letter -= 32
            print(chr(letter), end="")
            print()
