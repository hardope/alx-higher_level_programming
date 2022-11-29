#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and str(number)[-1] != "0":
    sign = "-"
else:
    sign = ""
number = f"{number}"
print(f"Last digit of {number} is {sign}{number[-1]}")