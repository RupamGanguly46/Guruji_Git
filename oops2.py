class cat:
    def __init__(self):
        print('oye')

obj1=cat
obj1.a=10

obj2=cat()
obj2.a=5

obj3=cat()

print(obj1.a,obj2.a,obj3.a)

# obj3.a is not assigned by us but by obj1.a , 
# we assigned default 10 to every object until we change it manually

class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

# here, attr1 is class attribute but name is instance attribute.
