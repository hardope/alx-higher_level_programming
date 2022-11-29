#!/usr/bin/python3
for number in range(100):
    if (number != 99):
        print("{}{}, ".format(int(number / 10), number % 10), end="")
    else:
        print("{}{}".format(int(number / 10), number % 10))
