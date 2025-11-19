import math
from time import sleep

print("="*40)
print("\U0001F60E \033[31mSine, cosine, and tangent\033[m \U0001F60E")
print("="*40)

angle_rad = float(input("Enter the angle you want: "))

angle = math.radians(angle_rad)

cos = math.cos(angle)
sin = math.sin(angle)
tan = math.tan(angle)

print("Wait...")
sleep (1)

print(f"\033[32mThe cosine of {angle_rad:.1f}º is {cos:.1f}\033[m")
print(f"\033[33mThe sine of {angle_rad:.1f}º is {sin:.1f}\033[m")
print(f"\033[34mThe tangent of {angle_rad:.1f}º is {tan:.1f}\033[m")

