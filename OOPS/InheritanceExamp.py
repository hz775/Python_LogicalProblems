class A:
    def work1(self):
        print("Work 1 is assigned")
    
    def work2(self):
        print("Work 2 is assigned")

class B(A):
    def work3(self):
        print("Work 3 is assigned")
    
    def work4(self):
        print("Work 4 is assigned")

W1=A()
W1.work1()
W1.work2()
W2=B()
W2.work1()
W2.work2()
W2.work3()
W2.work4()


#multiple inheritance
# A child class inherits from more than one parent class.

class A:
    def work1(self):
        print("Work 1 is assigned")
    
    def work2(self):
        print("Work 2 is assigned")

class B:
    def work3(self):
        print("Work 3 is assigned")
    
    def work4(self):
        print("Work 4 is assigned")

class C(A,B):   
    def work5(self):
        print("Work 5 is assigned")
    
    def work6(self):
        print("Work 6 is assigned")

obj=C()
obj.work1()
obj.work2()
obj.work3()
obj.work4()
obj.work5()
obj.work6()

# Multilevel Inheritance
# A child class inherits from a parent, and another class inherits from that child.

class A:
    def work1(self):
        print("Work 1 is assigned")
    
    def work2(self):
        print("Work 2 is assigned")

class B(A):
    def work3(self):
        print("Work 3 is assigned")
    
    def work4(self):
        print("Work 4 is assigned") 

class C(B):   
    def work5(self):
        print("Work 5 is assigned")
    
    def work6(self):
        print("Work 6 is assigned")

obj=B()
obj.work1()
obj.work2()
obj.work3()
obj.work4()
obje=C()
obje.work1()
obje.work2()
obje.work3()
obje.work4()
obje.work5()
obje.work6()

# Hierarchical Inheritance
# Multiple child classes inherit from a single parent class.


class A:
    def work1(self):
        print("Work 1 is assigned")
    
    def work2(self):
        print("Work 2 is assigned")

class B:
    def work3(self):
        print("Work 3 is assigned")
    
    def work4(self):
        print("Work 4 is assigned")

class C(A):   
    def work5(self):
        print("Work 5 is assigned")
    
    def work6(self):
        print("Work 6 is assigned")

obj=C()
obj.work1()
obj.work2()
obj.work5()
obj.work6()





