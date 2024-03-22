# rows=5
# val=0
# for i in range(1,rows+5):
#     for j in range(i):
#         if val+1<10:
#             print(val+1,end='')
#         else:
#             val=0
#             print(val+1,end='')
#         val+=1
#     print()

rows=10
val=1
for i in range(1,rows+1):
    for j in range(i):
        print(val,end='')
        val+=1
        if val==10:
            val=1
    print()
    