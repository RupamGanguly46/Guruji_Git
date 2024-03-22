#Assignment 6: Ticket Price
#Problem: Create a program that reads a person's age and
#determines the ticket price for a theme park based on
#the following rules:
#Age 0-3 (free), Age 4-12 ($10), Age 13-17 ($15),
#Age 18 and above ($20).

age=int(input("Enter your age"))
if 0<=age<=3:
    print("Ticket is free")
else:
    if age<=12:
        price=10
    elif age<=17:
        price=15
    else:
        price=20
    print(f"Your ticket price is ${price}")
    
