users = ["hr","bob","amit","krishnaswami","kunal","parvati"]

users.sort(key=len,reverse=True)
print(users)

#2 list --> ["a","c"] ["a","b"] -->["a"]

list1 = ["A","B","C","x"]
list2 = ["B","C"]
list3 = []

for i in list1:
    if i in list2:
        list3.append(i)

print(list3)        
        