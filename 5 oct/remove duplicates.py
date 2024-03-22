ls=eval(input("Enter list"))

for index in range(len(ls)):

    item=ls.pop(index)

    for remindex in range(len(ls)):
        if ls[remindex]==item:
            ls[remindex]=''

    ls.insert(index,item)

empty=ls.count('')

for iter in range(empty):
    ls.remove("")
    
print(ls)
