from itertools import *

lst=[1,2,3]
print([i for i in permutations(lst)])
print([i for r in range(1,len(lst)+1) for i in combinations(lst,r)])