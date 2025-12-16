# 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(nums)-1, -1, -1):
    if nums[i] % 2 == 0 or i % 2 == 1:
        nums.remove(nums[i])

print(nums)

# 2
words = ["apple", "banana", "cherry"]

nodo = len(words)
for i in range(nodo):
    words.append(words[i])

print(words)

# 4
words = ["apple", "Banana", "cherry", "Dog", "elephant"]

for i in range(len(words)):
    words[i] = words[i].capitalize()

print(words)

# 5
# append(x) – სიაში ამატებს ელემენტს ბოლოში

# insert(i, x) – ამატებს ელემენტს კონკრეტულ ინდექსზე

# remove(x) – შლის მითითებულ ელემენტს

# pop(1) – შლის ჩვენ მითითებულ რიცხვზე

# len(list) – აბრუნებს სიის სიგრძეს

# count(x) – ითვლის რამდენჯერ გვხვდება ელემენტი

# reverse() – აბრუნებს სიის რიგს

# upper() – ყველა ასოს აქცევს დიდად

# lower() – ყველა ასოს აქცევს პატარად

# capitalize() – მხოლოდ პირველ ასოს ხდის დიდს