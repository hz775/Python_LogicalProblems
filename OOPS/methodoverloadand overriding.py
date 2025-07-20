# Method Overloading:in python method overloding is not there because same method and different arguments and 
# if same name it will consider last method and it will overides the beforfe method.

class Test:
    def show(self):
        print("No arguments")
    
    def show(self, name):
        print("Hello", name)

obj = Test()
obj.show("Sai")               #Works: Hello Sai
obj.show()                    #Error: missing 1 required argument


class student:
    def show(self):
        print("Hi i am a student")

class teacher(student):
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Hi i am a teacher",self.name)

t1=teacher("hemanth")
t1.show()







