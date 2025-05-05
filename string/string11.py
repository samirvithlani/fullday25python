no = 123
nostr = str(no) #"123"
flag = True
for i in range(0,len(nostr)-1):
    #4>9
    if (nostr[i]>nostr[i+1]):
        flag = False
        break

print("flag ",flag)    