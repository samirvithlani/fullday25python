data = "india is my country"
count=0
for i in data:
    if i == " ":
        count += 1

print("number of spaces in string",count+1)        


name  ="madam"
revName = ""
#for i in range(1,10)
#for i in range(10,0,-1)

#ram 3 -1 2
for i in range(len(name)-1,-1,-1):
    #"" = " "+name[i] ="m"
    #m = "m" + name[i]= "ma"
    #ma = "ma"+name[i]= "mar"
    revName += name[i]

print("reversed name",revName)    


if name == revName:
    print("palindrome")
else:
    print("not palindrome")    


  

