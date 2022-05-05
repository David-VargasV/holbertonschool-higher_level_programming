#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    larg = len(argv)
    value = 0

    for num in range(1, larg):
        value += int(argv[num])
    print(value)
