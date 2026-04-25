# 1
def multi_table(number):
    empty = ""
    for i in range(1, 11):
        empty += str(i) + " * " + str(number) + " = " + str(i * number)
        if i != 10:
            empty += "\n"
    return empty


# 2
"ver gavige"




# 3
"ver gavige"



# 4
def add_length(str_):
    carieli = []
    teqsti = str_.split(" ")
    for i in teqsti:
        carieli.append(i + " " + str(len(i)))
    return carieli



# 5
def reverse_list(l):
    return l[::-1]


# 6
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        catYears = 15
        dogYears = 15
    elif human_years == 2:
        catYears = 24
        dogYears = 24
    else:
        catYears = 24 + (human_years - 2) * 4
        dogYears = 24 + (human_years - 2) * 5
    return [human_years, catYears, dogYears]


# 7
def str_count(strng, letter):
    return strng.count(letter)