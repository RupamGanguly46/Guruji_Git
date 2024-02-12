# Significace of 'self'

class cat:
    def add(name,sex):
        cat.name=name
        cat.sex=sex
    def show():
        return [cat.name,cat.sex]

obj=cat
obj.add('billu','male')
obj.add('billi','female')
print(obj.show())

obj=cat()
obj.add('billu','male')
obj.add('billi','female')
print(obj.show())

class cat:
    def add(self,name,sex):
        self.name=name
        self.sex=sex
    def show(self):
        return [cat.name,cat.sex]

obj=cat
obj.add('billu','male')
obj.add('billi','female')
print(obj.show())

obj=cat()
obj.add('billu','male')
obj.add('billi','female')
print(obj.show())




# When you do obj = cat, you are not creating an instance of the class cat;
#  instead, you are creating an alias or reference to the class itself. 
# This means obj now points to the class cat, and you can use it to access class-level 
# attributes or methods.

# In your code:

# python

# obj = cat
# cat.add('billu', 'male')
# cat.add('billi', 'female')
# print(cat.show())

# Here, you are directly calling the add method on the class cat and
#  setting class attributes cat.name and cat.sex. This is possible because in
#  Python, classes themselves are objects, and you can assign attributes to them.
#  However, these attributes are shared among all instances of the class.

'''
    The self parameter is used in instance methods to refer to the instance of the class.
    When you create an instance (obj) and call an instance method (obj.add), the self parameter is implicitly passed, and it refers to that instance.
    The usage of class attributes (cat.name and cat.sex) directly within the methods is unconventional and can lead to unexpected behavior. Typically, you would use self.name and self.sex to work with instance attributes.
'''

# cat.name= somethig gives value to property/attribute of whole class, that is it will be shared with all instances
#  self.name= something gives value to attribute of that instance
# obj=cat assigns class to variable obj. now obj.add will assign values to whole class attributes.
# obj=cat() assigns instance to variable obj. now obj.add will assign values to that instance attributes.