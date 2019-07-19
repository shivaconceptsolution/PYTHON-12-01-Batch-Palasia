num = int(input("Enter Number To Check Prime"))
i=1
c=0
while i<=num:
    if num%i==0:
      c=c+1
      break
    i=i+1  

if c==0:
    print("prime")
else:
    print("not prime")
