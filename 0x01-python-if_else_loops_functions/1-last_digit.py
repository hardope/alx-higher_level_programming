#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and str(number)[-1] != "0":
    sign = "-"
else:
    sign = ""
number = f"{number}"
print(f"Last digit of {number} is {sign}{number[-1]}", end=" ")
if int(sign+number[-1]) > 5:
    print("and is greater than 5")
elif int(sign+number[-1]) < 6 and int(number[-1]) != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")
