num = [4,2,6,8,10]
nums  = []
for i in num:
    if i % 2 == 0 and num.index(i) % 2 == 0:
        nums.append(i)
print(nums)