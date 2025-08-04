class Game:
    
    def __init__(self,name,points):
        self.name = name
        self.points = points
    
    
    #self =yash
    #other = bi..
    def __gt__(self,other):
        #100>110 False
        return self.points > other.points        
    
    def __eq__(self,other):
        return self.points == other.points    


yash = Game("yash",110)    
bijendra = Game("Bijendra",110)

flag = yash>bijendra
print(flag)
if yash>bijendra:
    print("yash point's are more...")
elif yash == bijendra:
    print("both are equal..")
else:
    print("bijendra's points are more..")
