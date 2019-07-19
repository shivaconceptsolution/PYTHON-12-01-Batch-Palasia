for i in range(1,6):
  data1=65
  for j in range(65,71-i):
      if j%2!=0:
       print(chr(data1),end=" ")
      else:
       print(chr(data1+32),end=" ")
       data1=data1+1
  print()
