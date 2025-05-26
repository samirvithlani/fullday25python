#dict
#{1:1,2:2,3;3}

# data = {i :i for i in range(1,10)}
# print(data)

# data = {i:i**2 for i in range(1,11)}
# print(data)

# data = {i:chr(i) for i in range(97,123)}
# print(data)

#alpha = ['a','x','p','q','r','S']

# alpha_ascii  = {i : ord(i) for i in alpha}
# print(alpha_ascii)


# names = ["ram","shyam","amit","sumit","kunal patel","ajay jadeja"]
# #{name:len,name:len}

# data = {i:len(i) for i in names}
# print(data)

# names = ["ram","shyam","amit","sumit","kunal patel","ajay jadeja"]
# #{name:len,name:len}

# data = {i:len(i) for i in names if len(i)>5}
# print(data)

# names = ["ram","shyam","amit thakkar","sumit","kunal patel","ajay jadeja"]
# #{name:len,name:len}

# data = {i:len(i) for i in names if " " in i}
# print(data)

names = ["ram","shyam","amit thakkar","sumit","kunal patel","ajay jadeja"]
marks = [10,20,30,40,50,60]
#{name:len,name:len}

data = {names[i]:marks[i] for i in range(0,len(names))}
print(data)

# data = {i for i in zip(names,marks)}
# print(data)

names = ["ram","bob","naman","shah","racecar"]
#{"ram":"no","bob":"yes"}

palindromenames = {i:"yes" if i == i[::-1] else "no" for i in names}
print(palindromenames)
