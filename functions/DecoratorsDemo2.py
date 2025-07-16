
def order_food(func):
    
    def inner(noofpers):
        if noofpers >100:
            print("ordering vadapav... for",noofpers)
        #func(100)
            func(noofpers)
        elif noofpers ==0:
            print("no party..")    
        else:
            print("ordering pizza fo ",noofpers)    
            func(noofpers)
    
    return inner    




@order_food
def throw_party(per):
    print("throwing party for ",per)

throw_party(0)    