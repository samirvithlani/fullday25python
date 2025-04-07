#string iterable subscript
data = "royal Technosoft" #index
# print(data[0]) # 0
# print(data[1]) # 1

#len -->global function
l = len(data)
print("len of string",l)

# for i in range(0,len(data)):
#     print(data[i]) # 0 1 2 3 4


data[0] = "R"

for i in data:
    print(i,end=" ") 