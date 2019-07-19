num = int(input("enter mobile no"))  #6612312645
max=0
for i in range(1,11):
    a=num%10
    num=num//10
    if max<a:
        max=a
print("max digit is "+str(max))  

    
