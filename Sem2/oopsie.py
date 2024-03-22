# instance variable vs class variable
# instance method vs class method

class Cat:
    pair=4 #class variable
    def __init__(self):
        print('meow')
    
    def naamkaran(self,naam,umar,sex):
        self.name=naam #instance variable 'name'
        self.age=umar
        self.gender=sex
    
    @classmethod
    def classwalamethod():
        print('koi kaam')

    def __del__(self):
        print('ouch')

pussy=Cat()
pussy.naamkaran('katrina',30,'salmankesaath')

pussy2=Cat()
pussy2.naamkaran('deepika',50,'ranbirkesaath')

Cat.classwalamethod

print(pussy.name)



    
    

