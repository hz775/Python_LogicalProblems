# # emp can be any object.
# It doesn’t care whether emp is an employee or an employee1.
# It only expects emp to have an .info() method.
# If it has that method, display() will work. Otherwise, Python throws an error.

# In Python, you don’t need to know which class an object belongs to.
# If it has the method you want to call — you just call it.
# That’s duck typing.

class employee:
    def info(self):
        print("Sai","IT Department","Google")

class employee1:
    def info(self):
        print("Sai","IT Department","Google")
        print("Pranav","Software","TCS")
    def detail(self,name,department):
        print(self.name,self.department)
    
class Department:
    def display(self,emp):            
        emp.info()

e1=employee()
e2=employee1()
d1=Department()
d1.display(e1)




        


