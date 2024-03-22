digit=0
n=int(input("Number of rows"))
flag=1
loop=0

for i in range(1,n+1):

    for j in range(i-1):
        print(' ',end='')

    for j in range(n-i+1):
        print(digit,end='')

        if digit==0:
            flag=1
        elif digit==9:
            flag=0

        if flag==1:
            digit+=1
        elif flag==0:
            digit-=1
    
    for j in range(1,n-i+1):
        print(digit,end='')

        if digit==0:
            flag=1
        elif digit==9:
            flag=0

        if flag==1:
            digit+=1
        elif flag==0:
            digit-=1

    print()

for i in range(1,n+1):

    if loop==0:
        loop=1
        continue

    for j in range(1,n-i+1):
        print(' ',end='')

    for j in range(i):
        print(digit,end='')

        if digit==0:
            flag=1
        elif digit==9:
            flag=0

        if flag==1:
            digit+=1
        elif flag==0:
            digit-=1
    
    for j in range(i-1):
        print(digit,end='')

        if digit==0:
            flag=1
        elif digit==9:
            flag=0

        if flag==1:
            digit+=1
        elif flag==0:
            digit-=1

    print()


