# 1
"gavaket ukve"

# 2
def summation(num):
    return (num * (num + 1)) // 2

# 3
def sum_array(a):
    total = 0 
    
    for x in a:
        total += x 
        
    return total

# 4
def digitize(n):
    result = []

    if n == 0:
        return [0]
    while n > 0:
        result.append(n % 10)
        
        n = n // 10
    return result

# 5
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# 6
"ver gavige"

# 7
def find_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

# 8
"ver gavige"