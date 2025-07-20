import math

class Circle:
    def __init__(self,radius):
        if radius<0:
            raise ValueError("Radius should be positive number")
        self.radius=radius
    
    def area(self):
        return math.pi * self.radius **2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def diameter(self):
        return 2 * self.radius