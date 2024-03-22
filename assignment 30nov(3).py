# Medicine store management system

print('''1. Add Medicine
2. Display Medicine Inventory
3. Update Medicine Quantity
4. Search Medicine by ID
5. Exit''')

inventory=dict()

while True:
    print("\n\n\n")
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        med_id=input("Enter Medicine ID: ")
        med_name=input("Enter Medicine Name: ")
        qty=input("Enter Quantity: ")
        price=input("Enter Price: ")
        inventory.update({med_id:[med_name,qty,price]})
        print("\n\n\n")

    elif ch==2:
        print("Medicine Inventory:")
        for i in range(len(inventory)):
            print(f"Medicine ID: {list(inventory.keys())[i]}")
            print(f"Medicine Name: {list(inventory.values())[i][0]}")
            print(f"Quantity: {list(inventory.values())[i][1]}")
            print(f"Price: ${list(inventory.values())[i][2]}")
            print("\n\n\n")
    
    elif ch==3:
        med_id=input("Enter Medicine ID to Update Quantity: ")
        qty=input("Enter the new Quantity: ")
        inventory.get(med_id)[1]=qty
        print("\n\n\n")
        print("Medicine quantity updated successfully.")
        print("\n\n\n")

    elif ch==4:
        med_id=input("Enter Medicine ID to Search: ")
        print("Medicine Details:")
        print(f"Medicine ID: {med_id}")
        print(f"Medicine Name: {inventory.get(med_id)[0]}")
        print(f"Quantity: {inventory.get(med_id)[1]}")
        print(f"Price: ${inventory.get(med_id)[2]}")
        print("\n\n\n")

    elif ch==5:
        break

 