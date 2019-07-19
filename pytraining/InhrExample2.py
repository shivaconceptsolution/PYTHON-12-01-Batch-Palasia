class Admin:
    def fun(self):
        print("Admin")
    def accept(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print("ID is "+str(self.id)+" Name is "+str(self.name))


class Employee:
    def fun(self):
        print("Employee")
    def accept1(self,sal):
        self.sal=sal

    def display1(self):
        print("Salary is "+str(self.sal))

#class OtherStaff(Employee):
class OtherStaff(Employee,Admin):       
    def accept2(self,bonus):
        self.bonus=bonus
    def display2(self):
        print("Bonus is "+str(self.bonus))



print("Admin Info")
#obj = Employee()
obj=Admin()
obj.accept(1001,"admin")
obj.display()
print("Emp Info")
obj2 = Employee()
#obj2.accept(1002,"Emp")
obj2.accept1(12000)
#obj2.display()
obj2.display1()
print("Other Staff Information")
obj3 = OtherStaff()
obj3.fun()
obj3.accept(1003,"OtherStaff")
obj3.accept1(1200)
obj3.accept2(200)
obj3.display()
obj3.display1()
obj3.display2()

