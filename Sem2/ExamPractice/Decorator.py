
def add(a, b):
    return a+b

def deco(fun):
    def wraper(a, b):
        print('This is Addition')
        return fun(a, b)
    return wraper


# wraper is the finishing function which returns the output
# wraper is like the bullet loader, but we don't need to shoot

'''
re=deco(add)
out=re(3,5)
print(out)
'''

# we are modifying our function.
# flow managing
# function is passed as an argument to our decorator

re=add(3,5)
print(re)

re=deco(add(3,5))
print(re)