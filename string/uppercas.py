name = input("enter name")
upperName =""
#ABC
for i in name:
    #AbC
    if(ord(i)>=97 and ord(i)<122):
        upperName = upperName + chr(ord(i)-32)
        #"AB"
    else:
        upperName = upperName + chr(ord(i))        
        #"ABC"

print(upperName)    