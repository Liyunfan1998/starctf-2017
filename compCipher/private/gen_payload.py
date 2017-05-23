
for seed in range(255):
    c='d'*0x68+'130c400000000000c30c4000000000005007400000000000'.decode('hex')
    keys=[]
    keys.append([])
    l=len(c)

    for i in range(l):
        keys[0].append((seed+i)%256)
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
    if c.find('\n')==-1 and c.find('\t')==-1 and c.find(' ')==-1 and c.find('\x0b')==-1 and c.find('\x0c')==-1:
        print seed
        print c.encode('hex')
        break
