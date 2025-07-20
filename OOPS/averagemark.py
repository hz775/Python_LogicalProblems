class student:
    count=0
    total_cgpa=0
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        student.count+=1
        student.total_cgpa+=cgpa
    
    def get_info(self):
        return f"{self.name} and {self.cgpa}"

    @classmethod
    def getcount(cls):
        return f"{cls.count} of total student"
    
    @classmethod
    def totalcgpa(cls):
        return f"{cls.total_cgpa}"

    @classmethod
    def avg_total(cls):
        if cls.count==0:
            return 0
        else:
            return f"{cls.total_cgpa / cls.count}"
    
std1=student("Hemanth",8.5)
std2=student("surya",9.5)

print(std1.get_info())
print(std2.get_info())
print(student.totalcgpa())
print(student.avg_total())
print(student.getcount())
