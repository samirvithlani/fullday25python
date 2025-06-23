data = ["amit","raj","parth","ajay","priya","kunal","shyam"]
#{"a":["amit","ajay"]....}
result={}

for name in data: #amit,raj,ajay
    key = name[0] #a,r,a
    if key not in result: #a,r,
        result[key]=[] #{'a':[],'r':[]}
    
    result[key].append(name)   #{a:["amit","ajay"]:r:["raj"]} 

print(result)        