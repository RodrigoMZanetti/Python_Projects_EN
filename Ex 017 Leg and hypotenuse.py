import math

num1 = float(input("\033[34mEnter the first number:\033[m "))
num2 = float(input("\033[34mEnter the second number:\033[m "))

hyp = math.hypot(num1, num2)
print(f"The hypotenuse is {hyp:.2f}.")
