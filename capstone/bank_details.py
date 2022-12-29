class bank():

    def __init__(self,avai_balance,name):
        self.avai_balance=avai_balance
        self.name=name
    def details_of_customer(self):
        print("Hi {}, your available balance is {}".format(self.name,self.avai_balance))

    def withdraw(self,amount):
        if amount >self.avai_balance:
            try:
                0/0
            except:
                print("not available balance")
        else:
            self.avai_balance-=amount
            print("you have withdrawn {}. Procedure completed".format(amount))
    def deposit(self,amount):
        if amount>1000:
            try:
                0/0
            except:
                print("limit exceeded")
        else:
            self.avai_balance+=amount
            print("you have deposited {}".format(amount))
    def balance(self):
        print("available balance is {}".format(self.avai_balance))

obj=bank(200,"yamani")
obj.details_of_customer()
obj.withdraw(100)
obj.deposit(1000)
obj.balance()



