class NumException(RuntimeError):
    def __init__(self, arg):
      self.args = arg
try:
 a=int(input("enter number"))
 if a<0:
    raise NumException("enter positive")
 else:
    print(a)

except NumException:
    print("enter only positive value")


