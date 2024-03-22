side1,side2,side3=eval(input("Enter 3 sides"))

if side1==side2==side3:
    tri_type="equilateral"
elif side1==side2 or side2==side3 or side3==side1:
    tri_type="isosceles"
else:
    tri_type="scalene"
print(f"The triangle is {tri_type}")