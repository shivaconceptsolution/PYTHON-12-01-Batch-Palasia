x = [2,11,56,67,18,91,12]
for i in range(0,len(x)):
    count=0
    for j in range(1,x[i]+1):
        if x[i]%j==0:
            count=count+1
    if count==2:
        print(x[i])
