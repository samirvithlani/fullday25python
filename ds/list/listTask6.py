# x =[i**2 for i in range(1,6)]
# print(x)


names = ["okkk","Raj","amitthakkar","parth","ok"]
names.sort(key=len,reverse=True)
print(names)
print("longestName = ",names[0])


names = ["okkk","raj patel","amitt hakkar","parth","ok"]

count=0
for i in names:
    if " " in i:
        count+=1

print(count)        






