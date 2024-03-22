import time as t
rows=5
patlen=4
space=4
for i in range(1,rows+1):
    for z in range(patlen):
        for j in range(rows-i):
            print(' ',end='')
        for j in range(i):
            print('*',end='')
        for j in range(i-1):           
            print('*',end='')
        for j in range(rows-i+space):
            print(' ',end='')
    t.sleep(0.25)
    print()
for i in range(1,rows+1):
    for z in range(patlen):
        for j in range(i-1):
            print(' ',end='')
        for j in range(rows-i+1):
            print('*',end='')
        for j in range(rows-i):
            print('*',end='')
        for j in range(i+space-1):
            print(' ',end='')
    t.sleep(0.25)
    print()

