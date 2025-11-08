#1 
word = input("შეიყვანე სიტყვა: ")

for ch in word:
    if ch == 'e' or ch == 'E':
        break
    print(ch, end='')


#2
sentence = input("შეიყვანე წინადადება: ")

if "bad" in sentence:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")


#3 
text = input("შეიყვანე წინადადება: ")

for ch in text:
    if ch == ' ':
        continue
    print(ch, end='')


#4 
text = input("შეიყვანე წინადადება: ")
vowels = 'aeiouAEIOU'

for ch in text:
    if ch in vowels:
        continue
    print(ch, end='')


#5 
start = int(input("შეიყვანე პირველი რიცხვი: "))
end = int(input("შეიყვანე მეორე რიცხვი: "))

for num in range(start, end + 1):
    if num % 15 == 0:
        print("პირველი რიცხვი, რომელიც იყოფა 15-ზე:", num)
        break


#6 
while True:
    text = input("შეიყვანე ტექსტი: ")
    if text == 'python is best':
        break
    print("you should learn python")


#7
start = int(input("შეიყვანე პირველი რიცხვი: "))
end = int(input("შეიყვანე მეორე რიცხვი: "))

count = 0

for num in range(start, end + 1):
    if num % 3 == 0:
        count += 1
        if count == 3:
            print("მესამე რიცხვი, რომელიც იყოფა 3-ზე:", num)
            break
