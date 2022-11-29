#!/usr/bin/python3
for number in range(100):
    if int(number / 10) != number % 10 and int(number / 10) < number % 10:
        print("{}{}".format(int(number / 10), number % 10), end="")
        if (number != 89):
            print(", ", end="")
print("")
