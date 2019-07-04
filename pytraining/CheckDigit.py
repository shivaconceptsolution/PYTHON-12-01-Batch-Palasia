num = int(input("Enter number to check two digit or above"))
if(num>=0 and num<10):
    print("ONE Digit Number")
elif(num<100):
    print("Two Digit Number")
elif(num<1000):
    print("Three Digit Number")
else:
    print("Above Three Digit Number")
