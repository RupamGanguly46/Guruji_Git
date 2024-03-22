import numpy as np

# array array type

'''
arr = np.array('hello')
print(arr)
print(arr.dtype) # 'object' class but other category U5
print(type(arr))

arr = np.array([1, 2, 3])
print(arr)
print(arr.dtype)
print(type(arr))

arr = np.array([1, 2, 'hello'])  # Not homogeneous
print(arr)
print(arr.dtype) # 'object' class but other category U11
print(type(arr))

arr = np.array({'a':10, 'b':20})
print(arr)
print(arr.dtype)  # 'object' class
print(type(arr))

'''

arr = np.arange(1, 11, 1).reshape(2, 5)
print(arr)

out = np.sum(arr, axis=0) #along rows/vertically
print(out)

out = np.sum(arr, axis=1) #along columns/horizontally
print(out)

# axis=3 can be used for 3rd dimension.. and so on.. number of axes= number of dimensions

out = np.max(arr, axis=0) # for finding max element among same columns

# By default, axis=none, performs operation on 'all' elements.

a = 3.4999999999999999
print(round(a, 2))
print(round(a))

a = np.array([3.5, 2.33, 1.009])
out = np.round(a)
print(a)

# ceil(), floor()
# ones(), zeroes(), empty()
# linspace, arange()

# dtype=int,float,complx,bool are for numbers, rest all are treated as objects

# for transposing our array
# np.transpose(arr)
# array.T

# for flattening matrix/base array
# arr.flatten()
# arr.base()