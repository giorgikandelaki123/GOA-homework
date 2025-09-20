#1
# Index არის ელემენტის მდებარეობა სიაში. Python-ში ინდექსი იწყება 0-დან.
# მას ვიყენებთ კონკრეტულ ელემენტზე მისასვლელად.


#2
numbers = [4, 6, 1, 5, 9, 8, 4]
print(numbers[0] + numbers[1])  
print(numbers[1] - numbers[0]) 
print(numbers[3] + numbers[4])
print(numbers[1] + numbers[4] + numbers[3])
print(numbers[6])
print(numbers[1] + numbers[2])
print(numbers[4] + numbers[5] + numbers[1] + numbers[0]) 


#3
names = ["ნიკა", "მარიამი", "თემო", "ანა", "გიორგი", "სალომე", "დავითი", "ეკა", "ლევანი", "ნუცა"]
print(names[5])  
print(names[9])  
print(names[3])  
print(names[7])  
print(names[1])  



#4
cities = ["თბილისი", "ბათუმი", "ქუთაისი", "გორი", "რუსთავი"]


print("For loop:")
for city in cities:
    print(city)

print("while loop")
i = 0
while True:
    if i == 5:
        break
    print(cities[i])
    i=i+1


#5    
my_list = [10, "hello", 25, "apple", 7, True, "old_value"]
my_list[3] = "vashli"   
my_list[6] = "msxali"   
my_list[4] = "atami"    
print(my_list)



#7
animals = ["კატა", "ძაღლი", "თუთიყუში", "ლომი", "ფარშევანგი"]

if animals[3] == "ლომი":
    print("there is lion on index 3")
else:
    print("there is no lion on index 3")



#8
basket = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]
basket[1] = "მსხალი"
print(basket[0])
print(basket[1])
print(basket[2])
print(basket[3])
print(basket[4])


#9
letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]
word_mama = letters[6] + letters[5] + letters[6] + letters[5]
print(word_mama)
word_gola = letters[2] + letters[3] + letters[4] + letters[5]
print(word_gola)  
word_goga = letters[2] + letters[3] + letters[2] + letters[5]
print(word_goga)  



#10
letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]
char_at_4 = letters[4]
if char_at_4 == "ლ":
    print("სწორია! ასო ლ ა")
else:
    print("არასწორია, სცადე თავიდან")
last_char = letters[-1]

if last_char == "ე":
    print("საიდუმლო სიტყვა იწყება სწორად")
else:
    print("საიდუმლო სიტყვა არასწორია")
word = letters[2] + letters[4] + letters[7]  

if word == "გელა":
    print("გაარტყი სახელი!")
else:
    print("შტერი ხარ!დ")


#11
my_list = ["თბილისი", "ბათუმი", "ქუთაისი", "გორი", "რუსთავი"]
index = int(input("შეიყვანეთ ინდექსი (0-4): "))
if index >= 0 and index <= 4:
    print("ელემენტი ინდექსზე", index, "არის:", my_list[index])
else:
    print("შეყვანილი ინდექსი არასწორია")
