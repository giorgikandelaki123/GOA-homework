#1
list = [1, 2, 3, 4, 5, 6]
list[2:4] = [10, 20, 30]
print(list)

#2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits[0:2] = ["pear", "plum"]
print(fruits)

#3
letters = ["a", "b", "c", "d", "e", "f"]
letters[3:6] = ["x", "y", "z"]
print(letters)


#4
colors = ["red", "green", "blue", "yellow", "black", "white"]
colors[2:6] = ["purple", "orange"]
print(colors)


#5
just_name = ["გიორგი" , "ირმა" , "საბა" ]
print(just_name)
print("ზემოთ მოცემული სია სეიცვალა ამ ქვემოთ  მოცემულ სიით:")
just_name = ["red", "green", "blue", "yellow", "black", "white"]
print(just_name)

#6
num = int(input("enter number"))
if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")

#7
numbers = [4, 7, 12, 9, 15]
num = numbers[3]
if num % 2 == 0:
    print("EVEN number")    
else:
    print("ODD number")

#8
x = [10,25,48,67,52]
last_y = x[-1]
if last_y % 2 == 0 and last_y > 50:
    print("ეს რიცხვი არის ლუწი და მეტი 50 ზე")
elif last_y % 2 != 0 and last_y < 50:
    print("ეს რიცხვი არის კენტი და ნაკლები 50 ზე")


#9
nums = [12,45,78,99,150,200,7,34]
if nums[5] % 2 == 0 or nums[5] > 100:
    print("even or more than 100")
if nums[5] % 2 != 0 or nums[3] < 100:
    print("oddmor less than 100")

#10
str1 = "hello"
str2 = "world"
if str1 != str2:
    print("strings are not equal")
else:
    print("strings are equal")    