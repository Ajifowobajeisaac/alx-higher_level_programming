#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = int(repr(number)[-1])

if number > 0:
    if last_number > 5:
        print(f"Last digit of {number} is {last_number} and is greater than 5")
    elif last_number == 0:
         print(f"Last digit of {number} is {last_number} and is 0")
    elif last_number < 6 and last_number != 0:
        print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
elif number < 0:
    last_number = -abs(last_number)
    if last_number == 0:
         print(f"Last digit of {number} is {last_number} and is 0")
    elif last_number < 6 and last_number != 0:
        print(f"Last digit of {number} is {last_number} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_number} and is 0")
