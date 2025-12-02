names = ["goga", "irakli", "gio", "nikaaa", "ana", "salome", "dato"]

for i in range(len(names) - 1, -1, -1):   
    if len(names[i]) > 5:
        names.remove(names[i])

print(names)