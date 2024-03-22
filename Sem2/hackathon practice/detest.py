# Detest of an integer for given number

# detest_of_what=int(input("Enter which number you dislike"))
# check_number=int(input("Enter number to be checked"))

# if check_number%detest_of_what!=0 and check_number%10!=detest_of_what:
#     print("Great! I like this number")
# else:
#     print("I hate this number")

# List of all positive integers chosen with a detest of a number

# Print the Nth integer which you don't dislike 
# if number is multiple of the detest number or it's last digit
# is equal to the detest number, then you dislike it.

detest_of_what=int(input("Enter number which you don't like"))
end_point=int(input("Enter position till we need to check"))

i=1
count=0
while True:
    if i%detest_of_what!=0 and i%10!=detest_of_what:
        count+=1
        if count==end_point:
            break
    i+=1
print(f"{i} is the {end_point}{'st' if end_point==1 else 'nd' if end_point==2 else 'rd' if end_point==3 else 'th'} number which I like.")


