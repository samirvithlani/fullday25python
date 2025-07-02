# def getData(t,**kwargs):
#     x={}
    
#     for i,j in kwargs.items():
#         if type(j).__name__ == t:
#             x[i]=j
#     return x        



# print(getData("int",a=10,b=20,x="ok",d=[1,2]))
# #output {a:10,b:20}


# def calulator(op,*args):
#     sum = 0
#     sub =0
#     match op:
#         case "add":
#             for i in args:
#                 sum  = sum +i
#             return sum
#         case "sub":
#             for i in args:
#                 sub  = sub -i
#             return sub    


# print(calulator("add",1,2,3,4))
# print(calulator("sub",11,22,90,-100))



def add(*args):
    x=[]
    for i in args:
        x = x +i
    return x    
        

print(add([1,2,3],[4,5,6]))
#[1,2,3,4,5,6]


def add(discount,*args):
    discount = discount/100
    print(discount)
    return [i- i*discount for i in args]


print(add(10,100,300,78,89))
#output[90,270] #comprehension...





