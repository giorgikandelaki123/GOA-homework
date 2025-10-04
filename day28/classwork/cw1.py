#1
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
last_5 = my_list[5:10]
print("ბოლო 5 ელემენტი:", last_5)


#2
my_list = list((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21))  
first_11 = my_list[0:11]
print("პირველი 11 ელემენტი:", first_11)


#3
my_list = list((1,2,3,4,5,6,7,8,9,10,11,12,13)) 
user_input = int(input("შეიყვანეთ რიცხვი (2-ზე მეტი და 12-ზე ნაკლები): "))
subset = my_list[2:user_input]
print("ელემენტები 2-დან", user_input, "-მდე:", subset)