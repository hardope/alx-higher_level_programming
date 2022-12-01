#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    i = 1
    result = 0
    arguments = len(argv) - 1

    if (arguments != 0):
        while (i <= arguments):
            result += int(argv[i])
            i += 1
    print(result)
