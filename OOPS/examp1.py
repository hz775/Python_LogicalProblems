# Method Overload:compile time

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    # def sleep(self,sleepinghours):
    #     print("Sleeping Hours",sleepinghours)
    
    # def sleep(self,start,end):
    #     print("Sleeping hours",end-start)


    def sleep(self,sleepinghours,start=None,end=None):
        if start is not None and end is not None:
            print("Sleeping hours",end-start)
        else:
            print("Sleeping Hours",sleepinghours)

person1=Person("Sai",22)
person1.sleep(9)


# Method Overriding:Run Time Polymorphinsm

class Parent:
    def show(self):
        print("I AM A PARENT")

class Child(Parent):
    def show(self):
        print("I AM A CHILD")




obj=None

name=input()
if name=="Parent":
    obj=Parent()
else:
    obj=Child()

obj.show()
