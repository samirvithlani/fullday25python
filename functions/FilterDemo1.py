users = ["ram","shyam","amit","sumit","seeta"]

# sname = [i for i in users if i.startswith("s")]
# print(sname)

sname = filter(lambda x:x.startswith("s"),users)
print(list(sname))

users = ["ram","shyam","amit","sumit",None,"seeta",""]

cleanuser = filter(lambda x:x,users)
print(list(cleanuser))


