import angr
import claripy

class DoNothing(angr.SimProcedure):
    def run(self):
        return self.ret()

def main():
    p = angr.Project("./cracked", auto_load_libs=False)

    p.hook(0x4008C0, DoNothing())

    st = p.factory.entry_state()
    sm = p.factory.simgr(st)

    sm.explore(find =lambda s: b"yay" in s.posix.dumps(1),
               avoid=lambda s: b":("  in s.posix.dumps(1))

    print(sm.found[0].posix.dumps(1))
    print(sm.found[0].posix.dumps(0))


main()
