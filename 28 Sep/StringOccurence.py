#stringoccurence, membershipoperator, listfunction
string=input("Enter")
l=[]
l3=[]
for i in string:
    if i not in l:
        print(f"Count of {i} is {string.count(i)}")
        l.extend([i])
        #or you can use l.append(i)
        l3.insert(string.count(i),i)
print(f"List of charachters used in string : {sorted(l)}",end=' ')
l2=[]
for i in range(len(l)):
    l2.append(ord(sorted(l)[i]))
print(f"i.e. {l2}")
for i in l2:
    print(f"The charachter for ascii value {i} is {chr(i)}")
print(l3)


        