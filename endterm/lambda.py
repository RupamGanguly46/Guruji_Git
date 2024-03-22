ls=["abcdefghijkz","jklmn"]
#sort in reverse with first letter of string's ascii value's square

# ls.sort(reverse=True,key=lambda st:ord(st[0])**2)
# print(ls)

# print(max(ls,key=lambda st:st[-1]))


# map1=map(lambda x:[i**2 for i in range(1,x+1)],[i for i in range(1,11)])

# while True:
#     print(next(map1))

# filter()

# ls=[1,2,3,4,5]
# print(list(filter(lambda num:True if num>3 else False,ls)))
# # or
# print(list(filter(lambda num:num>3,ls)))

ls=["Abc","abc","Bcd","bcd"]
# def cap(st):
#     return st.capitalize()==st
# out=list(filter(cap,ls))


# out=list(filter(lambda st:st.capitalize()==st,ls))

out=[st for st in ls if st.capitalize()==st]
print(out)

