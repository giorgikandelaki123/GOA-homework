name = input("შეიყვანეთ თქვენი სახელი: ")
print(name.upper())


# 2) 
name = input("შეიყვანეთ თქვენი სახელი დიდი ასოებით: ")
print(name.capitalize())


# 3) 
names = input("შეიყვანეთ თქვენი სახელი პატარა ასოებით: ")
print(name.capitalize())


# 4) 
arvici = ["nika", "mari", "saba", "luka"]
for noda in arvici:
    print(noda.upper())


# 5) 
ravici = ["NIKA", "MARI", "SABA", "LUKA"]
for patara in ravici:
    print(patara.lower())


# 6) 
vici = ["nika", "mari", "saba", "luka"]
for n in vici:
    print(n.capitalize())


# 7)
items = ["apple", "banana", "cherry", "orange"]
print("სიის სიგრძეა:", len(items))


# 8) 
name = "ალექსანდრე"
print("ასოების რაოდენობაა:", len(name))


# 9) 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1
print("ლუწი რიცხვების რაოდენობაა:", even_count)


# 10)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_count = 0
for n in numbers:
    if n % 2 != 0:
        odd_count += 1
print("კენტი რიცხვების რაოდენობაა:", odd_count)


# 11) 
start = int(input("შეიყვანეთ start რიცხვი: "))
end = int(input("შეიყვანეთ end რიცხვი: "))
step = int(input("შეიყვანეთ step რიცხვი: "))

for i in range(start, end, step):
    if i % 2 == 0:
        print(i)