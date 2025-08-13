def compose(*functions):
    print(functions)
    #cleaneData,convert...
    def compose_functions(x): #x = hi this is india
        #f = cleanData
        for f in functions:
            x = f(x) #cleanData(x),convertLower(text)
        return x #x
    
    return compose_functions        


def cleaneData(text):
    print("cleaninng data...",text)
    return text.strip()

def convertLower(text):
    print("conver lowe called")
    return text.lower()

result = compose(cleaneData,convertLower)    
ans = result("  Hi This iS india  ")
print(ans)