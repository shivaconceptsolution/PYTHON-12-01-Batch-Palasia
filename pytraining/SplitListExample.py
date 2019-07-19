x = [12,23,34,45,56,67,78,89,11,12]
y=[int]*3
z=[int]*3
k=[int]*4
for i in range(0,len(x)):
    if i<3:
        y[i]=x[i]
        print("First List Element is "+str(y[i]))
    elif i<6:
        z[i-3]=x[i]
        print("Second List Element is "+str(z[i-3]))
    else:
       k[i-6]=x[i]
       print("Third List Element is "+str(k[i-6]))
   
