numbers = [100,200,100,30,40,30,50]
uniqueList =[]

#i =100 i =200
for i in numbers:
    #100 True
    #200
    #100
    if i not in uniqueList:
        uniqueList.append(i) # [100,200]

print(uniqueList)        

