#importing the abstract base class module
#abstract base class
from abc import ABC, abstractmethod

#asbtract class
class RBI(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def withdraw(self,amoount):
        pass
    
    def otp(self):
        print("OTP method called.. of RBI")

class SBI(RBI):    
    
    def __init__(self):
        super().__init__()
    
    def withdraw(self, amount):
        print("withdraw of SBI with amount:", amount)    

s = SBI()        