class A:
    
    def __init__(self,a,b):
          self.a=a
          self.b=b
    def logic(self):
         self.c=self.a+self.b
    def display(self):
        print(self.c)
    def __del__(self):
        print("Destructor will be called")

obj = A()
obj.logic()
obj.display()

del obj

