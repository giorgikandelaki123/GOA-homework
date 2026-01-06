# 1
sityvebi = ["python", "Java", "hello", "World", "apple", "Gamer", "computer"]
i = 0

while i < len(sityvebi):
    exlandeli_sityva = sityvebi[i]
    
    if exlandeli_sityva == exlandeli_sityva.lower():
        sityvebi[i] = exlandeli_sityva.upper() 
        i += 1
    else:
        sityvebi.pop(i)
        

print(sityvebi)

# 2
sityva = "cuRcxElA"
geniosi = []

i = 0
while i < len(sityva):
    if sityva[i] == sityva[i].upper():
        geniosi.append(sityva[i].lower())
    else:
        geniosi.append(sityva[i].upper())
    i += 1

print(geniosi)


# 3
saxelebi = ["giorgi", "ANA", "luka", "NINO", "elene", "DAVID"]
saxelebi_1 = []

for x in saxelebi:
    if x == x.lower():
        saxelebi_1.insert(0, x.upper())
    elif x == x.upper():
        saxelebi_1.append(x.lower())

print(saxelebi_1)

# 4
cities = ["tbilisi", "BATUMI", "kutaisi", "TELAVI", "rustavi", "GORI"]
y = 0  

while y < len(cities):
    if cities[y] == cities[y].upper():
        cities.pop(y) 
    else:
        cities[y] = cities[y].upper() 
        y += 1

print(cities)

# 5
# arvcii

# 6
# arvicii

# 7
# arvicii

# 8
original = "python"
reverse = ""

for z in original:
    reverse = z + reverse
result = reverse.upper()

print(result)

# 9
"გადავხედე"