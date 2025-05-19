data = {"Gujarat":"Gandhinagr","Maharashtra":"Mumbai","Punjab":"Chandigadh","Rajasthan":"Jaipur",
        "Tamilnadu":"Chennai"}


print(data)
data.update({"Bihar":"Patna","Gujarat":"Ahmedabad"})
data["UP"]="Lucknow"
print(data)



#remvedElm = data.pop("Gujarat")
remvedElm = data.popitem()
print("removing...",remvedElm)
print(data)

