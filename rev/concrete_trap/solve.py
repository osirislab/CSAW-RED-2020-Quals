from pwn import *
from z3 import *
import angr, claripy
from functools import reduce
context.log_level = 'debug'

def stage1(p):
    stage1_solution = "u_will_never_guess_this_because_its_so_long"
    p.sendlineafter("What is my super secret passcode?\n", stage1_solution)

def stage2(p):
    def guess_vals():
        for b in range(50, 100):
            print(f"Trying b = {b}")
            #unrolled: a = a ^ (ab)+b ^ a(b-1)+b ^ ... ^ a+b

            a = BitVec('a', 32)
            L = range(b, 0, -1)
            L = [a] + list(map(lambda x: BitVecVal(x, 32)*a+BitVecVal(b, 32), L))
            #L = [a, ba+b, (b-1)a+b, ..., a+b]

            s = Solver()

            s.add(reduce(lambda x,y: (x ^ y), L) == 31337)

            if s.check() == sat:
                ret_a = s.model()[a]
                ret_b = b
                return ret_a, ret_b

    a, b = guess_vals()
    print(f"Got {a} {b}")
    p.sendlineafter("What are my two numbers?\n", f"{a} {b}")

def stage3(p):
    angr_base = 0x400000
    pr = angr.Project("./concrete_trap")
    st = pr.factory.call_state(addr=angr_base+0xB3B)
    sm = pr.factory.simulation_manager(st)

    print("Starting to explore")
    sm.explore(find=angr_base+0xC4A, avoid=angr_base+0xC51)

    solution = sm.found[0].posix.dumps(0)
    #print(f"Solution: {solution}")
    p.sendlineafter("Even I haven't figured this one out yet\n", solution)


def main():
    #p = process("./concrete_trap")
    p = remote("localhost", 8000)

    p.recvuntil("shall fail.\n")
    stage1(p)
    stage2(p)
    stage3(p)

    p.interactive()


main()
