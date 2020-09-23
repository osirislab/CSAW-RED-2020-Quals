#!/usr/bin/python2
#solve-mind-reader.py
#by N4T_20

# See Wenliang Du, Computer & Internet Security: A Hands-on Approach, 2nd edition, p. 486
# for a description of this chosen-plaintext attack on AES with output feedback mode
# when the IV is reused.

# This solver is in Python 2. server.py is in Python 3.

from base64 import b64encode, b64decode

from pwn import *
local = True
if local:
    p = remote('localhost',5000)
else:
    p = remote('crypto.red.csaw.io', 5001)

def get_secret_ct():
    p.send("1\n")
    p.recvuntil("thinking: ")
    thought = p.recvuntil("\r\n")
    thought_bytes = b64decode(thought)
    p.recvuntil("> ")
    return(thought_bytes)

def get_ct_from_chosen_pt(pt):
    chosen_pt_bytes = bytes(pt)
    p.send("2\n")
    p.recvuntil("> ")
    pt_b64_encoded = b64encode(chosen_pt_bytes)
    p.send(pt_b64_encoded + "\n")
    p.recvuntil("thinking: ")
    thought = p.recvuntil("\r\n")
    thought_bytes = b64decode(thought)
    p.recvuntil("> ")
    return(thought_bytes)

def xor_two_strings(str1, str2):
    output = ""
    n = len(str1)
    for i in range(n):
        output += chr(ord(str1[i])^ord(str2[i]))
    return output

p.recvuntil(">")
ct = get_secret_ct()
pt1 = "A"*63
ct1 = get_ct_from_chosen_pt(pt1)
output_stream = xor_two_strings(pt1,ct1)
pt = xor_two_strings(output_stream, ct)
print("pt = " + str(pt))
p.interactive()