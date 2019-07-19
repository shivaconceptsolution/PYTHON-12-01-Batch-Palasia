a=-1
b=1
for i in range(1,9):
    c=a+b
    count=0
    for j in range(1,c+1):
        if c%j==0:
            count=count+1
    if count==2:        
      print(c) 
    a=b 
    b=c
    
