def findMax(data):
    max = data[0]
    for i in data:
        if i >max:
            max = i
    
    return max        
    



ans = findMax([1,2,3,4,5])    
print(ans)


def getSquare(data):
    x= [i**2 for i in data]
    return x

ans = getSquare([1,2,3,4,5])
print(ans)