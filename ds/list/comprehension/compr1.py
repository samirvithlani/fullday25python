'''
data=[]
    for i in range(1,10)
        data.append(i)

'''

data = [i for i in range(1,10)]
print(data)

users = ["ram","shyam","ramesh","rahul","raj"]
rusers =[i for i in users if i.startswith("r")]

# for i in users:
#     if i.startswith("r"):
#         rusers.append(i)
print(rusers)        

numbers = [100,23,456,78,90,23,56,78,901,234,567]
evenNumbers = [i for i in numbers if i %2 ==0]
print(evenNumbers)

students = ["","amit","raj","","parth",None]
cleanStu = [i for i in students if i]
print(cleanStu)

x = ["hi","hello","ok","java"]
data = [len(i) for i in x]
print(data)

name = "1amit234"
#[1,2,3,4]

numbers = [i for i in name if i.isdigit()]
print(numbers)


    
