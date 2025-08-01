class Shape:
    
    def area(self,x):    
        print("are function called for square",x)

    def area(self):
        print("area function called.... without param")
        
s = Shape()
s.area(100)        