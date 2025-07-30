class Bank:
    
    def __init__(self):
        self.reporate = 5
        self.tax=10
        print("parent class const called....")


class SBI(Bank):
    
    def __init__(self):
        super().__init__()
        print("SBI CLASS const called....")        
        
    
    
    
    def getData(self):
        print(f"reporate = {self.reporate}")    
        print(f"tax = {self.tax}")
        


sbi = SBI()       #child const... 
#sbi.getData() sbi.getData(sbi)
sbi.getData()