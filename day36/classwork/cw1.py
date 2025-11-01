#1
word = input("შეიყვანეთ სიტყვა ან ტექსტი: ")

if 'a' in word or 'A' in word:
    print("ტექსტში არის 'a' ან 'A'.")
else:
    print("ტექსტში არ არის 'a' და არც 'A'.")
if 'car' not in word:
    print("ტექსტში არ არის სიტყვა 'car'.")
else:
    print("ტექსტში არის სიტყვა 'car'.")



#2
text = input("შეიყვანეთ ტექსტი: ")

for zangi in text:
    if zangi == 'a' or zangi == 'A':
        continue
    print(zangi)