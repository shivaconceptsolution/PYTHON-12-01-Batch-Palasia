class Bank:
    def __init__(self):
        self.bal=500
    def __credit(self,amt):
        self.bal+=amt
    def __debit(self,amt):
        self.bal-=amt

    def __checkbalance(self):
        print("Balance is "+str(self.bal))
    def login(self,pin):
        if(pin=="1234"):
            self.__credit(12000)
            self.__debit(1000)
            self.__checkbalance()
        else:
            print("invalid pin code")

obj = Bank()
obj.login("1234")
