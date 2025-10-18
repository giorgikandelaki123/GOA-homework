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