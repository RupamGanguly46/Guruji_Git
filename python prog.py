start=int(input("Enter start value"))
end=int(input("Enter end value"))

print(f"Even numbers between {start} and {end}")
for i in range(start,end+1):
    if i%2==0:
        print(i,"even")
    
print(f"Odd numbers between {start} and {end}")
for i in range(start,end+1):
    if i%2!=0:
        print(i,"odd")
