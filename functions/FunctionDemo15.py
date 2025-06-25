def printMarkshit(*args):
    
    def calulatePers():
        total = 0
        for i in args:
            total = total+i
            print(total)
        return (total*100)/(len(args)*25)
            
    
    pers = calulatePers()
    print(f"pers = {pers}")

printMarkshit(23,22,24,12,18,25)            
        