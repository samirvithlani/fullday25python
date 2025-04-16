#stirng is immutable..
data = "amit"
data = data.upper()
print(data)

data =data.lower()
print(data)

sent = "hi thIs iS iNdia"
#sent = sent.title()
#sent = sent.capitalize()
sent = sent.swapcase()
print(sent)



email = "  samir@gmail.com   "
print("email = ",email)
print(len(email))

#email = email.rstrip()
#email = email.lstrip()
email = email.strip()
print("email = ",email)
print(len(email))


#split join...
address ="Surbhi Complex, 2nd and 3rd floor, Chimanlal Girdharlal Rd, Opposite Municipal Market, Vasant Vihar, Navrangpura, Ahmedabad, Gujarat 380009"

add = address.split(" ")
print(add)

name = "royal"
name = name.join("   ")
print(name)

