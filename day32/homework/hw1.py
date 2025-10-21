#1
for i in range(1, 51):
    if i % 2 == 0:
        print(str(i) + " ლუწია")
    else:
        print(str(i) + " კენტია")


#2 
for i in range(0, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + " იყოფა 3-ზე და 5-ზე")
    elif i % 3 == 0:
        print(str(i) + " იყოფა 3-ზე")
    elif i % 5 == 0:
        print(str(i) + " იყოფა 5-ზე")
    else:
        print(str(i) + " არ იყოფა არცერთზე")


#3 
number = int(input("შეიყვანე რიცხვი: "))
even_count = 0
odd_count = 0
for i in range(0, number + 1):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("ლუწი რიცხვების რაოდენობა: " + str(even_count))
print("კენტი რიცხვების რაოდენობა: " + str(odd_count))



#4
numbers = [10, 25, 33, 47, 80, 99]
for i in range(0, 6):  
    if numbers[i] > 50:
        print(str(numbers[i]) + " მეტი 50-ზე")
    else:
        print(str(numbers[i]) + " ნაკლები 50-ზე")


#5
sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
        sum = sum + i
print("ლუწი რიცხვების ჯამია: " + str(sum))


#6
words = ["apple", "banana", "avocado", "grape", "apricot", "melon"]
for i in range(0, 6):  
    if words[i][0] == "a":
        print(words[i])


#7
for i in range(0, 21):
    if i == 0:
        print(str(i) + " ნულია")
    elif i % 2 == 0:
        print(str(i) + " ლუწია")
    else:
        print(str(i) + " კენტია")


#8
numbers = [5, 15, 25, 35, 45, 55]
for i in range(0, 6):
    if numbers[i] % 5 == 0:
        print(numbers[i])



#9 



#10
total = 0
for i in range(1, 11):
    total = total + i

print("ჯამი არის: " + str(total))