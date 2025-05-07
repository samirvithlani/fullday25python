numbers = [100,20,34,55,31,78,87,65,66,90,91]
evnList =[]
oddList =[]

for i in numbers:
    if i %2 ==0:
        evnList.append(i)
    else:
        oddList.append(i)


for i in range(0,len(evnList)):
    print(evnList[i])            
    
    

