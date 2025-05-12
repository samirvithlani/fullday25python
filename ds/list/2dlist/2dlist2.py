sales = [[10,12,23],[11,150,30],[10,22,40]]
totalSales =[]
sum=0
for i in sales:
    for j in i:
        print(j,end=" ")
        sum = sum+j
    totalSales.append(sum)
    print()  
    sum=0  

print(totalSales)  

maxval = max(totalSales)  
print("max day = ",totalSales.index(maxval)+1)



        