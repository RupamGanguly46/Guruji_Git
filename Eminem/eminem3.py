s1=eval(input("Enter side 1"))
s2=eval(input("Enter side 2"))
s3=eval(input("Enter side 3"))
res="Yes, it is triangle." if s1+s2>s3 and s2+s3>s1 and s3+s1>s2 else "Not a triangle."
print(res)