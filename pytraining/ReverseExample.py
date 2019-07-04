num = int(input("enter number to reverse"))  #123
print("Actual number is "+str(num))
a = num%10     #3
num = num//10  #12
b = num%10     #2
c= num//10     #1

num1 = a*100+b*10+c*1
print("After Reverse number is "+str(num1))
