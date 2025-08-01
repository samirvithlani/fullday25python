from multipledispatch import dispatch

class Shape:

    @dispatch(int)    
    def area(self,x):    
        print("are function called for square",x)

    @dispatch()    
    def area(self):
        print("area function called.... without param")
    
    @dispatch(int,int)        
    def area(self,x,y):
        print("area function called with 2 param int",x,y)
    
    @dispatch(list)
    def area(self,x):
        print("area functio called with list",x)    
        
s = Shape()
s.area([1,2,2,4])        