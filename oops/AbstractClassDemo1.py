from abc import ABC,abstractmethod

class Bank(ABC):
    
    @abstractmethod
    def deposit(self):
        pass
    
    @staticmethod
    def check_bal():
        print("check balancew...")    
    
class ICICI(Bank):
    
    def deposit(self):
        print("deposit of icici/..")        
         
        

#b = Bank()     #can not create...
i = ICICI()
#i.check_bal()
Bank.check_bal()