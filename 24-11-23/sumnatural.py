def sumnat(start,end):
    sum=0
    for number in range(start,end+1):
        sum+=number
    return sum
first,second=input("Enter comma seperated start and end values").split(",")
first=int(first)
second=int(second)
if first<second:
    print(sumnat(first,second))
else:
    print(sumnat(second,first))
