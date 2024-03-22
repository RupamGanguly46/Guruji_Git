from numpy import *

arr = array([[[1, 1, 1],[2, 2,],[3]],[[4],[5],[6]],[[7],[8],[2147483648]]])

print(type(arr), arr.ndim, arr.shape, arr.size, arr.dtype)

print(2**32/2)