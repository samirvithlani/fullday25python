data = [1,2,3,4,5] #10 10 11 12 13 14 15

# data10 =[i+10 for i in data]
# print(data10)


data10 = map(lambda x: x+10,data) #x = 1,2,3,4,5 -11 12 14 114 15
print(list(data10))

users = ["ram","shyam","amit","sumit","seeta"]

# upperUser = [i.upper() for i in users]
# print(upperUser)

upperUser = map(lambda x:x.upper(),users)
print(list(upperUser))