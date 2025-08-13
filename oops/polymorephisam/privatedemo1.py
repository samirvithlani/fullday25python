#access modifiers
class PrivateDemo1:
    def __init__(self):
        self.__private_variable = "This is a private variable"
        self.public_variable = "This is a public variable"
    
    def demo(self):
        print("Accessing private variable from within the class:", self.__private_variable)
    
    def __private_method(self):
        print("This is a private method")    


p = PrivateDemo1()
p.demo()
#Ep.__private_variable        
p.public_variable
p.__private_method()  # This will raise an AttributeError since __private_method is private
    
   
        