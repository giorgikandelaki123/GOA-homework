def list1(num):
    list2 = ["Gio", "goga", "Nika", "data", "Ilia"]
    amount = 0
    for i in list2:
        if len(i) >= 4 and i == i.capitalize():
            amount += 1
    return amount * num

print(list1(5))



def solution(string):
    string1 = "world"
    string1.reverse()