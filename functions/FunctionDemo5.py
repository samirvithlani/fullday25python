#default arg

def add(a=0,b=0,c=0):
    return a + b + c


print(add())  # No arguments, all default to 0
print(add(100))
print(add(20,20))
print(add(50,50,50))    