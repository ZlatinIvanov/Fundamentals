countries = input().split(", ")
capitals = input().split(", ")

pairs = {countries[inx]: capitals[inx] for inx in range(len(countries))}

for country, capital in pairs.items():
    print(f"{country} -> {capital}")

# my_dict = dict(zip(countries,capitals))
# print(my_dict)