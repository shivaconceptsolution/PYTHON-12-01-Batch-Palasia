class Ope:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        self.a=int(self.a)*int(other.a)
        return Ope(self.a)
    def __sub__(self,other):
        self.a=int(self.a)//int(other.a)
        return Ope(self.a)


    def __str__(self):
        return "result is "+str(self.a)


obj1 = Ope(100)    
obj2 = Ope(20)
#obj3 = obj1+obj2  #  + will call __add__
#print(obj3) #__str__() will call
obj3 = obj1-obj2  #  + will call __add__
print(obj3) #__str__() will call
