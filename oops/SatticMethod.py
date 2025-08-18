class Bank:
    
    def deposit(self):
        print("deposit method called...")
    
    @staticmethod
    def check_balance():
        print("check balance method called..")
    #Integer.parseInt() #static method...
    #Integer i = new....
    #i.pareseInt()



b =Bank()       
b.deposit()
#b.check_balance()
Bank.check_balance()