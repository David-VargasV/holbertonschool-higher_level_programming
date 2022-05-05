#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

count, add = 1, 0

while count < len(argv):
    add = (add + int(argv[count]))
    count = count + 1
print(add)
