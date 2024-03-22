#prime number: reverse and sum of digit

def program():
    
    start=int(input("Enter starting number"))
    end=int(input("Enter ending number"))

    for number in range(start,end+1):
        isprime=True
        for factor in range(2,number//2+1):
            if number%factor==0:
                isprime=False
        if isprime==True:
            
            print("The prime numbers are:")
            print(f"{number} \n ____________")

            reversed=0
            sum=0

            while number>0:
                last_digit=number%10
                reversed=reversed*10+last_digit
                number=number//10
                sum+=last_digit
            
            print(f"The reversed number is {reversed}")
            
            print("Sum of it's digits, i.e.",end='')
            # for i in range(len(str(number))):
            #     if i!=len(str(number))-1:
            #         print(str(i)+"+")
            #     else:
            #         print(str(i))
            print(f"is {sum}\n\n")

program()


            
