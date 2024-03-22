# this is a class that describes cars 

class car:
    def __init__(self,model,make,year_of_production,fuel_capacity,color):
        self.model = model
        self.make = make
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.color = color
    def print_make(self,make):
         print("the car is of {0} make".formart(self.make))

    def set_make(self,make):
        self.make = make
    def get_make(self):
        return self.make 
my_car = ("impalla","chevrolet","1960","2500 cc", "lilac")
friends_car = ("note","chevrolet","1960","2500 cc", "lilac")

print(my_car.get_make())
print(friends_car.get_make())


my_car
