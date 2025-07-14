def withdraw(amount,bal):
    print("withdraw process started...")
    bal -=amount
    return bal


def deposit(amount,bal):
    print("deposit process started...")
    bal +=amount
    return bal


def transaction(cb,balance,amount):
    print("welcome to your account..")
    finalBal = cb(amount,balance)
    #print(f"final balance = {finalBal}")
    return finalBal

balance = 10000
choice = int(input("press 1 for withdraw press 2 for deposit"))

if choice == 1:
    amount = int(input("enter ammount to withdraw"))
    balance = transaction(withdraw,balance,amount)
elif choice == 2:    
    amount = int(input("enter ammount to deposit"))
    balance = transaction(deposit,balance,amount)

print(f"final balance = {balance}")    
