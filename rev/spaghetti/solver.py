#!/usr/bin/env python3
"""
solver.py

    Regenerates source and sends correct string back to program.
"""
from pwn import *

# change if host processor is different
PWD = b"CPU:GenuineIntel"

with open("spaghetti.c", "r") as fd:
    lines = fd.readlines()

lines = lines[6:]

code = []
mapping = {}
for line in lines:
    if line.startswith("#define"):
        parts = line.split(" ")
        mapping[parts[1]] = parts[2].strip()
    else:
        code = line.split(" ")

for n, sym in enumerate(code):
    if sym in mapping:
        code[n] = mapping[sym]

# this generates the source code we want to read from
final_code = "".join([elem for elem in code])
with open("generated.c", "w") as fd:
    fd.write(final_code)

#p = subprocess.Popen(['./spaghetti'], stdin=subprocess.PIPE)
#print(p.communicate(input=PWD)[0])

r = remote("rev.red.csaw.io", 5001)
conn.recvline()
conn.send(PWD)
print(conn.recvline())
conn.close()
