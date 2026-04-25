# 2
names = ["gio", "nino", "luka"]
surnames = ["BERIDZE", "KAPANADZE", "TSERETELI"]

for i in range(len(names)):
    names[i] = names[i].upper()

for i in range(len(surnames)):
    surnames[i] = surnames[i].lower()

result = names + surnames
print(result)


