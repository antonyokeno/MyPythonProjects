print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill =0
if size=="S" and pepperoni=="Y" and extra_cheese=="Y":
    bill =18
elif size=="S" and pepperoni=="Y" and extra_cheese=="N":
    bill=17
elif size == "S" and pepperoni == "N" and extra_cheese == "Y":
    bill = 16
elif size == "S" and pepperoni == "N" and extra_cheese == "N":
    bill = 15
elif size == "M" and pepperoni == "Y" and extra_cheese == "Y":
    bill = 24
elif size == "M" and pepperoni == "Y" and extra_cheese == "N":
    bill = 23
elif size == "M" and pepperoni == "N" and extra_cheese == "Y":
    bill = 21
elif size == "M" and pepperoni == "N" and extra_cheese == "N":
    bill = 20
elif size == "L" and pepperoni == "Y" and extra_cheese == "Y":
    bill = 29
elif size == "L" and pepperoni == "Y" and extra_cheese == "N":
    bill = 28
elif size == "L" and pepperoni == "N" and extra_cheese == "Y":
    bill = 26
elif size == "L" and pepperoni == "N" and extra_cheese == "N":
    bill = 25
else:
    bill=0

print(f"Your final bill is: ${bill}.")