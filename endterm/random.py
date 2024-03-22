from random import random,randrange,randint as r
a=str(r(10000,20000))[-4:]
print(a if int(a)<1000 else None)

