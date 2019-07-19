num= int(input("enter number"))
i=num
f=1
s=""
while(i>=1):
    f=f*i
    if i>1:
     s=s+ str(i) +"*"
    else:
     s=s+str(i)   
    i=i-1

print(s+"="+str(f))    
    
