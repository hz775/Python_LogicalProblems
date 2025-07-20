class company:
    def __init__(self):
        self.__companyName="Google"
    
    def companyName(self):
        print(self.__companyName)

c1=company()
c1.companyName()
print(c1._company__companyName)   #but not recommended

# __ is the private keyword we can acess within that class we cant aceess outside 
# _ is the protected keyword we can acess through child class also which is inherited by parent class



class company:
    def __init__(self):
        self._companyName="Google"
    
    def companyName(self):
        print(self._companyName)

class company1(company):
    def companyName(self):
        return super().companyName()

c1=company1()
print(c1._companyName)
c1.companyName()

