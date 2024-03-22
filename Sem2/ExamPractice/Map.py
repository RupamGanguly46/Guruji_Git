def apna_fun(x):
    print(x)

a=map(apna_fun,[3,10,34])
print(a)

# this is not enough, it will not return anything
# memory is not yet used
# bullets are loaded but not shot uk

# type cast using function, for loop iteration over the map, next()

print(list(a))
# gives 
# 3
# 10
# 34
# [None, None, None]

# after using up the mapping, we lose the map, so list is emptied, we can't fetch anymore

print(list(a))
# no error

# print(next(a))
# give error

def apna_fun(x):
    return x

a=map(apna_fun,[3,10,34])
print(list(a))

print(list(a))
# won't give error, it will give empty list

# print(next(a)) 
# will give error as no more item can be fetched


# list supports iteration, it is iterative object, loop can be run on them
# list is not iterable, you get error on using next(list)
# to create iterable object you can use iter()


