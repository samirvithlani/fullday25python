#if in lambda

# x = lambda a,b : a if a<b else b
# print(x(100,20))

# x = lambda no : "even" if no %2==0 else "odd"
# print(x(100))
# print(x(101))

x = lambda no : "pos" if no >0 else("zero" if no == 0 else "neg")
print(x(-100))
print(x(100))
print(x(0))
