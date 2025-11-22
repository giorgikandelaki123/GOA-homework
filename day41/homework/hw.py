# # 1
# # append() - სიაში ამატებს ახალ ელემენტს ბოლოში.
# # insert() - სიაში ამატებს ელემენტს გარკვეულ ინდექსზე (ნომერზე).
# # pop() - შლის სიიდან ელემენტს: თუ ინდექსს არ მივუთითებთ, შლის ბოლო ელემენტს; თუ მივუთითებთ ინდექსს, შლის მითითებულ ინდექსზე არსებულ ელემენტს.
# # remove() - სიიდან შლის პირველივე ელემენტს, რომელიც ტოლია გადაცემული მნიშვნელობის.

# # 2
# numbers = [1, 2, 3, 4, 5]
# numbers.append(10)
# print(numbers)

# # 3
# names = ["goga", "saba", "luka"]
# names.append("შენი სახელი")
# print(names)

# # 4
# names = ["ani", "nino", "dato"]
# new_name = input("შეიყვანე სახელი: ")
# names.append(new_name)
# print(names)

# # 5
# names = ["goga", "saba", "luka", "nino", "dato"]
# names.insert(3, "შენი სახელი")
# print(names)

# # 6
# my_list = ["a", "b", "c", "d", "e", "f"]
# user_name = input("შეიყვანე სახელი: ")
# user_index = int(input("შეიყვანე რიცხვი (0–6): "))
# my_list.insert(user_index, user_name)
# print(my_list)

# # 7
# fruits = ["apple", "banana"]
# fruits.insert(1, "orange")
# print(fruits)

# # 8
# names = ["goga", "saba", "luka"]
# names.insert(2, "irakli")
# print(names)

# # 9
# foods = ["bread", "milk", "cheese"]
# foods.insert(0, "water")
# print(foods)

# 10
numbers = [5, 10, 15]
numbers.pop()
print(numbers)

# # 11
# fruits = ["apple", "banana", "orange"]
# fruits.pop(1)
# print(fruits)

# # 12
# names = ["goga", "saba", "luka"]
# names.pop(1)
# print(names)

# # 13
# colors = ["red", "green", "blue", "yellow", "black", "purple"]
# colors.pop(0)  
# colors.pop(3)   
# print(colors)

# # 14
# tems = ["pen", "pencil", "book", "eraser"]
# index_num = int(input("შეიყვანე რიცხვი 0-დან 3-მდე: "))
# tems.pop(index_num)
# print(tems)

# # 15
# fruits = ["apple", "banana", "orange"]
# fruits.remove("banana")
# print(fruits)

# # 16
# nums = [3, 5, 3, 7]
# nums.remove(3)
# print(nums)

# # 17
# colors = ["red", "blue", "green"]
# colors.remove("blue")
# print(colors)

# # 18
# names = ["goga", "saba", "luka"]
# user_name = input("აირჩიე სახელი (goga, saba, luka): ")
# names.remove(user_name)
# print(names)

# # 19
# items = ["pen", "pencil", "book", "pencil"]
# items.remove("pencil")
# print(items)

# # 20 
# "შევასრულე სოლოლეარნი"