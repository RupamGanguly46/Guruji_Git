# tup=(1,2,3,4,5,6,7,8)
# a,_,_,_,*c=tup
# print(a,type(a),c,type(c),type(tup))

# inpulist=input("Enter").split()
# mapp=map(int,inpulist)
# obj1=next(mapp)
# obj2=next(mapp)
# print(obj1,obj2,list(mapp))

# mapp=map(int,inpulist)
# for i in mapp:
#     print(i)

# switch=int(input("Enter"))
# a=["On" if switch==1 else "Off" if switch==0 else "Stuck" ]
# print(a)

# start,end=list(map(int,input("Enter start and end value").split()))
# for num in range(start,end+1):
#     print(num,end='')
#     print(": Good Student!") if num%2==0 and num%3==0 else print(": Good") if num % 2 == 0 else print(": Student") if num % 3 == 0 else print()

# start,end=[int(i) for i in input().split]

# lis=[i**2 for i in range(1,10) if i%2==0]
# print(lis)

gen=(i**2 for i in range(10))
tup=tuple(gen)
print(tup,gen)