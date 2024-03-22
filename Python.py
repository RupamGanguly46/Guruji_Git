#Assignment28: Largest of two numbers

while True:
    num1=eval(input("Enter first number"))
    num2=eval(input("Enter second number"))
    a=type(1)

    if type(num1)!=a or type(num2)!=a:
        print(num1,num2,"(invalid)",sep='\t')
    elif num1<=0 or num2<=0:
        print(num1,num2,"(invalid)",sep='\t')
    elif num1==num2:
        print(num1,num2,"(both numbers are same)",sep='\t')
    else:
        if(num1>num2):
            print(num1,num2,"(valid)",f"{num1} is the largest and {num2} is the smallest",sep='\t')
        else:
            print(num1,num2,"(valid)",f"{num2} is the largest and {num1} is the smallest",sep='\t')

    ch=input("Wish to run program again?")
    if ch.upper()=="NO":
        break



