#khai bao thu vien
from abc import ABC, abstractmethod

#Abstract  class Vehicle
class Vehicle(ABC):
    def __init__(self,make,model,year):
        self.__make = make #__privateproerty
        self.__model = model
        self.__year = year
        #__(2 gạch dưới: private):__make
        #_(1 gạch dưới: protected):_name
        # (0 gạch :public):name



    @abstractmethod
    def maintance_cost(self):
        pass
    @abstractmethod
    def max_speed(self):
        pass

    def get_vehicle_info(self):
        return f"{self.__year}{self.__make}{self.__model}"

class Car(Vehicle): #Ke thua
    def __intit__(self, make, model, year):
        super().__intit__(make, model, year)
        self.doors = doors

    def maintance_cost(self):
        return 100 + (self.doors*50)
    
    def max_speed(self):
        return 500


class Motocycle(Vehicle):
    def __intit__(self, make, model, year):
        super().__init__(make. model, year)
        self.type_of_bike = type_of_bike

    def maintance_cost(self):
        return 500 if self.type_of_bike == 'sport' else 200
    
    def max_speed(self):
        return 150 if self.type_of_bike =='sport' else 110
    
def display_vehicle_details(vehicle): #Da hinh
    print(f"Vehicle: {vehicle.get_vehicle_info()}")
    print(f"Max speed: {vehicle.max_speed()} km/h")
    print(f"Maintance cost: ${vehicle.maintance_cost()} per year")

# tao object car motocyc
car = Car|("Toyota", "Camry", 2024,4)
Motocycle = Motocycle("Yamaha", "YAMZ-Y1", 2024,"sport")

display_vehicle_details(car)
display_vehicle_details(Motocycle)