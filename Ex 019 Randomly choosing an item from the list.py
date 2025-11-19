import random

print("="*40)
print("\U0001F525 \033[31mRandomly choosing an item from the list\033[m \U0001F525")
print("="*40)

first = str(input("First student's name: "))
second = str(input("Second student's name: "))
third = str(input("Third student's name: "))
fourth = str(input("Fourth student's name: "))

namelist = [first, second, third, fourth]

name = random.choice(namelist)
print(f"The randomly chosen student was \033[35m{name}\033[m \U0001F4AA")