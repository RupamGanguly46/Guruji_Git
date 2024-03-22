'''
rows=5
for i in range(1,rows+1):
    for j in range(rows+1-i):
        print(' ' ,end='')
    for j in range(i):
        print('*',end='')
    for j in range(i-1):
        print('*',end='')
    print()


rows=5
for i in range(1,rows+1):
    if (rows+1-i)%2!=0 and i%2!=0:
        for j in range(rows+1-i):
            print(' ',end='')
        for j in range(i):
            print('* ',end='')
        print()
    


rows=5
for i in range(1,rows+1):
    print((' '*(rows+1-i))+('*'*i))

'''

