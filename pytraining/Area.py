class AreaImpl:
 def Triangle(self,base,height):   #param with return type
    return (base*height)/2

 def Rectangle(self,width,height):  #param without return type
    area = width*height
    print("Area is "+str(area))

 def Circle(self):
    r=float(input("enter radius"))  #default with return type
    area = 3.14*r*r
    return area

 def Square(self):                       #default without return type
     s = float(input("enter size"))
     area = 4*s**2
     print("Area of Square is "+str(area))


obj = AreaImpl()
r=obj.Triangle(100,2)
print(r)

     
