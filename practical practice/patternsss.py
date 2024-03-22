# upper right triangle

rows=5
for i in range(1,rows+1):
    for j in range(i-1):
        print(' ',end='')
    for j in range(rows+1-i):
        print('*',end='')
    print()

print("OR")
for i in range(1,rows+1):
    print(' '*(i-1)+'*'*(rows-i+1))

print("\n\n")

# upper left triangle

rows=5
for i in range(1,rows+1):
    for j in range(rows+1-i):
        print('*',end='')
    for j in range(i-1):
        print(' ',end='')
    
    print()

print("OR")
for i in range(1,rows+1):
    print('*'*(rows-i+1)+' '*(i-1))

print("\n\n")

# lower right triangle

rows=5
for i in range(1,rows+1):
    for j in range(rows+1-i):
        print(' ',end='')
    for j in range(i):
        print('*',end='')

    print()

print("OR")
for i in range(1,rows+1):
    print(' '*(rows-i+1)+'*'*(i))

print("\n\n")

# lower left triangle

rows=5
for i in range(1,rows+1):
    for j in range(i):
        print('*',end='')
    for j in range(rows+1-i):
        print(' ',end='')
    print()

print("OR")
for i in range(1,rows+1):
    print('*'*(i)+' '*(rows-i+1))
