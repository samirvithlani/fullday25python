#parent class can create in child class with same signature called method overriding

#ATM -->
#HDFC -> BANK -->       --->withdrawhdfc
#SBI __ATM___>MACHINE --> withdrawsbi


#jio -->call jio callable  airtal call

class RBI:
    
    def __init__(self):
        pass
    def withdraw(amount):
        print("withdraw method called.. of RBI")

class SBI(RBI):
    
    def __init__(self):
        pass
    
    # def withdraw(amount):
    #     print("withdraw of sbi")        

s = SBI
s.withdraw(10)        