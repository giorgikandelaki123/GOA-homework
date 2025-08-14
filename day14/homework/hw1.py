#დააყენე საწყისი ბალანსი და ცარიელი ტრანზაქციების სია
balance = 0
transactions = []

def show_balance():
    print("ბალანსი:", balance)

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        transactions.append(f"+{amount}")
        print(f"{amount} ჩაირიცხა")
    else:
        print("არასწორი თანხა")

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        transactions.append(f"-{amount}")
        print(f"{amount} გაიყვანეს")
    else:
        print("არასაკმარისი თანხა ან არასწორი თანხა")

# მაგალითად:
deposit(100)
show_balance()
withdraw(50)
show_balance()
print("ტრანზაქციები:", transactions)



#ბალანსის ნახვა
balance = 1000

def show_balance():
    print(f"ბალანსი: {balance} ₾")
show_balance()