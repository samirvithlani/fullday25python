def log_Data(func):
    
    def inner(*args,**kwargs):
        print(f"accessing function  {func.__name__}")
        func(*args,**kwargs) #make_payment(1 args)
    
    return inner



@log_Data
def make_payment(amount):    
    print(f"making payment of  {amount}")


@log_Data
def send_mail(to,subject):
    print(f"seding mail to {to} and subject is {subject}")    


make_payment(1000)    
send_mail("samir","test")