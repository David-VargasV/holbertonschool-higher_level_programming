#!/usr/bin/python
from itertools import count
from unittest import result


if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    result = 0

    for num in range(count - 1):
        result += int(sys.argv[num + 1])
        print("{}".format(result))
