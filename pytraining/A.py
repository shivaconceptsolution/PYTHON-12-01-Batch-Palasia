class A:
  def fun2(self):
      a=100  #local instance 
      self.b=200 #global instance
      print(a)
      print(self.b)

ref = A()
ref.fun2()
