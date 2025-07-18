
def login_Required(func):
    
    def inner(**kwargs):
        if kwargs["role"] == "ADMIN":
            func(**kwargs)
        else:
            print(f"No access granted....")    
    
    return inner        


@login_Required
def access_data(**kwargs):
    print(f"accessing dtaa by {kwargs["name"]} ")


access_data(name="RAM",role="USER")