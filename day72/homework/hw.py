# 1


# 2


# 3


# 4
def well(x):
    datvla = x.count("good")
    
    if datvla == 0:
        return "Fail!"
    elif datvla <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
    

# 5
def warn_the_sheep(queue):
    n = queue[::-1].index('wolf')
    
    if n == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number " + str(n) + "! You are about to be eaten by a wolf!"
    

# 6 
def sum_digits(numbers):
    jami = 0
    for i in str(numbers):
        if i != "-":
            jami += int(i)
    return jami

# 7
def number(lines):
    pasuxi = []
    for i in range(len(lines)):
        pasuxi.append(str(i+1) + ": " + lines[i])
    return pasuxi

# 8
def remove_url_anchor(url):
    pasuxi = ""
    for simbolo in url:
        if simbolo == "#":
            return pasuxi
        pasuxi += simbolo
    return pasuxi

# 9
def position(letter):
    anbani = "abcdefghijklmnopqrstuvwxyz"
    adgili = anbani.find(letter) + 1
    return "Position of alphabet: " + str(adgili)

# 10
