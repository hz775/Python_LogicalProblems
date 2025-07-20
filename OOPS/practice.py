class student:
    def __init__(self,name,std,mark):
        self.name=name
        self.std=std
        self.mark=mark
    def average(self):
        if self.mark>35 and self.mark<=100:
            return  sum(self.mark)/len(self.mark)
        else:
            return f"fail"

stude1=student("Hemanth",10,[90,67,88,40,80])
print(stude1.average())