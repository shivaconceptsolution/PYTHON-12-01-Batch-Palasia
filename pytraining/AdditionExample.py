def Addition():
    a=100
    b=200
    c=a+b
    print(c)
def multiplication():
    a=100
    b=20
    return a*b

def Substraction(a,b):  #called function
    c=a-b
    print(c)

def division(a,b):
    return a/b

    
Addition()              #calling function without param
s=multiplication()
print(s)
Substraction(100,20)   #calling function with param
s= division(10,2)
print(s)

