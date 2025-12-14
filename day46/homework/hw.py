# 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(nums)-1, -1, -1):
    if nums[i] % 2 == 0 or i % 2 == 1:
        nums.remove(nums[i])

print(nums)

# 2
words = ["apple", "banana", "cherry"]

nodo = len(words)
for i in range(nodo):
    words.append(words[i])

print(words)

# 3
