#1
for i in range(1, 51):
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტი")


#2 
for i in range(0, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "იყოფა 3-ზე და 5-ზე")
    elif i % 3 == 0:
        print(i, "იყოფა 3-ზე")
    elif i % 5 == 0:
        print(i, "იყოფა 5-ზე")
    else:
        print(i, "არ იყოფა არცერთზე")


#3 
nn = int(input("ნომერი: "))
luwi = 0
kenti = 0
for i in range(0,1):
    if i % 2 == 0:
        luwi += 1
    else:
        kenti += 1
print("ლუწი:", luwi)
print("კენტი:", kenti)


#4
lst = [10, 25, 33, 47, 80, 99]
for x in lst:
    if x > 50:
        print(x, "მეტი 50-ზე")
    else:
        print(x, "ნაკლები 50-ზე")



#5
total = 0
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
        total += i
print("ლუწი რიცხვების ჯამია:", total)



#6
words = ["apple", "banana", "avocado", "cherry", "apricot"]
for w in words:
    if w.startswith("a"):
        print(w)


#7
for i in range(0, 21):
    if i == 0:
        print(i, "ნულია")
    elif i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")


#8
list = [5, 15, 25, 35, 45, 55]
for x in lst:
    if x % 5 == 0:
        print(x)




#9 
s = "შენი სიტყვა"
for ch in s:
    print(ch)


#10
total = 0
for i in range(1, 11):
    total += i
print("ჯამი არის:", total)