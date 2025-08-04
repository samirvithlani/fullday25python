class Demo:
    
    def __init__(self,no1):
        self.no1 = no1
        
    
    
    #self d1
    #other d2
    def __add__(self,other):
        print(self.no1) #100
        print(other.no1) #1000
        return self.no1 + other.no1
    
    
d1 = Demo(100)        
d2 = Demo(1000)

ans = d1 + d2
print(f"ans = {ans}")

        