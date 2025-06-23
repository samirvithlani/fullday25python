def checkInt(*args):
    #return True if all data in args is int or else return False
    flag = True
    for i in args:
        if type(i).__name__ != "int":
            flag = False
            break
    
    return flag    
        


# x =100
# print(type(x))
# print(type(x).__name__)

#x = checkInt(10,20,30,40)
x = checkInt(10,20,30,40,"raj")
print(x)

#args and retun max numner from args
# def findMax(*args):
#     flag=True
#     for i in args:
#         if type(i).__name__ != "int":
#             flag = False
#             break
#     if flag == True:
#         return max(args)        
#     else:
#         return "all data should be int"    


def findMax(*args):
    flag=True
    max1 = args[0] #10
    for i in args:
        if type(i).__name__ != "int":
            flag = False
            break
        
    if flag == True:
        for j in args:
            if j>max1:
                max1 = j
        return max1        
            
    else:
        return "all data should be int"    


x = findMax(10,11,0,12,34)
print(x)
        
            





