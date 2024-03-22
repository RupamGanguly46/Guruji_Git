# dics={"dic1":{1:"First",2:"Second"},"dic2":{3:"Third",4:"Fourth"}}
# for i in dics:
#     print(i,":")
#     for j in dics[i]:
#         print(j,"-",dics[i][j])

# num=int(input("Enter number of key-value pairs you want to add"))
# dic={}
# for iter in range(num):
#     key,pair=input("Enter space seperate key value pair").split()
#     if key.isdigit()==True:
#         key=eval(key)
#     if pair.isdigit()==True:
#         pair=eval(pair)
#     dic.update({key:pair})
# print()
# print(dic)
# for i in dic:
#     print(i,':',type(i),'\t',dic[i],':',type(dic[i]))

dic={"John":85,"Jane":90,"Bob":75,"Alice":95}
dic["Sam"]=80
dic.update({"Bob":80})
dic.remove("Jane")
print(dic)