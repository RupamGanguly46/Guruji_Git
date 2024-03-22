a=[0,1,2,3,4,5,6,7,8]

# for i in range(len(a)):
#     if i%2==0:
#         print(a[i])

# # or
        
# for i in a[::2]:
#     print(i)

# # or

# b=a.copy()  
# for i in b:
#     index=b.index(i)
#     if index%2==0:
#         print(i)
#     # This won't work if there are multiple items of same value
#     b.pop(index)
#     b.insert(index,'')
#     # This will ensure that once an item is used, it is removed so that
#     # another item with same name will be operated next time, not the first one
#     # as python list functions always take up the first occurence of similar items

# # or

# z=[print(i) for i in a[::2]]

# # or

a=list(map(lambda x: print(x),a[::2]))

# or

a=list(filter(lambda index: index%2==0,))