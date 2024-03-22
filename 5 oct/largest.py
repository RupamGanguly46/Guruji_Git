List=eval(input("Enter a list"))
largest=List[0]
for item in List:  
    if item>largest:
        largest=item
print(largest)
