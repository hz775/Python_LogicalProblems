class student:
    school="BDMHSS"

    def __init__(self,name,age,Dob,Std):
        self.name=name
        self.age=age
        self.Dob=Dob
        self.Std=Std
    
    def display(self):
        print(f'name of the student is {self.name} and age is {self.age} and Date of Birth {self.Dob}')

    def standard(self):
        print(f'name:{self.name} and standard:{self.Std}')
    
    @staticmethod
    def info():
        print("This is school management team:")
        
    
    @classmethod
    def displayschl(cls): 
        print(f'School:{cls.school}')
    
    @classmethod
    def getschool(cls):
        return cls.school
    

student1=student("Hemanth",16,"18-10-2003","7th")
student2=student("Rohan",16,"1-1-2003","7th")
student.info()
student1.display()
student2.display()
student1.standard()
student2.standard()
student.displayschl()
print(student.getschool())


