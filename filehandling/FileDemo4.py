with open("marksheet.txt") as file:
    x = file.readlines()
    print(x)
    for i in x:
        print(i,end="")