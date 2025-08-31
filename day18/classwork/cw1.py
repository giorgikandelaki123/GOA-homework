#1
x=int(input("დაწერე x-ის მნიშვნელობა"))
y=int(input("დაწერე y-ის მნიშვნელობა"))
z=int(input("დაწერე z-ის მნიშვნელობა"))

if x==y==z:
    print("x=y=z")
    
elif x==y:
    print("x=y")

elif x==z:
    print("x=z")

elif y==z:
    print("y=z") 

else: 
    print("არცეთი არ არის ტოლი")               



#2
month=int(input("ჩაწერე 1-დან 12-ჩათვლით"))
if month==12:
    print("ზამთარი")

elif month==1:
    print("ზამთარი")

elif month==2:
    print("ზამთარი")

elif month==3:           
    print("გაზაფხული")

elif month==4:         
    print("გაზაფხული")

elif month==5:           
    print("გაზაფხული")   

elif month==6:
    print("ზაფხული")

elif month==7:           
    print("ზაფხული")      

elif month==8:           
    print("ზაფხული")

elif month==9:           
    print("შემოდგომა")

elif month==10:           
    print("შემოდგომა")    

elif month==11:          
    print("შემოდგომა")    


#3
name = input("შემოიყვანე შენი სახელი: ")

if name == "admin":
    password = input("შემოიყვანე ადმინის პაროლი: ")
    if password == "adminpassword123":
        print("სალამი ადმინ")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")
