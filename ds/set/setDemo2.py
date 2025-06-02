user1 = {"ram","shyam","amit","sumit","kunal"}
user2 = {"ram","shyam","amit","ajay","seeta"}


#x = user1.union(user2)
#x = user1 | user2
#x = user1.intersection(user2)
#x = user1 & user2
#x = user2.difference(user1)
x = user1 - user2
#x = user1.symmetric_difference(user2)
print(x)


user1.difference_update(user2)
print(user1)