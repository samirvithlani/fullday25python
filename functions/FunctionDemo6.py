#args

# def getData(x):
#     print(f"Received data: {x}")


#args == users == data =
# def getData(*args):
#     print(f"Received data: {args}")
#     print(f"type of args: {type(args)}")

# getData(10,20,30,100,100)    


# def getData(*args,x):
#     print(f"Received data: {args}")
#     print(f"type of args: {type(args)}")
#     print(f"x: {x}")

# getData(10,20,30,100,100)    

# def getData(x,*args):
#     print(f"Received data: {args}")
#     print(f"type of args: {type(args)}")
#     print(f"x: {x}")

# getData(10,20,30,100,100)    

def getData(*args,x):
    print(f"Received data: {args}")
    print(f"type of args: {type(args)}")
    print(f"x: {x}")

getData(10,20,30,100,100,x=1000)   
# getData(10,20,30,100,100,x=1000,90)    #error