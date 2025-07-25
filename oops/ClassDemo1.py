class Person:
    
    #class level variable....
    
    persx = 1000 #static class name...
     
    #self == this
    def test(self): #self == person object
        print("test function called...")
        print(self)
    
    def getpersondetail(self,name,email):
        #print(f"persx  ===== {Person.persx}")
        print(f"persx == {self.persx}")
        print(f"name = {name} email = {email}")
        


#object..
person = Person()
person.test()   #person.test(person)      
print(person) #hashcode
person.getpersondetail("ram","ram@gmail.com")
print(person.persx)