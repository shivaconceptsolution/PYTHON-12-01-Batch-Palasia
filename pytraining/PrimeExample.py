c=0
for num in range(2,30):
 count=0
 for i in range(1,num+1):
    if num%i==0:
        count=count+1
        
 if count==2:
    c=c+1 
    print(num,end=" ")
    if c==1 or c==3 or c==6:
     print() 

    
    
