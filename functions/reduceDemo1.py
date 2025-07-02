import functools

marks = [1,2,3,4,5]

#x y
#1 2
#3 3
#6 4
#10 5
x = functools.reduce(lambda x,y:x+y,marks)
print(x)