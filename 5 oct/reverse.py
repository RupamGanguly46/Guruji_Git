lst=eval(input("Enter list"))
for i in range(-1,-len(lst)-1,-1):
    print(lst[i])

#or

for i in range(len(lst)-1,-1,-1):
    print(lst[i])