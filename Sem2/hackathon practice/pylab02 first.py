# Binary Bits 1
a, b = input().split()   # reading 2 space separated values given in single line  
a = int(a)
b = int(b)
k = int(input())  # read thersold 

# logical section 
re1 = a & b  # bitwise and 
re2 = a | b  # bitwise or 
re3 = a ^ b  # bitwise xor

# filter avoid the value greater than thersold 
re1 *= re1 < k
re2 *= re2 < k
re3 *= re3 < k

# display largest value amoung three re1, re2 and re3 
re = max(re1, re2, re3)
print(re)
