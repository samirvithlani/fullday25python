data = {}

while True:
    
    char = input("enter char press y for yes and n for no")
    if(char == 'y'):
        name = input("enter name")
        marks = int(input("enter marks"))
        data[name] = marks
    elif char =='n':
        break
    else:
        print("invalid choice")
        break

print(data)    
        