class Bank:
    
    #const is used to initilize instance variable of class
    
    def __init__(self): #x001
        print("default const called...")
        self.name = "raj" #instance variable...
    
    def getData(self): #x001
        print(f"name = {self.name}")
            


raj = Bank()     #x001
raj.getData()
parth = Bank()
parth.getData()
