def display_available_items(dct):
    for x,y in dct.items():
        if x==1:
            print(f'{"S.No.":<10}{"Item":<15}{"Quantity":<15}{"Cost/Item"}')
        print(f"{x:<10}",end="")
        for i in range(3):
            print(f"{list(y.values())[i]:<15}",end="")
        print()

availableItems = {1: {'Item': 'Biscuits', 'Quantity': 5, 'Cost/Item': 20.5}, 
2: {'Item': 'Chocolates', 'Quantity': 10, 'Cost/Item': 35}, 
3: {'Item': 'Coffee', 'Quantity': 25, 'Cost/Item': 55},
4: {'Item': 'Chips', 'Quantity': 10, 'Cost/Item': 50},
5: {'Item': 'Cream', 'Quantity': 5, 'Cost/Item': 30}}

display_available_items(availableItems)

# val=1000
# st=f"result is {val:<10} hi"
# print(st)

