num = int(input("Enter Five Digit Number To Count Even Odd Digit")) #45672
a = num%10  #2
num=num//10 #4567
b = num%10 #7
num = num//10 #456
c = num%10  #6
num = num//10 #45
d = num%10 #5
e1 = num//10 #4
print(a,b,c,d,e1)
e=0
o=0
if a%2==0: 
  e=e+1
else:
 o=o+1
if b%2==0: 
  e=e+1
else:
 o=o+1

if c%2==0: 
  e=e+1
else:
 o=o+1
if d%2==0: 
  e=e+1
else:
 o=o+1
 
if e1%2==0: 
  e=e+1
else:
 o=o+1
#print(1%2)
print("Total even is ",e ," Odd is ",o)
