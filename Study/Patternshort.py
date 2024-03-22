# rows=5
# for i in range(1,rows+1):
#         print(' '*(rows-i),'*'*i,'*'*(i-1),' '*(rows-i+5),sep='')

rows=5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()