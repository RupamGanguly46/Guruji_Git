'''
num1=input("Enter number")
for i in range(len(num1)-1,-1,-1):
    print(num1[i],end='')
'''
num=int(input("Enter a number"))
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
print(rev)