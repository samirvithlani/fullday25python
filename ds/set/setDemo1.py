#data = {} #empty dict
#data  = set() #empty set

data  ={100,20,34,56,99,0,23,23,199,45,67,78,87,77,0}
print(data)

#print(data[0])

# for i in data:
#     print(i)


names  = {"ram","shyam","ram","amit","kunal"}
print(names)

names.add("ajay")
print(names)

#names.update({"seeta","seema"})
#names.update(("seeta","seema"))
#names.update("seeta")
#names.clear() --> empty set

#removedELm = names.pop()
#print("removing...",removedELm)

names.remove("ram")
#names.discard("rama")
print(names)