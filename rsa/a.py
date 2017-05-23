from Crypto.Util.number import getPrime, isPrime, GCD, inverse

nbits = 2048
gbits = 992
g = getPrime(int(gbits))
while True:
    a = getPrime(int(nbits*0.5)-gbits)
    p = 2*g*a + 1
    if isPrime(p):
        break

while True:
    b = getPrime(int(nbits*0.5)-gbits)
    q = 2*g*b + 1
    if p!=q and isPrime(q):
        break
N = p*q
e = 65537

def str2int(s):
    return int(s.encode('hex'),16)

def int2str(i):
    tmp=hex(i)[2:-1]
    if len(tmp)%2==1:
        tmp='0'+tmp
    return tmp.decode('hex')

with open('pubkey.txt','w') as f:
    f.write(str(e)+'\n')
    f.write(str(N)+'\n')

with open('flag.txt') as f:
    plain = str2int(f.read())

c = pow(plain,e,N)
with open('cipher.txt','w') as f:
    f.write(int2str(c))
