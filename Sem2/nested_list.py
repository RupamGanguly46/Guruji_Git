def minfind(n,ls):
    for i in range(n-1):
        a=min(ls)
        while True:
            if a in ls:
                ls.remove(a)
            else:
                break
    return min(ls)


# inpu=input().split('\n')
# lis=[]

# for i in range(0,len(inpu),2):
#     arecord=[inpu[i],inpu[i+1]]
#     lis.append(arecord)

n=int(input())
lis=[]
for i in range(n):
    a=input()
    b=float(input())
    lis.append([a,b])
    
grades=[]

for record in lis:
    grades.append(record[1])

second_lowest_grade=minfind(2,grades)

names=[]

for record in lis:
    if second_lowest_grade in record:
        names.append(record[0])

names.sort()
for name in names:
    print(name)
