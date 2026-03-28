# 1
def dont_give_me_five(start, end):
    ramdenia = 0
    for n in range(start, end + 1):
        if "5" not in str(n):
            ramdenia += 1
    return ramdenia


# 2
def solution(text, ending):
    return text[len(text) - len(ending):] == ending

# 3


# 4
def number(bus_stops):
    jami = 0
    for i in bus_stops:
        jami += i[0] - i[1]
    return jami