word1=input("Enter")
word2=input("Enter")
result=''
letter=0
for letter in range(len(word2) if len(word1)>=len(word2) else len(word1)):
    result+=word1[letter]
    result+=word2[letter]
result+=word1[letter+1:len(word1)] if len(word1)>=len(word2) else word2[letter+1:len(word2)]
print(result)
