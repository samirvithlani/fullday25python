class ParentA:
    
    def __init__(self):
        print("default const of parent A")
        self.amount = 5000
        self.a = 2000
    
    def car(self):
        print("car function called...")    

    def home(self):
        print("home of parent a")

class ParentB:
    def __init__(self):
        print("default const of Parent B")        
        self.amount = 6000
    
    
    def bike(self):
        print("bike function called..")    

    def home(self):
        print("home of parent B")

class Child(ParentB,ParentA):
    
    def __init__(self):
        super().__init__()
        print("child class const called...")
    
    
    def getGift(self):
        print(f"amount = {self.amount}")        
        #print(f"a = {self.a}")
        self.car()
        self.bike()
        self.home()


child = Child() #child const default
child.getGift()            