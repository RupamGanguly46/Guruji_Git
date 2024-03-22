string=input("Enter string")
digits=""
alphabets=""
for i in range(len(string)):
    if string[i].isalpha():
        alphabets+=" "+string[i]
    elif string[i].isdigit():
        digits+=" "+string[i]
print(f"Digits are - {digits}\nAlphabets are - {alphabets}")