#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = int(str(number)[-1:])
if int(str(number)[-1:]) < 5:
    print(f"Last digit of {number}  and is {num} greater than 5")
elif int(str(number)[-1:]) == 0:
    print(f"Last digit of {number} is {num} and is 0")
elif int(str(number)[-1:]) < 6 & int(str(number)[-1:]) != 0:
    print(f"Last digit of {number} and is {num} less than 6 and not 0")
