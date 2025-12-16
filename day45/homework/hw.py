# # 1
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = []

# for haha in nums:
#     if haha % 2 == 0:
#         even_nums.append(haha)

# print(even_nums)

# # 2
# numbers = [1, 3, 4, 7, 8, 9, 10]
# result = []

# for i in range(len(numbers)):
#     if i % 2 == 1:
#         if numbers[i] % 2 == 1:
#             result.append(numbers[i])

# print(result)

# # 3
# names = ["გიორგი", "ანა", "გიგი", "ლუკა", "გელა"]

# for i in range(len(names) - 1, -1, -1):
#     if names[i][0] == "გ" and names[i][-1] == "ი":
#         names.pop(i)

# print(names)

# names = ["გიორგი", "ანა", "გიგი", "ლუკა", "გელა"]

# for name in names[:]:
#     if name[0] == "გ" and name[-1] == "ი":
#         names.remove(name)

# print(names)

<<<<<<< HEAD
=======

# # 4
# words = ["Apple", "banana", "Car", "dog", "Tree", "house"]

# for i in range(len(words) - 1, -1, -1):
#     first_letter = words[i][0]

#     if first_letter >= "A" and first_letter <= "Z":
#         if i % 2 == 1:
#             words[i] = words[i].lower()
#         else:
#             words.pop(i)

# print(words)

# 5


# 6
nums = [1, 2, 4, 5, 6, 8, 9, 10]
words = ["Apple", "banana", "Cat", "dog", "Elephant", "fish"]


numes = []

for i in range(len(nums)):
    if i % 2 == 1 and nums[i] % 2 == 0:
        numes.append(nums[i])
print(numes)


>>>>>>> 988668f5134cfef38a3b543a49e87b276f755500
