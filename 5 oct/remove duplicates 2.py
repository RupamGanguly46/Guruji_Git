GivList=eval(input("Enter a list"))
UniqList=[]
for item in GivList:
    if item not in UniqList:
        UniqList.append(item)
print("List after removing duplicates is",UniqList)


