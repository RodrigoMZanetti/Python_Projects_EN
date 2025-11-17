days = int(input("For how many days was the car rented?: "))
daysprice = days * 60

km = float(input("How many kilometers did the car travel?: "))
kmprice = km * 0.15

total = daysprice + kmprice

print(f"The total amount to be paid will be: {total} dollars. ")