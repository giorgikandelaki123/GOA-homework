# 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in nums[:]:  
    index = nums.index(n)
    if n % 2 == 0 or index % 2 == 1:
        nums.remove(n)

print(nums)


# 2
words = ["apple", "banana", "cherry"]

for w in words[:]:
    words.append(w)

print(words)


# 3
numbers = [10, 15, 20, 25, 30, 35]      
for num in numbers[:]:
    if num % 10 == 0:
        numbers.remove(num)
    else:
        numbers.append(num)
print(numbers)

# 4
words = ["one", "two", "three", "four", "five"]
for i in range(len(words) - 1, -1, -1):
    if len(words[i]) % 2 == 0:
        words.pop(i)
    else:
        words.insert(0, words[i])
print(words)