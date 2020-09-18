from pwn import *

#p = process('./recursive')
p = remote('rev.red.csaw.io', 5000)
p.recvline
p.sendline('1408')
p.recvline
p.interactive()

