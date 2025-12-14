# 2
names = ["gio", "nino", "luka"]
surnames = ["BERIDZE", "KAPANADZE", "TSERETELI"]

for i in range(len(names)):
    names[i] = names[i].upper()

for i in range(len(surnames)):
    surnames[i] = surnames[i].lower()

result = names + surnames
print(result)

# 3
words = ["Python", "hello", "WORLD", "coding", "TestA"]

for w in words[:]:
    if len(w) < 6 or ('A' <= w[-1] <= 'Z'):
        words.remove(w)

print(words)
