class car:
    # name model year price
    def __init__(self,maker,name,model,year,price):
        self.maker=maker
        self.name=name
        self.model=model
        self.year=year
        self.price=price
        self.available=True
    def details(self):
        return f'''
Maker:{self.maker:>15}
Name:{self.name:>15}
Model:{self.model:>15}
Year:{self.year:>15}
Price:{self.price:>15}
'''

class dealership:
    def __init__(self,name) ->None:
        self.name=name
        self.inventory=[]
    def add(self,cars):
        if type(cars)==list:
            self.inventory.extend(cars)
        else:
            self.inventory.append(cars)
    def display_available_cars(self):
        count=1
        for acar in self.inventory:
            if acar.available==True:
                print(count)
                print(acar.details())
                count+=1
    def sellcar(self,cus,carnum):
        if 0 < carnum <= len(self.inventory) and self.inventory[carnum-1].available:
            cus.purchase(self.inventory[carnum-1])
            self.inventory.pop(carnum-1)
            # return something





class customer:
    def __init__(self,name):
        self.name=name
        self.purchased_car=[]
    def purchase(self,acar):
        if acar.available:
            self.purchased_car.append(acar)
            acar.available=False
        else:
            print("Car not available")

# Main Code
car1=car('Suzuki','Dzire','VDI',2019,700000)
car2=car('BMW','Competition','M3',2017,30000000)
car3=car('Tata','Nano','Zero',2012,114000)

# print('Car Details:',car1.details(),car2.details(),car3.details(),sep='\n')

dealer1=dealership("Arvind Chip Wala")
dealer1.add([car1,car2])
dealer1.add(car3)
dealer1.display_available_cars()

cusname=input("Enter Customer Name")
carnum=int(input(f"Enter the car number [1-{len(dealer1.inventory)}]"))
customer1=customer(cusname)

ret=dealer1.sellcar(customer1,carnum)
if ret:
    print(f'{customer1.name} purchased car\n{ret.display_car()}')
else:
    print(f'Car not available')

print('\nAfter selling available cars')
dealer1.display_available_cars()




