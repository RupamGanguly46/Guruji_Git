ls=[1,2,3,4]
out=iter(ls)
print(out)
print(next(out))

# let's suppose, we have a box of items, box is memory, items are the values
# on other place, we have noted down, where the items are kept, we don't take
# the items from the box, similarly, actual data is kept in memory, but our 
# iter() only knows where the objects are. 

