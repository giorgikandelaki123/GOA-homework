#1
number = float(input("შეიყვანეთ რიცხვი: "))
if number > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif number < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")


#2
age = int(input("შეიყვანე შენი ასაკი: "))
if age < 0:
    print("არასწორი ინფო")  #თუ შემოყვანილი ასაკი უარყოფითია --> 'არასწორი ინფო ხარ' 
elif age <= 12:
     print("ბავშვი ხარ") #0–12 წლის ასაკი --> 'ბავშვი ხარ'
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")  #13-19 წლის ასაკი --> 'მოზარდი/თინეიჯერი ხარ'
elif age <= 64:
    print("ზრდასრული ხართ")  #20-64 წლის ასაკი --> 'ზრდასრული ხართ'
elif age <= 120:
    print("ხანში შესული ხართ")   #65-120 წლის ასაკი --> 'ხანში შესული ხართ'
else:
    print("გურუ ან ჯადოქარი")   #120 ზემოთ --> 'გურუ ან ჯადოქარი ხართ'


#3
password = "goa"
print ("გამოიცანი ჩემი პაროლი")
cda=0

while True:
    password = input()
    cda=cda+1
    if password=="goa":
       if cda>1:
          print("სწორია, თქვენ გამოიცანით პაროლი", cda, "-ე ცდაზე")
       elif cda==1:
        print("თქვენ გამოიცანით პაროლი პირველივე ცდაზე")  
      
    elif password=="nah strong password":
     break
#4
a=int(input("ჩაწერე მთელი რიცხვი"))
b=int(input("ჩაწერე მთელი რიცხვი"))
c=float(input("ჩაწერე ათწილადი რიცხვი"))
print(max(a, b, c))
print(min(a, b, c))
#საშუალო არითმეტიკული ვერ გავაკეთე თუ შეგიძლიათ გვასწავლოთ😁

#5
day = int(input("შეიყვანეთ რიცხვი 1-დან 7-მდე: "))
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
    print("არ ვიცი ეგ რა დღეა")
