#1
print(3 + 4)   
print(10 + 5)    
print(2 + 6)    

print(7 - 3)
print(15 - 15)   
print(8 - 4)

print(2 * 3)     
print(7 * 5)    
print(6 * 4)

print(6 / 3)     
print(8 / 2)     
print(16 / 4) 

print(7 % 3)     
print(10 % 4)    
print(9 % 5)

print(7 // 2)    
print(10 // 3)   
print(20 // 6)

print(2 ** 2)   
print(3 ** 3)   
print(1 ** 1)

#2
# დამატება (+)
# ორი რიცხვის ერთმანეთზე მიმატება. აბრუნებს მათ ჯამს.

# გამოკლება (-)
# ერთი რიცხვის მეორედან გამოკლება. აბრუნებს განსხვავებას.

# გამრავლება (*)
# ორი რიცხვის გამრავლება. აბრუნებს ნამრავლს.

# ნამდვილი გაყოფა (/)
# ერთი რიცხვის მეორეზე გაყოფა. აბრუნებს წილადს (მოციმალურეს თუ საჭიროა).

# % ნაშთით გაყოფა
# ერთი რიცხვის გაყოფა მეორეზე და აბრუნებს მხოლოდ ნაშთს.

# // იატაკზე გაყოფა
# ერთი რიცხვის გაყოფა მეორეზე და აბრუნებს მხოლოდ მთელ რიცხვს (ნაშთის გარეშე).

# ** ხარისხში აყვანა
# რიცხვის რამდენჯერმე გამრავლება თავის თავზე. ანუ, აყვანა ხარისხში.

#3
print(7 // 2)    
print(10 // 3)   
print(20 // 6)  
print(15 // 4)  
print(9 // 5)    


print(2 ** 3)   
print(5 ** 2)    
print(10 ** 0)   
print(3 ** 4)    
print(6 ** 1)    


print(7 % 2)     
print(10 % 3)    
print(20 % 6)    
print(15 % 4)    
print(9 % 5)     


#4
# 15 / 3 = 5.0
# 20 / 4 = 5.0
# 100 / 20 = 5.0

# 15 // 10 = 1
# 10 // 7 = 1
# 40 // 12 = 3

# 4 * 3 = 12
# 40 * 3 = 120
# 120 * 3 = 360

# 4 ** 3 = 64
# 10 ** 3 = 1000
# 2 ** 6 = 64
# 3 ** 4 = 81

# 10 % 7 = 3
# 3 % 2 = 1
# 50 % 25 = 0
# 14 % 11 = 3
# 110 % 50 = 10


#5
# სიები ინახავენ რამდენიმე მნიშვნელობას ერთ ცვლადში.
# ცვლადი ინახავს მხოლოდ ერთ მნიშვნელობას.
# სიები მორგებულია მრავალი მონაცემის დასამუშავებლად ერთიანად.


#6
my_list = ["apple", "banana", "cherry", "date", "elephant"]
print(my_list)

#7
my_list = [10, 20, 30, 40, 50]
print(my_list)

#8
my_list = [1.5, 2.75, 3.14, 4.0, 5.99]
print(my_list)

#9
my_list = [True, False, True, True, False]
print(my_list)


#10
my_list = ["hello", 123, 3.14, True]
print(my_list)

#11
a = 10
b = 5
print(a // b)  
print(a ** b)
print(a % b)

#12
num = int(input("შეიყვანეთ მთელი რიცხვი: "))

if 30 < num < 100:
    print("between 30 and 100")
elif 100 < num < 200:
    print("between 100 and 200")
else:
    print("other number")

#13
a = "hello"       
b = 42            
c = 3.14         
d = True         
e = [1, 2, 3]     

print(type(a))    
print(type(b))    
print(type(c))    
print(type(d))   
print(type(e))    


#14
number = 50
while number <= 100:
    print(number)
    number=number+5

#15
for number in range(40, 91, 3):
    print(number)

#16
for i in range(15):
    print(str(i)+"giorgi")    

name = 0
while name < 15:
    print("giorgi")
    name=name+1



#17
my_name = "giorgi"
my_surname = "kandelaki"
user_name = input("შეიყვანეთ სახელი: ")
if user_name == my_name:
    user_surname = input("შეიყვანეთ გვარი: ")
    if user_surname == my_surname:
        print("same name and surname")
    else:
        print("same name but different surname")
else:
    print("aqedan moshordi")   

#18
my_password = "12345"
while True:
    user_password = input("შეიყვანე პაროლი: ")
    if user_password == my_password:
        print("გამოიცანი")
        break
    else:
        print("პაროლი არასწორია, სცადე თავიდან")         