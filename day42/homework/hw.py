# 1
fruits = ["apple", "banana", "orange"]
fruits.extend(["kiwi", "mango"])
print(fruits)

# 2
numbers = [10, 20, 30]
numbers.extend([40, 50])
print(numbers)

# 3
names = ["saba", "nino", "luka"]
names.reverse()
print(names)

# 4
nums = [1, 5, 3, 5, 5, 2]
print(nums.count(5))

# 5
letters = ["a", "b", "a", "c"]
print(letters.count("a"))

# 6
name = ["luka", "nino", "goga", "gio"]
print(name.index("goga"))

# 7
colors = ["red", "green", "blue"]
print(colors.index("blue"))

# 8
num = [1, 2, 3]
num.extend([7, 8, 9])
print(num)

# 9
foods = ["pizza", "burger", "pasta"]
foods.reverse()
print(foods)

# 10
cities = ["batumi", "kutaisi", "tbilisi", "rustavi"]
print(cities.index("tbilisi"))

# 11
animals = ["cat", "dog", "cat", "cow"]
print(animals.count("cat"))

# 12
fruit = ["apple", "banana"]
fruit.append("grape")
print(fruit)

# 13
number = [1, 2, 3]
number.extend([4, 5])
print(number)

# 14
saxeli = ["jima", "merabiko"]
saxeli.insert(1, "luka")
print(saxeli)

# 15
items = ["pen", "pencil", "eraser"]
items.pop()
print(items)

# 16
color = ["red", "green", "blue"]
color.remove("green")
print(color)

# 17
ragaca = ["bread", "milk"]
if len(ragaca) == 2:
    ragaca.append("cheese")
else:
    ragaca.append("meat")
print(ragaca)

# 18
numes = [10, 20, 30]
gio = int(input("Enter number: "))
if gio in numes:
    print("Already in list")
else:
    numes.append(40)
    print(numes)

# 19 
"es ver mivxvdi"

# 20
values = ["giorgi", "saba", "irakli", "ina"]
index = int(input("Enter index: "))

if 0 <= 10 < 4:
    values.pop(index)
else:
    print("Index out of range")

print(values)

# 21
pets = ["cat", "dog", "hamster"]
pet = input("Enter pet name: ")

if pet in pets:
    pets.remove(pet)
    print("Removed")
else:
    print("Not found")

print(pets)

# 22
a = [5, 5, 7]
numees = int(input("Enter number: "))

if num in a:
    print(a.count(numees))
else:
    a.append(numees)
    print(a)

# 23    
queue = ["first", "second"]
new_item = input("Enter new item: ")

queue.insert(0, new_item)
if len(queue) > 5:
    queue.pop()
    print(queue)
else:
    queue.reverse()
    print(queue)

# 24 
cifri = [2, 4, 6]
n = int(input("Enter number: "))

if n > 0:
    cifri.append(n)
else:
    print("Only positive allowed")

print(cifri)

# 25
mixed = ["x", "y", "z"]
mixed.extend([1, 2, 3])

letter = input("Enter a letter: ")

if letter in mixed:
    mixed.remove(letter)
    print("Removed")

print(mixed)
