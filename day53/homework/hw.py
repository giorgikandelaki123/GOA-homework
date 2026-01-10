# 2
random = ["gamarjoba", "NINO", "HELLO", "giga", "ilia"]
axali_list = []

for i in random:
    if i == i.lower() and i[0] == "g":
        axali_list.append("Goga")
    elif i == i.upper() or i[0] == "N":
        axali_list.append("Nika")
    else:
        axali_list.append("ლიდერი")

print(axali_list)

# 3
numb = [1, 2, 3, 4, 5]
list_00 = []
i = 0

while i < len(numb):

    if numb[i] % 2 == 0 or i % 2 == 0:
        list_00.append(numb[i] ** 2)
    else:
        list_00.append(numb[i] * 2)
    i = i + 1

print(list_00)

# 5
nums = "012345678"
list_nums = []

for i in range(len(nums)):
    cifri = int(nums[i]) 
    if i % 2 == 0 or cifri > 7:
        list_nums.append(cifri)
print(list_nums)
