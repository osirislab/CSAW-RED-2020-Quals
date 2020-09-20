from enum import IntEnum

class Opcodes(IntEnum):
    NOP = 0
    MOVC = 1
    MOVR = 2
    PUT = 3
    GET = 4
    INC = 5
    DEC = 6
    MUL = 7
    SHRINK = 8
    XOR = 9
    HRMPF = 10

class Variables(IntEnum):
    a = 0x61
    b = 0x62
    c = 0x63
    d = 0x64
    e = 0x65

flag = 'flag{m0m:w3_h4v3_v1rtu4l1z3r_4t_h0m3}'

encode_flag = []
i = 100

encode_flag.append(Opcodes.MOVC.value)
encode_flag.append(Variables.a.value)
encode_flag.append(0)

for c in flag:
    encode_flag.append(Opcodes.MOVC.value)
    encode_flag.append(Variables.b.value)
    encode_flag.append(((ord(c)*3)^i)&0xff)

    encode_flag.append(Opcodes.PUT.value)
    encode_flag.append(Variables.a.value)
    encode_flag.append(Variables.b.value)

    encode_flag.append(Opcodes.INC.value)
    encode_flag.append(Variables.a.value)

    i += 1

decode_input = []

decode_input.append(Opcodes.MOVC.value)
decode_input.append(Variables.a.value)
decode_input.append(100)

decode_input.append(Opcodes.MOVC.value)
decode_input.append(Variables.e.value)
decode_input.append(0)

decode_input.append(Opcodes.MOVC.value)
decode_input.append(Variables.d.value)
decode_input.append(1)

i = 0
while i < 37:
    decode_input.append(Opcodes.GET.value)
    decode_input.append(Variables.b.value)
    decode_input.append(Variables.a.value)

    decode_input.append(Opcodes.MOVC.value)
    decode_input.append(Variables.c.value)
    decode_input.append(3)

    decode_input.append(Opcodes.MUL.value)
    decode_input.append(Variables.b.value)
    decode_input.append(Variables.c.value)

    decode_input.append(Opcodes.XOR.value)
    decode_input.append(Variables.b.value)
    decode_input.append(Variables.a.value)

    decode_input.append(Opcodes.SHRINK.value)
    decode_input.append(Variables.b.value)

    decode_input.append(Opcodes.GET.value)
    decode_input.append(Variables.c.value)
    decode_input.append(Variables.e.value)

    decode_input.append(Opcodes.HRMPF.value)
    decode_input.append(Variables.d.value)
    decode_input.append(Variables.b.value)
    decode_input.append(Variables.c.value)

    decode_input.append(Opcodes.INC.value)
    decode_input.append(Variables.a.value)

    decode_input.append(Opcodes.INC.value)
    decode_input.append(Variables.e.value)
    i += 1

program = encode_flag + decode_input

print(program)
#print("".join(map(str, program)))


