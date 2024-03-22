rows=5
saptak=["Sa","Re","Ga","Ma","Pa","Dha","Ni"]
ind=0
for i in range(1,rows+1):
    for j in range(i):
        print(saptak[ind],end='')
        ind+=1
        if ind==7:
            ind=0
    ind-=1
    print()
