#1
number = float(input("შეიყვანეთ რიცხვი: "))
if number > 0:
    print("დადებითი")
elif number < 0:
    print("უარყოფითი")
else:
    print("ნულია")


#2
day = int(input("შეიყვანეთ რიცხვი (1-7): "))
if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არასწორი რიცხვი")


#3
hour = int(input("შეიყვანეთ საათი (0-23): "))
if hour < 12:
    print("დილა")
elif hour == 12:
    print("შუადღე")
else:
    print("საღამო")



#4 
score = int(input("შეიყვანეთ ქულა (0-100): "))
if score >= 90:
    print("A")
elif score == 80:
    print("B")
elif score == 70:
    print("C")
elif score == 60:
    print("D")
else:
    print("F")


#5
password = input("შეიყვანეთ პაროლი: ")
if password == "12345":
    print("შესვლა წარმატებულია")
else:
    print("არასწორი პაროლი")


#6
speed = float(input("შეიყვანეთ სიჩქარე: "))
if speed <= 60:
    print("ნორმალური სიჩქარე")
elif speed <= 120:
    print("გადაჭარბებული სიჩქარე")
else:
    print("საშიში სიჩქარე")


#7
temperature = float(input("შეიყვანეთ ტემპერატურა: "))
if temperature < 0:
    print("ყინვაა")
elif 0 <= temperature < 15:
    print("ცივა")
elif 15 <= temperature < 25:
    print("თბილია")
else:
    print("ცხელა")


#8
score1 = int(input("შეიყვანეთ პირველი ქულა: "))
score2 = int(input("შეიყვანეთ მეორე ქულა: "))
if score1 >= 50 and score2 >= 50:
    print("ჩააბარა")
elif score1 >= 50 or score2 >= 50:
    print("მარტო ერთი ჩააბარა")
else:
    print("ჩაჭრილია")


#9
number = int(input("შეიყვანეთ რიცხვი: "))
if 10 < number < 20:
    print("შუალედურია")
elif number < 10:
    print("პატარაა")
else:
    print("დიდია")


#10    
month = int(input("შეიყვანეთ თვე (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("ზამთარი")
elif month == 3 or month == 4 or month == 5:
    print("გაზაფხული")
elif month == 6 or month == 7 or month == 8:
    print("ზაფხული")
elif month == 9 or month == 10 or month == 11:
    print("შემოდგომა")
else:
    print("არასწორი თვე") 
