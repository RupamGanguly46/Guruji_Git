#pallindrome
'''
pattern
*
**
***
****
*****
'''

'''
n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        if col==row:
            print('*',end='\n')
        else:
            print('*',end='')
'''

n=5
for i in range(1,n+1):
    print('*'*i)
        
        

    
