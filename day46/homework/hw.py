# 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in nums[:]:  
    index = nums.index(n)
    if n % 2 == 0 or index % 2 == 1:
        nums.remove(n)

print(nums)


# 2
words = ["apple", "banana", "cherry"]

for w in words[:]:
    words.append(w)

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


# 3
numbers = [10, 15, 20, 25, 30, 35]      
for num in numbers[:]:
    if num % 10 == 0:
        numbers.remove(num)
    else:
        numbers.append(num)
print(numbers)

# 4
words = ["one", "two", "three", "four", "five"]
for i in range(len(words) - 1, -1, -1):
    if len(words[i]) % 2 == 0:
        words.pop(i)
    else:
        words.insert(0, words[i])
print(words)
