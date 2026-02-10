# 1
def goga(name):
    return "გამარჯობა" + name + "!" 

print(goga("giorgi"))
print(goga("erekle"))
print(goga("datoo")) 


# 2
def ricxvebi_jami(num1, num2):
    return num1 + num2

print(ricxvebi_jami(6, 7))
print(ricxvebi_jami(3, 0))

# 3
def kvadrati(num):
    return num * num

print(kvadrati(4))
print(kvadrati(2))

# 4
def weli(age):
    if age >= 18:
        return "სრულწლოვანი ხარ"
    else:
        return "არ ხარ სრულწლოვანი"

print(weli(24))
print(weli(12))


# 5
def datvla(string):
    print(len(string))

datvla("გამარჯობა")  
datvla("hello")     
datvla("privet")         

# 6
def gamravleba(num1, num2):
    return num1 * num2

print(gamravleba(5, 10))
print(gamravleba(3, 7))   
print(gamravleba(4, 0))   

# 7
def qula(score):
    if score >= 90:
        return "შესანიშნავი ქულა"
    elif 70 <= score <= 89:
        return "კარგი ქულა"
    elif 50 <= score <= 69:
        return "დამაკმაყოფილებელი ქულა"
    else:
        return "ჩაჭრილი"

print(qula(95)) 
print(qula(75)) 
print(qula(55)) 
print(qula(30)) 



# 8
def kentia_luwia(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(kentia_luwia(10)) 
print(kentia_luwia(7)) 

# 9
def pirveli_aso(name):
    return name[0]

print(pirveli_aso("Giorgi")) 
print(pirveli_aso("Mariam")) 
print(pirveli_aso("Levani")) 


# 10
def pasuxi(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(pasuxi(10, 20, 30))
print(pasuxi(30, 90, 30))    

# 11
def paroli(password):
    if password == "python123":
        return "წვდომა დაშვებულია"
    else:
        return "არასწორი პაროლი"


print(paroli("python123")) 
print(paroli("12345"))      
print(paroli("Python123")) 