# 1
რიცხვი = [1, 2, 3, 4, 5]
ახალი_რიცხვი = []
for i in რიცხვი:
    ახალი_რიცხვი.append(i*2)
print(ახალი_რიცხვი)


# 2
სახელები = ["გიო", "დათა", "ლუკა," "მარი"]
რიცხვები = int(input("შეიყვანე რიცხვი"))
სახელები.insert(რიცხვები, "ნიკა")
print(სახელები)

# 3
sityvis_kaci = "გამარჯობა როგორ ხარ"
asoebi = "აეიოუ"

for g in sityvis_kaci:
    if g in asoebi:
        print(g)



# 5
numbers = [10, 20, 30, 40, 50]
შედეგი = sum(numbers)
დაითვლის = len(numbers)
print(შედეგი / დაითვლის)
