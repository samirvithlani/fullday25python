# with open("marksheet.txt","r") as file:
#     x = file.read()
#     print(x)



file  = open("marksheet.txt","r")    
# x = file.readline()
# print(x)
count=0
while True:
    x = file.readline()
    count+=1
    print(x,end="")
    if not x:
        break


print(f"no of lines = {count}")    