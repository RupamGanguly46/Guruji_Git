def divisorlist(str1,L):
    match="True"
    firststr=''
    for end in range(len(str1)): #number of letters in one check group
        e=end+1
        
        if e>=len(str1)-1:
            break

        firststr=str1[0:e]

        if len(firststr)>len(str1)-len(firststr):
            break

        s=e
        e=(e)+len(firststr)

        for seconds in range(len(str1)-len(firststr)): #next groups check
            
            if e>len(str1):
                break

            secondstr=str1[s:e]

            if firststr!=secondstr:
                match="False"
                break
            else:
                match="True"
            s=e
            e+=len(firststr)
        if match=="True":
            L.append(firststr)
L1=[]
L2=[]
str1,str2=input("Enter space seperated string").split()
divisorlist(str1,L1)
divisorlist(str2,L2)
x=''
for item in L1:
    if item in L2:
        x=item
        break
print(x)



