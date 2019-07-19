class A:
  def fun(self):
      print("Fun")
  def fun1(self):
     print("A")

class B(A):
  def fun1(self):
    print("B")
  def fun(self,a):
    print(a)  


obj = B()
obj.fun1()
obj.fun(10)
