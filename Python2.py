#Assignment 9: Triangle Classification using nested if else statements

side1, side2, side3=eval(input("Enter sides of triangle"))

if(side1==side2):
    if(side2==side3):
        print("All sides are equal, hence equilateral triangle")
    else:
        print("Only side 1 and side 2 are equal,hence isosceles triangle")
else:
    if(side2==side3):
        print("Only side 2 and side 3 are equal, hence isosceles triangle")
    else:
        if(side1==side3):
            print("Only side 1 and side 3 are equal, hence isosceles triangle")
        else:    
            print("No sides equal, hence scalene triangle")
        
    

    
