# start=int(input("Enter starting number"))
# end=int(input("Enter ending number"))

# start,end=input("Enter space seperated start and end number").split()
# start,end=int(start),int(end)
# for num in range(start,end+1):
#     print(num,end='')
#     if num%2==0 and num%3==0:
#         print(": Good Student!")
#     elif num % 2 == 0:
#         print(": Good")
#     elif num % 3 == 0:
#         print(": Student")
#     else:
#         print()

# for num in range(start,end+1):
#     print(num,end='')
#     a=print(": Good Student!") if num%2==0 and num%3==0 else print(": Good") if num % 2 == 0 else print(": Student") if num % 3 == 0 else print()
# del a

# dic={}
# while True:
#     ch=input("Would you like to enter a record? (y/n)")
#     if ch=='y':
#         try:
#             key,pair=input("Enter space seperated item and price").split()
#         except:
#             print("Enter correctly")
#             continue
#         pair=int(pair)
#         dic.update({key:pair})
#     elif ch=='n':
#         break
#     else:
#         print("Enter your choice properly")
# print(dic)
# totalprice=0
# for item in dic:
#     totalprice+=dic[item]
# print(totalprice)

list1=[ "Rupam" , "Rajat" , "Shivam" , "Sadaf" ]
list2=[ 100 , 90 , 80 , 70 ]

dic={}
total_score=0
number_of_scores=0

for index in range( len(list1) ):
    dic[ list1[index] ] = list2[ index ]
print( dic )

for key in dic:
    total_score += dic[ key ]
    number_of_scores += 1
average_score = total_score / number_of_scores

print( average_score )
