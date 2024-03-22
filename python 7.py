#factorial calculator

num=int(input('Enter number'))
fac=1
for iter in range(num):
    fac*=iter+1
print(f"Factorial is : {fac}")