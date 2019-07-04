num = int(input("enter number"))  #78923
a = num%10   #5
num=num//10   #1234
b = num%10   #4
num=num//10 #123
c = num%10 #3
num=num//10 #12
d = num%10  #2
e= num//10  #1  
num1 = e*10000+b*1000+c*100+d*10+a*1
print(num1)
