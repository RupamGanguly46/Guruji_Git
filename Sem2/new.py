# a=1
# def fun():
#     # a=a+1 gives unbound error
#     print(a)
#     # a=a+1 also gives error
# fun()

a=1
def fun():
    # print(a) gives error as another a is used afterwards which is local
    a=10
    print(a)
fun()

