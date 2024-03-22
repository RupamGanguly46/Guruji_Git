user_input=input("Enter numbers seperated by spaces: ")
numbers=list(map(int,user_input.split()))
squared_numbers=list(map(lambda x: x**2,numbers))
print(f"Original Numbers: {numbers}")
print(f"Squared Numbers: {squared_numbers}")

even_odd_checker = list(map(lambda x: "Even" if x%2==0 else "Odd",numbers))
print("Results:",even_odd_checker)

evensquareoddcube= list(map(lambda x: x**2 if x%2==0 else x**3,numbers))
for i in evensquareoddcube:
    print(f"for {numbers[evensquareoddcube.index(i)]} : {i}")

