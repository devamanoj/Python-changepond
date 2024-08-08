from abc import ABC , abstractmethod
#defines an abstrcat base class
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
#define a concrete clas that inherits from the abstract base class
class dog(animal):
    def sound(self):
        return "barks"
class cat(animal):
    def sound(self):
        return "meow"
d = dog()
c = cat()
print(d.sound())
print(c.sound())