class Ope:
    def __init__(self,num):
        self.num=num

    def __truediv__(self,other):
        self.num=self.num*other.num
        return Ope(self.num)

    def __str__(self):
        return "result is "+str(self.num)


obj = Ope(10)    
obj1 = Ope(20)
obj2 = obj/obj1
print(obj2)


