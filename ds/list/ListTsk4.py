numbers = [100,200,100,30,40,30,50,100,20,30,30]
duplicateElm = []
uniqueElm = []

for i in numbers:
    if i not in uniqueElm:
        uniqueElm.append(i)
    else:
        if i not in duplicateElm:
            duplicateElm.append(i)

print(duplicateElm)   
print(len(duplicateElm))     
            

          
