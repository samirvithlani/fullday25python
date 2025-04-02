no=1634
rem=0
sum=0
temp =no
temp2=no
digit=0

#find not of digit

while temp2>0:
    temp2 = temp2//10
    digit+=1

print("digit ",digit)    
    

while no>0:
    rem = no%10
    sum = sum + (rem**digit)
    no = no//10


if temp == sum:
    print("arsmstring...")    
else:
    print("not an armstrong")    


    
