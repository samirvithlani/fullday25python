class Bank:
    
    #const is used to initilize instance variable of class
    bankName = "SBI"
    def __init__(self,name): #x001,x002
        print("param const called...")
        self.name = name #instance variable...
    
    def getData(self): #x001,x002
        print(f"name = {self.name}")
            


raj = Bank("raj")     #x001
raj.getData() #x001
parth = Bank("parth")
parth.getData() #x002
