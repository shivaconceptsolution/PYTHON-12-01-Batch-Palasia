class A:
   def functionname(self):
      print("A")

class B:
   def functionname2(self):
     print("B")
class C(A,B):
   def functionname3(self):
     print("c")     


obj = C()
obj.functionname()
obj.functionname2()
obj.functionname3()
