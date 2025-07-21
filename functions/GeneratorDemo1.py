# def getData():
#     return 1
#     return 2

# x  = getData()
# print(x)

def getData():
    print("get Data called........")
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    

# x = getData()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for x in getData():
    print(x)
    


def getStudents():
    yield [f"student {i}" for i in range(1,11)]
    yield [f"student {i}" for i in range(11,21)]    
    yield [f"student {i}" for i in range(21,31)]


for i in getStudents():
    print(i)    
    
    
def getStudents(total,batch):    
    for i in range(0,total,batch):
        yield [f"student {j}" for j in range(i+1,i+batch+1)]

for i in getStudents(100,10):
    print(i)        