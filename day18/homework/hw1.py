#1
first=int(input("შემოიყვანე რიცხვი"))
second=int(input("შემოიყვანე რიცხვი"))

if first > second:
    print("first is more than second")
elif first < second:
    print("first is less than second")
else:
    print("first number equal to second number")


#2
name = "გიორგი"
მომხმარებლის_სახელი = input("გთხოვ შეიყვანე შენი სახელი: ")
if მომხმარებლის_სახელი == name:
    print("სეხნიები ვართ")
else:
    print("სხვადასხვა სახელები გვაქვს")


#3
პირველი = int(input("შეიყვანე პირველი რიცხვი:"))
მეორე = int(input("შეიყვანე მეორე რიცხვი: "))
if პირველი > 0 and მეორე > 0:
    print("ორივე რიცხვი დადებითია")
elif პირველი < 0 and მეორე < 0:
    print("ორივე რიცხვი არის უარყოფითი")
else:
    print("ეს რა ჯანდაბაა")


#4
x=50
while x<100:
    print(x)
    x=x+2

#5
i=20
while i < 40:
    print(i)
    i=i+1


#6
"გავაკეთე"