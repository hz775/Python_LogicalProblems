class Person:
    def __init__(self):
        print("Hi i am Sai")
    
    def display(self):
        print("Hi")

class random(Person):
    def __init__(self):
        super().__init__()
        print("Hi i am Hemanth")
    
person2=random()
person2.display()


class Person:
    def __init__(self):
        self.name = "Sai"
        print("Hi I am Sai")
    
    def display(self):
        print(f"My name is {self.name}")

class Student(Person):  # Student extends Person
    def study(self):
        print(f"{self.name} is studying.")

# Creating object of child class
s = Student()
s.display()       # from parent
s.study()         # from child


class employee:
    def __init__(self,name,age,dob):
        self.name=name
        self.age=age
        self.dob=dob

    def display(self):
        return f"{self.name} {self.age} {self.dob}"

class department(employee):
    def __init__(self,name,age,dob,department):
        super().__init__(name,age,dob)
        self.department=department
    
    def displaydep(self):
        return f"{self.name} works in {self.department} department"

emp1=department("Hemanth","20","10-11-2003","software")
print(emp1.displaydep())


class car:
    total_cars=0

    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        car.total_cars+=1

    def displayinfo(self):
        return f"brand:{self.brand} model:{self.model} and year:{self.year}"

    @classmethod
    def displaytotal(cls):
        return f"Total cars is: {cls.total_cars} "     

    @staticmethod
    def vintagecar(year):
        if year<2000:
            return "vintage"
    

car1=car("BMW","z1",2003)
car2=car("mini","old",1999)
car3=car("tata","old",1998)

print(car1.displayinfo())
print(car2.displayinfo())
# class method
print(car.displaytotal())
# static method
print(car.vintagecar(car3.year))
