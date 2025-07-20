# Method Resolution Order(MRO) left->Right
class A:

    def __init__(self):
        print("Hi i am working for class A")

    def work1(self):
        print("Work 1 is assigned")
    
    def work2(self):
        print("Work 2 is assigned")

class B:

    def __init__(self):
        print("Hi i am working for class B")

    def work3(self):
        print("Work 3 is assigned")
    
    def work4(self):
        print("Work 4 is assigned") 

class C(A,B):

    def __init__(self):
        super().__init__()
        print("Hi i am working for class C")   

    def work5(self):
        print("Work 5 is assigned")
    
    def work6(self):
        print("Work 6 is assigned")

obj=C()

def intersect_ranges(range1, range2):
    a, b = range1
    c, d = range2
    
    x = max(a, c)
    y = min(b, d)
    
    if x <= y:
        return [x, y]
    else:
        return None  
