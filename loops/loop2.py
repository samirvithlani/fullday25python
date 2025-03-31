sp = int(input("Enter the starting point: "))
ep = int(input("Enter the ending point: "))

for i in range(sp,ep+1):
    if i %2 == 0 :
        print(i,end=" ")