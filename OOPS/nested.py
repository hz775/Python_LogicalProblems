class company:
    class Employee:
        def __init__(self,name,position):
            self.name=name
            self.position=position
        
        def display(self):
            return f"{self.name} and {self.position}"
            
    
    def __init__(self,companyname):
        self.companyname=companyname
        self.employee=[]
    
    def add_employee(self,name,position):
        emp=self.Employee(name,position)
        self.employee.append(emp)
        
    def listemployee(self):
        return [employee.display() for employee in self.employee]

company1=company("TCS")
company1.add_employee("Hemanth","Manager")
company1.add_employee("Rohan","HR")
print(company1.listemployee())        