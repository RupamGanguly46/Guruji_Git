from abc import ABC, abstractmethod

class Sample(ABC):

    # This is a mandatory method
    @abstractmethod
    def add(self, a, b):
        return a + b
    
    # This is optional
    def sub(self, a, b):
        return a - b
    
# obj=Sample() 
# gives error, as abstract class can not construct object/instance
    
# class Test(Sample):
#     pass
# obj=Test()
# gives error, as class inheriting abstract class must contain 
# abstract method of add()
    
class Test(Sample):
    def add(self, a, b):
        return super().add(a, b)

