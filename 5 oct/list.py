#don't use sum variable and sum function, name differently 
#if u pop in loop, list length reduces everytime, loop length reduces
lst=eval(input("Enter a list"))
lst2=list()
total=0
len=len(lst)
for i in lst:
    if isinstance(i,int):
        total+=i
    else:
        lst2.append(i)
        lst[lst.index(i)]=''
for i in range(lst.count('')):
    lst.remove('')
print(lst,lst2)
print(f"Sum of numeric items in list is: {total}")
print("Sum of integers using list method",sum(lst))

