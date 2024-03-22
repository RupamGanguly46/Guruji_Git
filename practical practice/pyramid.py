#pyramid

# rows=int(input("Enter a number"))
# value=65
# for i in range(1,rows+1):
#     for j in range(rows+1-i):
#         print(' ',end='')
#     for j in range(i):
#         print(chr(value),end='')
#         value+=1
#         if value>90:
#             value=65
#     for j in range(i-1):
#         print(chr(value),end='')
#         value+=1
#         if value>90:
#             value=65
#     print()

rows=int(input("Enter"))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(' ',end='')
    if i==3:
        for j in range(2*i-1):
            print('*',end='')
    else:
        for j in range(i):
            if j==0:
                print('*',end='')
            else:
                print(' ',end='')
        for j in range(i-1):
            if j==(i-2):
                print('*',end='')
            else:
                print(' ',end='')
    print()