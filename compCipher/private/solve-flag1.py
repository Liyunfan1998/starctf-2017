
c='a106bb05b0b2f81e04701afe73af0eda344636b79f04b506992c26d82b00388a846417db9e66465beaeb40de26dc'.decode('hex')
keys=[]
keys.append([])
l=len(c)
for i in range(l):
    keys[0].append(i)
for i in range(1,30):
    keys.append([])
    for j in range(l):
        keys[i].append((keys[i-1][j]*97+7)%256)
for i in range(30)[::-1]:
    c2=c
    c=''
    if i%2==1:
        for j in range(l):
            c+=chr(ord(c2[j])^keys[i][j])
    else:
        for j in range(l):
            c+=chr((ord(c2[j])-keys[i][j]+256)%256)
print c
