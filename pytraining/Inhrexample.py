class A:
    def fun1(self):
        print("A")

class B:   #B inherited by A class 
    def fun2(self):
        print("B")

class C(A,B):   #C Multiple
    def fun3(self):
        print("C")

class D(C):
    def fun4(self):
      print("D")


obj = B()
#obj.fun1()
obj.fun2()

obj1 = C()
obj1.fun1()
obj1.fun2()
obj1.fun3()
obj2 = D()
obj2.fun1()
obj2.fun2()
obj2.fun3()
obj2.fun4()

        
