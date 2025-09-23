#1
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[-7] * numbers[-1])
print(numbers[-5])
print(numbers[-3])


#2
fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]
print(fruits[2]) 
print(fruits[3]) 
print(fruits[-4]) 
print(fruits[-3])


#3
"ვერ გავიგე"


#4
my_word=["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
print(my_word[-11] + my_word[-9] + my_word[-7] + my_word[-4] + my_word[-6] + my_word[-1] + my_word[-5])
print(my_word[-3] + my_word[-9] + my_word[-1] + my_word[-8])

#5
animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]

index = int(input("შეიყვანე ინდექსი (0-დან 5-მდე): "))

if 0 <= index <= 5:
    selected = animals[index]
    
    if selected == "cat":
        print("შენ აირჩიე კატა")
    elif selected == "goat":
        print("შენ აირჩიე თხა")
    else:
        print("სხვა ცხოველი აირჩიე")
else:
    print("არასწორი ინდექსი — უნდა იყოს 0-დან 5-მდე")


#6
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Gori", "Zugdidi"]

a = int(input("შეიყვანე პირველი ინდექსი: "))
b = int(input("შეიყვანე მეორე ინდექსი: "))

if a < b:
    print(cities[a], cities[b])
elif a > b:
    print("შეცვალე ინდექსები ადგილებით")
    print(cities[b], cities[a])
else:
    print("ორივე ერთია")
    print(cities[a])


#7
word = input("შეიყვანე სიტყვა: ")

if word[0] == "a" and word[-1] == "z":
    print("იწყება a-თი და მთავრდება z-ით")
elif word[0] == "a":
    print("იწყება a-თი")
elif word[-1] == "z":
    print("მთავრდება z-ით")
else:
    print("არც a-თი იწყება და არც z-ით მთავრდება")


#8    
word = input("შეიყვანე სიტყვა: ")

if word[0] == word[-1]:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")


#9
letters = "agivorsbgitr"

goga = letters[1] + letters[4] + letters[8] + letters[0]
print("goga:", goga)

saba = letters[6] + letters[0] + letters[7] + letters[0]
print("saba:", saba)

bativar = letters[7] + letters[0] + letters[10] + letters[2] + letters[3] + letters[0] + letters[5]
print("bativar:", bativar)


#10
"ვერ გავიგე"
