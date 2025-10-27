#1
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Telavi", "Gori", "Marneuli"]

for city in cities:
    if len(city) > 6:
        print(city)


#2
words = ["internationalization", "communication", "responsibility", "magnificent", "microelectronics"]

for word in words:
    if len(word) % 15 == 0:
        print(word)


#3
numbers = [3, 7, 12, 45, 89, 23, 56]

count = 0
for num in numbers:
    count += 1

print("სიის სიგრძეა:", count)        


#4
words = ["apple", "peach", "plum", "grape", "melon", "berry"]

for word in words:
    if len(word) == 5:
        print(word)


#5
sentence = input("შეიყვანე წინადადება: ")

symbols = 0
for char in sentence:
    symbols += 1

a_count = 0
for char in sentence:
    if char == "a" or char == "A":
        a_count += 1
print("სიმბოლოების რაოდენობაა:", symbols)
print("'a' ან 'A' სიმბოლოების რაოდენობაა:", a_count)
        


#6
strings = ["dog", "hippopotamus", "cat", "elephant", "giraffe", "turtle"]

longest = ""
for s in strings:
    if len(s) > len(longest):
        longest = s

print("ყველაზე გრძელი სტრინგია:", longest)        