class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
        mark1=self.m1+other.m1
        mark2=self.m2+other.m2
        return(mark1,mark2)

s1=student(40,50)
s2=student(20,70)
s3=s1+s2
print(s3)



class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        return Student(self.m1 + other.m1, self.m2 + other.m2)

    def show(self):
        print(f"Marks: {self.m1}, {self.m2}")

s1 = Student(30, 40)
s2 = Student(20, 10)
s3 = s1 + s2


s3.show()   

