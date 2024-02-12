# Car Dealership Inventory System 

# class car:
#     def __init__(self,company,model,price):
#         self.company=company
#         self.model=model
#         self.price=price
#     def details(self):
#         return 

# class sedan(car):

    
class shape:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width

class square(shape):
    def __init__(self,side):
        super().__init__(side,side)
    # def area(self):
    #     return f'The area is {super().area()}'
    
obj=square(5)
print(obj.area())
       
