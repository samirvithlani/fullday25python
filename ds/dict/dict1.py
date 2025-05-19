data = {"a":11,"b":22,"c":33,"d":44}

print(data)

print(data["a"])

x = data.keys()
print(x)
y = data.values()
print(y)
z = data.items()
print(z)

for i,j in data.items():
    print(i,j)