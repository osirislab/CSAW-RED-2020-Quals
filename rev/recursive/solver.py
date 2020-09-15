from pwn import *

p = process('./recursive')
p.recvline
p.sendline('1408')
p.recvline
p.interactive()

