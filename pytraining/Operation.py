class Ope:
    def addition(self):  #default with no return type
        a=100
        b=200
        c=a+b
        print(c)
    def substraction(self):  #default with return type
        a=10
        b=2
        return a-b

    def multi(self,a,b):     #param with return type
        c=a*b
        print(c)
    def division(self,a,b):   #param no return type
        c=a/b
        return c


obj = Ope()
obj.addition()
res=obj.substraction()
print(res)
obj.multi(100,2)
res = obj.division(100,2)
print(res)
