#!/usr/bin/python3
for n in range(122, 96, -1):
    num = n
    if num % 2 != 0:
        num -= 32
    print("{}".format(chr(num)), end="")
