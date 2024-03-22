# 1 to 20: as it is
# 20 onwards: even as it is, odd factorial

def program():
    start,end=input("Enter starting number and ending number").split(',')
    start,end=int(start),int(end)
    for num in range(start,end+1):
        if num<=20:
            print(num)
        else:
            if num%2==0:
                print(num)
            else:
                factorial=1
                for integer in range(1,num+1):
                    factorial*=integer
                print(f"Factorial of {num} is {factorial}.")

while True:
    ch=input("Do you wish to run program")
    if ch=='y':
        program()
    else:
        break

