'''fibonacci series 
(0,1,1,2,3,5,8,13..)
a=0
b=1
l=[a,b]
n=int(input('Enter number of items in series to be displayed'))
for i in range(n):
    print(f"Item number: {i+1}",end="\t\t")
    if i==0:
        print(a)
        continue
    print(b)
    l.append(b)
    c=a
    a=b
    b+=c   
print(f"The series is : {l}")'''

limit=int(input('Enter limit'))
num1=0
num2=1
num3=0
print(f"[{num1},{num2},{num3}]")
print(num1)
for num in range(1,limit+1):
    num1=num2
    num2=num3
    num3=num1+num2
    print(f"[{num1},{num2},{num3}]")
    print(num3)