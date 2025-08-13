def compose(*functions):
    
    def handle(x):
        print("handle called...")
        # functions[0](x) #convertData
        # functions[1](x) #printData
        for i in functions:
            x = i(x)
        return x    
        
    return handle

def printData(text):
    #print(text) 
    return text   

def convertUpper(text):
    #print("con...",text)    
    return text.upper()

result = compose(convertUpper,printData)    
#print(result) #result == ()
ans = result("hi") #hanlde
print(ans)