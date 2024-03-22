# Console based projects AnikAcherjeeSir

# Declaring a dictionary
Car = {"Brand":"Mercedes",
       "Model":"Coupe",
       "Color":"White"}

# Using dictionary functions
x= Car.keys()
y= Car.values()
z= Car.items()

print(f"Before changing, {x=}\n\n{y=}\n\n{z=}\n\n")

# Inserting another key in a dictionary
Car["Price"]=4500000

# Comparision
print(f"After changing, {x=}\n\n{y=}\n\n{z=}\n\n")

# Type of values returned by dictionary functions
print(f"{type(x)=}\n{type(y)=}\n{type(z)=} ")

# Using z i.e. dcitionary.items() to print dictionary ot take out values.
for i in z:
    for j in i:
        print(j,end=" ")
    print("\n")

# Updating dictionary using another dictionary
OtherDetails={"Class":"G"}
Car.update(OtherDetails)
print(Car)

# Popping items in dictionary
poppedItem=Car.popitem()
print(f"\nWe popped {poppedItem} from \n{Car}")

# Clearing or deleting
choice=int(input("What do u want to do?"))
if choice==1:
    Car.clear()
elif choice==2:
    del Car["Brand"]    
elif choice==3:
    del Car
print(Car)
