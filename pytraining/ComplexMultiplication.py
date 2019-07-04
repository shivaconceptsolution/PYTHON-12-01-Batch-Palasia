a = int(input("enter real number"))  #int is used to convert string to integer
b = int(input("enter imaginary number"))
c = int(input("enter real number"))
d = int(input("enter imaginary number"))
r = (a*c-b*d)
i = (a*d+b*c)
print(str(a) + "+" + str(b)+ "i")  #str is used to convert int to string
print(str(c) + "+" + str(d)+"i")
print(str(r) + "+" + str(i)+"i")
