data = {"Ahm":{"MG ROAD","vastrapur","SBR"},"mumbai":{"MG ROAD","borivalli","bandra"},"pune":{"MG ROAD","dagdusageb road"}}

cities =set()

for i,j in data.items():
    for city in j: #j == set
        cities.add(city)

print(cities)        