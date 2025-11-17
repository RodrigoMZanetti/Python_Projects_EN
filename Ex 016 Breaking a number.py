print("To transform a float into a whole number by removing the decimal part.")

import math
from math import floor

num=float(input("\033[34mEnter a number:\033[m "))
num = math.floor(num)

print(f"\033[33mThe number is {num}.\033[m")