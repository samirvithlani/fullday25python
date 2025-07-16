#decorators will return new function
#decortors will accept another function as arguement : hof


def order_food(func): #3 func == throw_party
    
    def inner(): #6
        print("calling.........",func.__name__)
        print("ordering food..") #7
        func() #8==throw_party()
    
    return inner #4 address
    
        


@order_food #2 5
def throw_party(): #9
    print("throw party") #10


throw_party() #1    