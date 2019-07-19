x = [2,94,45,56,78,11]
max=x[0]
for i in range(1,len(x)):
    if max<x[i]:
        max=x[i]

print("maximum number is ",max)
