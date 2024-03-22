a=eval(input("Enter"))
b=eval(input("Enter"))
c=eval(input("Enter"))
l=[a,b,c]
for i in range(3):
    if l[0]>l[1] and l[0]>l[2]:
        print(l[0],"is greatest")
    a=l.pop(0)
    l.append(a)


    
    
    
