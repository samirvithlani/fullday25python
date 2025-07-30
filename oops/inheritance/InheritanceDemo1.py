class Parent:
    
    def test(self):
        print("test function called...")


class Child(Parent):
    
    def demo(self):
        print("child class demo called...")        
        self.test()


c = Child()
c.demo()
c.test()        