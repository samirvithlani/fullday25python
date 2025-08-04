
#10,20,30
#10+20 + 30 - 60
#(10+20)=30 +30 =60

#10,20 =200

#10*20*3 600
#200
class User:
    
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        #self.x + u2.x = User + u3
        return User(self.x + other.x)

    def __str__(self):
        return f"{self.x}"
u1 = User(100)    
u2 = User(200)    
u3 = User(300)    
u4 = User(400)    

ans = u1+u2+u3+u4
print(ans)

        