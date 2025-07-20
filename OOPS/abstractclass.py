# define:a class canot instatiated on its own meant to be subclassed 
# they can contain abstract methods, which are declared but no implementation .

from abc import ABC,abstractmethod

class vehicle:
    @abstractmethod
    def stop(self):
        pass
    def go(self):
        pass
class car(vehicle):

    def stop(self):
        print("stop")

    def go(self):
        print("go")

class motorcycle(vehicle):
    def stop(self):
        print("stop")

    def go(self):
        print("go")
    
car1=car()
car1.go()
car1.stop()