try:
 a=int(input("enter first number"))
 b=int(input("enter second number"))
 c=a/b
 print(c)
except ZeroDivisionError:
 print("Denominator can not be zero")
except ValueError:
 print("Enter Only Numeric Value")
else:
 print("No Error Found")   
finally:
 print("Division Program")    

 
