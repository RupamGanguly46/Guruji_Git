import numpy as np

# ls = [1, 10, 5, 800, 10000, 70]
# arr=np.array(ls)
# print(ls)
# print(arr)
# print(type(arr))

# # total space occupied by each element: number of charachters in most long element

# # numpy is faster than list

import time

# data = range(100000)
# a=time.time()
# arr = np.array(data)
# b=time.time()
# lst=list(data)
# c=time.time()

# print(f"Time taken by array: {b-a}")
# print(f"Time taken by list: {c-b}")

# # time.time() gives current time

# ls=[1,2,3,4]
# n=np.array(ls)

# strt = time.time()
# list_data = [i*2 for i in ls]
# stop = time.time()
# print('List Time', stop-strt)

# strt = time.time()
# list_data = n*2
# stop = time.time()
# print('Array Time', stop-strt)

# # List operation is slower than array
# # numpy is made using mostly C and other languages too

class array:
    def __init__(self, lst):
        self.lst = lst
    
    def __str__(self):   #used when object/instance converted to string
        print(str(self.lst))
        st = str(self.lst).replace(',', '')
        return st
    
    def __add__(self, other):
        first=self.lst
        second=other.lst

        # return [i+j for i in self.lst for j in other.lst if len(self.lst)==len(other.lst)]

        # firstlen=len(first)
        # seclen=len(second)
        # if firstlen==seclen:
        #     return [i+j for i in self.lst for j in other.lst]
        # else:
        #     return "Error"

        try:
            return [self.lst[i]+other.lst[i] for i in range(len(self.lst))]
        except Exception as e:
            print(e)
            
            

        


lst1 = [2, 3, 5]
lst2 = [1, 2, 3, 4]

arr1 = array(lst1)
arr2 = array(lst2)

print(arr1 + arr1)
print(arr1 + arr2)

# # arr1 = np.array([1, 2, 3]) this will cause error on addition as number of elements not same
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([5, 6, 7, 8])
# print(arr1+arr2)






