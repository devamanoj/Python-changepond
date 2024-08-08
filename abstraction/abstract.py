#abstraction:
#abc = abstract base class  is used for creating abstract classes 
#an abstract class is a class that cannot be instantiated and is designed to be a base class for
#other classes 
#it is a common interdface for a group of subclasses 
from abc import ABC, abstractmethod
class Myabstractclass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass
#implement abstract method in subclasses
class Concreteclass(Myabstractclass):
    def my_abstract_method(self):
        print('Implement of the abstract method')