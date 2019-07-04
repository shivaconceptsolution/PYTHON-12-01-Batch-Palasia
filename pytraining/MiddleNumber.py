num1 = int(input("Enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

if num1>num2 and num1<num3 or num1<num2 and num1>num3:
    print("num1 is middle number")
elif num2<num3:
    print("num2 is middle number")
else:
    print("num3 is middle number")
