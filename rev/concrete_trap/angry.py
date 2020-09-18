import angr
import claripy
from pwn import *

def solve():
    p = angr.Project("./concrete_trap", auto_load_libs=False)

    st = p.factory.entry_state()
    sm = p.factory.simgr(st)

    sm.explore(find=lambda s: b"slightly convinced" in s.posix.dumps(1))

    stage1_solution = sm.found[0].posix.dumps(0)
    len_stage1_solution = len(stage1_solution)
    stage1_solution = stage1_solution[:-4]
    print(stage1_solution)

    sm.move(from_stash='found', to_stash='active')

    sm.explore(find=lambda s: b"couple bazillion" in s.posix.dumps(1))

    stage2_solution = sm.found[0].posix.dumps(0)[len_stage1_solution:]
    len_stage2_solution = len(stage2_solution)
    print(stage2_solution)

    sm.move(from_stash='found', to_stash='active')

    sm.explore(find=lambda s: b"Amazing" in s.posix.dumps(1))

    stage3_solution = sm.found[0].posix.dumps(0)[len_stage1_solution+len_stage2_solution:]
    print(stage3_solution)

    return stage1_solution, stage2_solution, stage3_solution

def main():
    s1, s2, s3 = solve()

    p = process("./concrete_trap")
    p.sendlineafter("passcode?\n", s1)
    p.sendlineafter("numbers?\n", s2)
    p.sendlineafter("yet\n", s3)
    p.interactive()

main()
