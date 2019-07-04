num1 = int(input("Enter first subject marks"))
num2 = int(input("Enter second subject marks"))
num3 = int(input("Enter third subject marks"))
num4 = int(input("Enter fourth subject marks"))
num5 = int(input("Enter fifth subject marks"))

if((num1>=0 and num1<=100) and (num2>=0 and num2<=100) and (num3>=0 and num3<=100) and (num4>=0 and num4<=100) and (num5>=0 and num5<=100)):
  c=0
  marks=0
  sub=""
  dist1=""
  if num1>=75:
    dist1=dist1+ " PHYSICS "
  if num2>=75:
    dist1=dist1+ " CHEM "
  if num3>=75:
    dist1=dist1+ " MATHS "
  if num4>=75:
    dist1=dist1+ " ENG "
  if num5>=75:
    dist1=dist1+ " HINDI "  
    
  if num1<33:
      marks=num1
      sub=sub+ "PHYSICS" + " "
      c=c+1
  if num2<33:
      marks=num2
      sub=sub+ "CHEM" + " "
      c=c+1
  if num3<33:
      marks=num3
      sub=sub+ "MATHS" + " "
      c=c+1
  if num4<33:
      marks=num4
      sub=sub+ "English " + " "
      c=c+1
  if num5<33:
      marks=num5
      sub=sub+ "HINDI" + " "
      c=c+1

  if c==0 or (c==1 and marks>=28):
     if(marks>=28):
      per= (num1+num2+num3+num4+num5+(33-marks))/5
     else: 
      per= (num1+num2+num3+num4+num5)/5
     if per>33 and per<45:
         print("Third division with "+str(per)+"%")
     elif per<60:
         print("Second Division"+str(per)+"%")
     else:
         print("First Division"+str(per)+"%")
     if dist1!="":
        print("Distinction subject name is "+dist1)
     if sub!="":
         print("You are pass by grace and grace subject name is "+sub+" grace marks is "+str(33-marks))
  elif c==1:
      print("suppl in "+sub)
  else:
      print("fail in "+sub)


else:
    print("all subejct marks should be 0 to 100")
    
