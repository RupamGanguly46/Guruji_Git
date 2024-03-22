rows=int(input())
count=0
reverse=0

for row in range(1,rows+1):
    for space in range(row-1):
        print(' ',end='')
    
    for number in range(rows+1-row):
        print(count,end='')

        if count==0:
            reverse=0
        elif count==9:
            reverse=1
        
        if reverse==0:
            count+=1
        elif reverse==1:
            count-=1
    
    for number in range(rows-row):
        print(count,end='')

        if count==0:
            reverse=0
        elif count==9:
            reverse=1
        
        if reverse==0:
            count+=1
        elif reverse==1:
            count-=1
    print()

for row in range(1,rows):

    for space in range(2,rows+1-row):
        print(' ',end='')
    
    for number in range(row+1):
        print(count,end='')

        if count==0:
            reverse=0
        elif count==9:
            reverse=1
        
        if reverse==0:
            count+=1
        elif reverse==1:
            count-=1
    
    for number in range(row-1):
        print(count,end='')

        if count==0:
            reverse=0
        elif count==9:
            reverse=1
        
        if reverse==0:
            count+=1
        elif reverse==1:
            count-=1
    print()




