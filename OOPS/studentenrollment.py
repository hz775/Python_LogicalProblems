class student:
    all_students=[]
    def __init__(self,name,course):
        self.name=name
        self.couse=course
    
    def __str__(self):
        return f"{self.name} and applied for {self.couse}"
    
    def add_students(self):
        if self.name not in student.all_students:
            student.all_students.append(self.name)
    
    @classmethod
    def show_all(cls):
        print("All students: ",cls.all_students)
    

class courses:
    def __init__(self):
        self.course=[]
        self.total_members=3

    def add_course(self,a):
        if len(self.course)<self.total_members:
            self.course.append(a)
        else:
            print("course is full")
        
    
    def display(self):
        for cour in self.course:
            print(cour)
    
std1=student("Hemanth","python")
std2=student("sai","Python")
cor=courses()
cor.add_course(std1)
cor.add_course(std2)
cor.display()

    

        