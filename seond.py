def display_available_items(dct):
    for x,y in dct.items():
        if x==1:
            print(f'{"S.No.":<10}{"Item":<15}{"Quantity":<15}{"Cost/Item"}')
        print(f"{x:<10}",end="")
        for i in range(3):
            print(f"{list(y.values())[i]:<15}",end="")
        print()

def display_user_demand(dct):
     print(f"{'Item':<10}{'Quantity'}")
     for key,value in dct.items():
          print(f"{key:<10}{value}")

def display_cart(dct):
    
    # Filtering Demand
    user=dct.items() 
    listofdict=list(availableItems.values())
    listofitems=[listofdict[i]['Item'] for i in range(5)]

    fixed=tuple(user)

    listofqtys=[listofdict[i]['Quantity'] for i in range(5)]

    for item,qty in fixed:
        if item not in listofitems:
            dct.pop(item)
        else:
            for Qty in listofqtys:
                if qty>Qty:
                  dct.pop(item)
                  break
            
    
        
    
    print(user)


availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

display_available_items(availableItems)

userDemand = {}
CustomerName = input("Enter Customer Name ")
CustomerAddress = input("Enter Customer Address City/State ") 
numberOfItem = int(input('Enter the number of item to be purchased '))
for _ in range(numberOfItem):
	Item = input('Enter the Item Name ') 
	Quantity = int(input('Enter the Quantity '))
	userDemand[Item] = Quantity
     

display_user_demand(userDemand)
display_cart(userDemand)

if userDemand=={}:
    print("Sorry bruh, we don't have what u need.")
     

     

     

     