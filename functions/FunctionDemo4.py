def findMaxWord(data):
    names = list(data.values())
    max = names[0]
    for i in names:
        if len(i)>len(max):
            max = i
    
    return max        


ans = findMaxWord({1:"amit",2:"raj",3:"ajay",4:"parth"})
print(ans)