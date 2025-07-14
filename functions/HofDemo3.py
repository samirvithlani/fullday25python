
def science(studentName):
    print(f"{studentName} your admission confirmed in science")
def commerce(studentName):
    print(f"{studentName} your admission confirmed in commm")
def arts(studentName):
    print(f"{studentName} your admission confirmed in arts")
    
def getAdmission(cb,sname):
    print("welcome to get admission window....")
    #cb("RAJ") #sc,com,arts
    cb(sname)


# pers = 81
# stuName = "jay"
pers = int(input("enter pers : "))
stuName  = input("enter name :")
if pers>80:
    getAdmission(science,stuName)
elif pers>70:
    getAdmission(commerce,stuName)    
elif pers>60:
    getAdmission(arts,stuName)    
else:
    print("no admission....")    