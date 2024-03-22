word=input("Enter a word\n")
pall=""
for index in range(len(word)):
    pall=word[index]+pall
print(f"It's pallindrome is - {pall}")