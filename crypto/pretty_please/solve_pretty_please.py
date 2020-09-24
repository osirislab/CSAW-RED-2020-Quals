#!/bin/python2
# solve pretty_please
# by N4T_20

from pwn import *
from time import sleep
import binascii
from base64 import b64encode, b64decode

local = True
if local:
    p = remote('localhost', 5000)
else:
    p = remote('crypto.ctf.csaw.io', 5002)

p.recvuntil("> ")

def get_ct():
    p.send("1\n")
    p.recvuntil("> ")
    p.send("blah\n")
    p.recvuntil("Token: ")
    ct = p.recvuntil("\r\n")
    p.recvuntil("> ")
    return ct

def send_new_ct(new_ct):
    p.send("2\n")
    p.recvuntil("> ")
    p.send(new_ct + "\n")
    p.interactive()

def xor_two_strings(str1, str2):
    output = ""
    n = len(str1)
    for i in range(n):
        output += chr(ord(str1[i])^ord(str2[i]))
    return output

ct = b64decode(get_ct())

# Flip bits in the ciphertext so that "REJECTED" reads "ACCEPTED"
tmp = xor_two_strings("REJECTED", "ACCEPTED")
ct_end = ct[(len(ct)-len("REJECTED")):]
ct_start = ct[0:(len(ct)-len("REJECTED"))]
new_ct = ct_start + xor_two_strings(tmp, ct_end)
new_ct_b64 = b64encode(new_ct)

send_new_ct(new_ct_b64)
p.interactive()