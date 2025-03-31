#true false -->

Ticketpurchased = True
securitycheck = True

if securitycheck == True:
    print("Security check done")
    if Ticketpurchased == True:
        print("Ticket purchased")
    else:
        print("Ticket not purchased")
        print("Please purchase the ticket")
        print("stay in the mall")    

else:
    print("Security check not done")        