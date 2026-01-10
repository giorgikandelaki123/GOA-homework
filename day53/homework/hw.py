# 2
words = ["gamarjoba", "NINO", "nika", "HELLO", "giga"]
axali_list = []

for i in words:
    if i == i.lower() and i[0] == "g":
        axali_list.append("Goga")
    elif i == i.upper() or i[0] == "N":
        axali_list.append("Nika")
    else:
        axali_list.append("ლიდერი")

print(axali_list)

# 3
numbers = [1, 2, 3, 4, 5]
new_list = []
i = 0

while i < len(numbers):
    ricxvi = numbers[i]

    if ricxvi % 2 == 0 or i % 2 == 0:
        new_list.append(ricxvi * ricxvi)
    else:
        new_list.append(ricxvi * 2)
    i = i + 1

print(new_list)

# 5
# ეს არის for
num = "0123456789"
list_num = []

for i in range(len(numbers)):
    cifri = int(numbers[i]) 
    if i % 2 == 0 or cifri > 7:
        new_list.append(cifri)
print(new_list)

# ეს არის while
numbers = "0123456789"
new_list = []
i = 0

while i < len(numbers):
    cifri = int(numbers[i])
    if i % 2 == 0 or cifri > 7:
        new_list.append(cifri)
    i = i + 1
print(new_list)