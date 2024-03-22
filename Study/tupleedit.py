# write a program in python to change the marks of given student
# from given list of tuples/records by accepting name from user.

# list=[('Rupam',27),('Shubhang',26),('Kamal',25)]
# name,newmarks=input("Enter name and new marks").split()
# for index in range(len(list)):
#     if list[index][0].upper()==name.upper():
#         tup=list.pop(index)
#         list.append((tup[0],newmarks))
# print(list)

lis=[('Rupam',27),('Shubhang',26),('Kamal',25)]
name=input("Enter name of student")
newmarks=int(input("Enter new marks of student"))
for tupl in lis:
    if tupl[0].lower()==name.lower():
        ind=lis.index(tupl)
        lis.remove(tupl)
        tupl=list(tupl)
        tupl[1]=newmarks
        tupl=tuple(tupl)
        lis.insert(ind,tupl)

print(lis)