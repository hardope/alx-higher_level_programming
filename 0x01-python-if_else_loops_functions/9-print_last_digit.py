#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10 if number >= 0 else -number % 10
    print(f"{last_digit}", end="")
    return last_digit
