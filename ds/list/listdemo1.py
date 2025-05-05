data = [] #empty list
print(data)
print(type(data))

users = ["amit","sachin","raj"] #string...
print(users)
print(users[0]) #first element


# for i in range(0,len(users)):
#     print(users[i])


#add element..
users.append("kunal")
users.insert(4,"ajay")

users.extend(["seeta","gita"])
#users.extend("GOA")



print("....",users[4])
for i in users:
    print(i)