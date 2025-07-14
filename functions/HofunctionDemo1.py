def toBeCalled():
    print("to be called........!!!")

def getData(a):
    print(a)
    a()

# getData(100)    
# getData("ok")
# getData([])
getData(toBeCalled)