# 1
names = ["Nika", "gio", "Ana", "luka", "Mariam"]
Upper_name = []

for name in names:
    if name[0] == name[0].upper():
        Upper_name.append(name)

print(Upper_name)

# 2
names = ["nika", "gio", "ana"]
surnames = ["TSERETELI", "BERIDZE", "GELASHVILI"]

for i in range(len(names)):
    names[i] = names[i].upper()

for i in range(len(surnames)):
    surnames[i] = surnames[i].lower()

შეკრიბე = names + surnames
print(შეკრიბე)

# 3
"ვერ გავიგე"

# 4
numbers = [5.5, 12.3, 150.7, 45.0, 99.9, 10.0, 100.0, 75.5, 200.2, 30.1]
new_list = []

for num in numbers:
    if num > 10 and num < 100:
        new_list.append(num)

print(new_list)

# 5
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Gori"]
countries = ["Georgia", "France", "Germany", "Italy", "Spain",
            "Portugal", "Greece", "Turkey", "Armenia", "Azerbaijan"]

i = 0
for city in cities:
    countries.insert(i, city)
    i += 1

print(countries)
