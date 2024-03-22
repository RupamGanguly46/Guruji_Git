def star_pattern(n):
    spaces=n
    for i in range(1,n+1):
        for j in range(1,spaces+1):
            print(' ',end='')
        for k in range(1,i+1):
            print('*',end='')
        print()
        spaces=spaces-1
n=int(input('enter number of rows'))
star_pattern(n)