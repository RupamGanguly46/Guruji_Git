lst=eval(input("Enter list"))
lst2=[]
for i in lst:
    count=0
    if i not in lst2:
        for j in lst:
            if i==j:
                count+=1
        print(f"Count of {i} is {count}")
        lst2.append(i)

