# Tip calculator for whenever you need it 😁


print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15 percent?"))
people = int(input("How many people to split the bill?"))
tip_convert = tip / 100
tip_total = total * tip_convert

each_person = round((total + tip_total) / people, 2)

print(f"Each person will pay ${each_person}. Fork it over pal.")

