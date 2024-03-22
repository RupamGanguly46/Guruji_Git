'''
print('"hello"',"'hello'",'\'hello\'',"\"hello\"")
print("Rupam"+" "+"Ganguly")
print("yes! "*3)
print(len("Oolaalaa"))

'''
rows=int(input())
n=int(input())
for i in range(1,rows+1):
    for space in range(rows-i):
        print(" ",end='')
    for j in range(i):
        if i==n:
            if j!=i-1:
                print('**',end='')
            else:
                print('*',end='')                
        else:
            if j==0 or j==i-1:
                print('* ',end='')
            else:
                print("  ",end='')
    print()