#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == "__main__"):
    argc = len(argv)
    result = 0
    operators = ["+", "-", "*", "/"]

    if (argc != 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    if (argv[2] not in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    num1 = int(argv[1])
    operator = argv[2]
    num2 = int(argv[3])

    if (operator == "+"):
        result = add(num1, num2)
    elif (operator == "-"):
        result = sub(num1, num2)
    elif (operator == "*"):
        result = mul(num1, num2)
    else:
        result = div(num1, num2)
    print(f"{num1} {operator} {num2} = {result}")
