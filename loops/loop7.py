#1+2+3 = 6
no=123
sum=0
mul=1
rem=0
#12>0
#1>0
while(no>0):
    #0 = 123 % 10 = 3
    #3 = 12 % 10 = 2
    #2 = 1% 10 =1
    rem = no % 10
    #0 = 0 + 3 = 3
    #3 = 3 + 2 = 5
    #5 = 5 + 1 = 6
    sum = sum + rem
    mul = mul * rem
    
    #123  = 123//10 12
    #12 = 12//10
    #1//10 
    no = no //10


print("sum ",sum)    
print("mul ",mul)

if(sum==mul):
    print("twin no")

else:
    print("not twin,.")
