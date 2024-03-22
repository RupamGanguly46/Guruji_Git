list1=eval(input("Enter First List"))
list2=eval(input("Enter Second List"))
intersec=[]
for item1 in list1:
    for item2 in list2:
        if item1==item2:
            intersec.append(item1)
print("Intersection is",intersec)
