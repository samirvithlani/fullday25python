users = ["ram","shyam","amit","sumit","seeta"]

# uppersname = [i.upper() for i in users if i.startswith("s")]
# print(uppersname)

#uppersname = map(lambda x:x.upper(),users)
uppersname = map(lambda x:x.upper(),filter(lambda x:x.startswith("s"),users))
print(list(uppersname))