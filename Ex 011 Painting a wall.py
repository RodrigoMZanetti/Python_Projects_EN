width=float(input("\033[33mWhat is the width of the wall? (m):\033[0m "))
height=float(input("\033[34mWhat is the height of the wall? (m):\033[0m "))

wallarea = width * height
liters = wallarea / 2

print(f"\033[35mThe amount of paint needed to paint a wall with an area of {wallarea:.1f} m² is: {liters:.1f} liters.\033[0m")
