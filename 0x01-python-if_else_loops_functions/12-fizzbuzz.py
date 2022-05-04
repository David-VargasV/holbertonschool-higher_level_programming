#!/usr/bin/python3
def fizzbuzz():
    for mul in range(1, 101):
        if mul % 3 == 0 and mul % 5 == 0:
        print("FizzBuzz"), end=" ")
        elif mul % 5 == 0:
        print("Buzz"), end=" ")
        elif mul % 3 == 0:
        print("Fizz"), end=" ")
        else:
        print(mul, end=" ")
