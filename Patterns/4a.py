rows=int(input("Enter numbers"))
for i in range(1,rows+1,2):
    print(str(i)*i)

for j in range(rows,0,-2):
    print(str(j)*j)