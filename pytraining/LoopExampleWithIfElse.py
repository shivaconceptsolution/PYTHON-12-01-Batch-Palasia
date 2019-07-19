num = int(input("enter mobile number"))
for i in range(1,11):
    a=num%10
    num=num//10
    if a%2!=0:
        print("square is ",a*a)
        print("cube is ",a*a*a)

        
