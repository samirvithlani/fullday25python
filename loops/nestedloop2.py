'''

*
* * 
* * *
* * * * 
* * * * *
'''

#i=1,i=2,i=3,i=4
for i in range(1,6):
    #1 ->2
    #1 3
    #* * *
    for j in range(1,i+1):
        print("*",end=" ") #* 
                           #* *
    print()