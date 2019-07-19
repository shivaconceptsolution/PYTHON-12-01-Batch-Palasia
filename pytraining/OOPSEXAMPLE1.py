class Student:
    def accept(self,rno,name):
        self.rno=rno
        self.name=name
    def display(self):
        print("rno is "+str(self.rno)+" name is "+self.name)



o = Student()
o.accept(1001,"STU1")
o.display()
o1 = Student()
o1.accept(1002,"STU2")
o1.display()

o2 = Student()
o2.accept(1003,"STU1")
o2.display()



        
