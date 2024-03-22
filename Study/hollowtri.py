# rows=5
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(' ',end='')
#     for j in range(i):
#         if i!=rows:
#             if j==0:
#                 print('*',end='')
#             else:
#                 print(' ',end='')
#         else:
#             print('*',end='')
#     for j in range(i-1):
#         if i!=rows:
#             if j!=i-2:
#                 print(' ',end='')
#             else:
#                 print('*',end='')
#         else:
#             print('*',end='')
#     print()

rows=5
for i in range(1,rows+1):
    for j in range(rows-i):
        print(' ',end='')
    for j in range(2*i-1):
        if j==0 or j==(2*i-2) or i==rows:
            print('*',end='')
        else:
            print(' ',end='')
    print()
