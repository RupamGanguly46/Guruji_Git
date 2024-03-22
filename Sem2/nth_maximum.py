n=int(input("Enter nth maximum"))
ls=eval(input("Enter a list"))
for i in range(n-1):
    a=max(ls)
    while True:
        if a in ls:
            ls.remove(a)
        else:
            break
print(max(ls))
    

