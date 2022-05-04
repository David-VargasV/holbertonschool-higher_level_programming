#!/usr/bin/python3
def fizzbuzz():
    for mul % 15 == 0:
        print("{}".format("FizzBuzz "), end="")
    elif mul % 5 == 0:
        print("{}".format("Buzz "), end="")
    elif mul % 3 == 0:
        print("{}".format("Fizz "), end="")
    else:
        print("{:d}".format(mul), end="")
