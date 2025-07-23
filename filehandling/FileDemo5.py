
count =0
file = open("marksheet.txt","r")
for i in file:
    count+=1
    print(i,end="")


print(count)    