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
    # finalBal = cb(amount,balance)
    # #print(f"final balance = {finalBal}")
    # return finalBal
    return cb(amount,balance)

balance = 10000
while True:
    choice = int(input("press 1 for withdraw press 2 for deposit press 3 for exit"))

    if choice == 1:
        amount = int(input("enter ammount to withdraw"))
        balance = transaction(withdraw,balance,amount)
    elif choice == 2:    
        amount = int(input("enter ammount to deposit"))
        balance = transaction(deposit,balance,amount)
    elif choice ==3:
        break
    else:
        print("invalid chouce")    
        break


print(f"final balance = {balance}")    
