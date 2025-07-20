class person:
    def __init__(self,name,age,DOB):
        self.name=name
        self.age=age
        self.DOB=DOB
    
    def display(self):
        print(f'Name:{self.name},age:{self.age},dob:{self.DOB}')

person1=person("Hemanth",22,"18/10/2003")
person2=person("subash",22,"28/5/2003")
person1.display()
person2.display()