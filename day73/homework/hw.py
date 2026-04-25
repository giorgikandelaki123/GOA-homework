# 2
def reverse(st):
    sityva = st.split()
    pasuxia = ""
    
    for i in range(len(sityva)-1, -1, -1):
        pasuxia += sityva[i]
        if i != 0:
            pasuxia += " "
    
    return pasuxia



# 3
def quote(fighter):
    if fighter.lower() == "conor mcgregor": 
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return "I am not impressed by your performance."

# 4
def replace_exclamation(st):
    aosebi = "aeiouAEIOU"
    sworia = ""
    
    for i in st:
        if i in aosebi:
            sworia += "!"
        else:
            sworia += i
            
    return sworia


# 5
def stringy(size):
    caamate = ""
    
    for i in range(size):
        if i % 2 == 0:
            caamate += "1"
        else:
            caamate += "0"
    
    return caamate