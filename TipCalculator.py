print("Welcome to the tip calculator")
total = input("What was the total bill? ")
# I change percentage tip, because in course next to "like to give?" was "10, 12, or 15?" and for that we should use loop
percentage_tip = input("What percentage tip would you like to give? ")
people = input("How many people to spilt the bill? ")

for_one_person = round(((float(total) * (float(percentage_tip)/100+1)) / int(people)),2)

print(f"Each person should pay: {for_one_person}")