#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    nlen = len(argv)
    if nlen == 1:
        print(f"{nlen - 1} arguments.")
    elif nlen == 2:
        print(f"{nlen - 1} argument:")
    else:
        print(f"{nlen - 1} arguments:")
    for arguments in range(1, nlen):
        print(f"{arguments}: {argv[arguments]}")
