from pwn import *

p = process('./prop_remote')
#p = remote('rev.red.csaw.io', 5000)
print(p.recvuntil(':'))
p.sendline('mvsvds~l}tvem&xxbcabfai{')
print(p.recvuntil('}'))
p.interactive()