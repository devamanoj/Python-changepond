#create an abstract class car which will have abstract methods related to a car 
#functionality(start_engine,stop_engine) implement concrete subclasses(ElectricCar,Gasolinecar)
#use the concrete subclasses (operate_car)
from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass

class ElectricCar(car):
    def start_engine(self):
        return "car is on"
    def stop_engine(self):
        return "car is off"
class Gasolinecar(car):
    def start_engine(self):
        return "gascar is on"
    def stop_engine(self):
        return "gascar is off"

hyundai = ElectricCar()
print(hyundai.start_engine())
# print(hyundai.stop_engine())
bmw = Gasolinecar()
print(bmw.start_engine())