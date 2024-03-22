# You are given a list of integers. 
# Write a Python program that squares each element of the list 
# and then filters out the even squared numbers. Finally, 
# print the resulting squared and filtered list in a single line.

inp=input("Enter space seperated integers").split()
ls=list(map(lambda x:int(x)**2,inp))
ls=list(filter(lambda x:x%2!=0,ls))
print(*ls)

# or

print(*[int(x)**2 for x in inp if int(x)**2%2!=0])