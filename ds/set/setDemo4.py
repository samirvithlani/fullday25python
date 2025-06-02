data = {"Ahm":{"MG ROAD","vastrapur","SBR"},"mumbai":{"MG ROAD","borivalli","bandra"},"pune":{"MG ROAD","dagdusageb road"}}

cities =set()

for i,j in data.items():
    for city in j: #j == set
        cities.add(city)

print(cities)        

city_names = list(data.keys())
print(city_names)
common_areas = data[city_names[0]].copy()

for name in city_names[1:]:
    common_areas = common_areas.intersection(data[name])

print(common_areas)    