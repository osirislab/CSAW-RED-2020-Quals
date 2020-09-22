import gdb
import string

"""
So I tried initially setting commands for breakpoints to do checkpoint/restore
but gdb 8.1 has a bug where commands is readonly even though docs say it's writable
then I tried putting the logic in custom gdb.Breakpoint.stop() for a watchpoint on
the return value ("success_flag") but you're apparently not supposed to change state
there and my watchpoint stopped getting triggered after even though the value was changing.
Then I found https://github.com/SouhailHammou/CTF/blob/master/HXP%20CTF%202017/Reversing/dont_panic/gdb_solve.py
and copied the structure, giving up on my really cool checkpoint/restore dream
it's not that cool now but whatever
"""

def main():
    #where gdb sets base of .text
    textbase = 0x555555554000

    #function with most of the program logic
    run_func = 0x930

    #this function takes a long time to run but does nothing
    #its return value is set to a negative offset from where we are in processing the buffer
    #hence never used
    useless_func = 0x8C0

    #$rdx in this branch contains where we are in the buffer
    main_branch = 0x9A2

    user_input = 0x7ffff7ff6064
    success_flag = 0x555555756020

    gdb.execute("set pagination off")

    bp = gdb.Breakpoint(f"*{textbase+main_branch}", gdb.BP_BREAKPOINT)

    flag = [" "] * 50
    flag = list("flag{m0m:w3_h4v3_v1rtu4l1z3r_4t_h0m3" + " "*14)

    #need 1st one to fail to get a baseline $rdx aka justifications for my shitty code
    #and last is punctuation without few chars cuz i cant be bothered to escape when sending to gdb
    charset = "\x01" + string.ascii_letters + string.digits + '!#$%&()*+,-./:;<=>?@[]^_{|}~'

    #compare rdx between runs to see if we progressed further (that character worked
    #and we failed on the next character)
    progress = 0
    for i in range(36,len(flag)):
        print(f"Flag: {''.join(flag)}")
        rdx = 0
        progress = 0
        for c in charset:
            flag[i] = c

            inp = "".join(flag)
            print(f"Trying {inp}")

            gdb.execute(f'starti <<< "{inp}"')
            gdb.execute(f"set *(char*)({textbase+useless_func}) = 0xC3")
            gdb.execute("c")

            still_fine = 0
            while still_fine == 0:
                still_fine = gdb.execute(f"x/wx {success_flag}", to_string=True)
                still_fine = int(still_fine.split("\t")[1].strip(), 16)
                blah = gdb.execute("c", to_string=True)
            while still_fine == 1:
                still_fine = gdb.execute(f"x/wx {success_flag}", to_string=True)
                still_fine = int(still_fine.split("\t")[1].strip(), 16)

                rdx = gdb.execute("p $rdx", to_string=True)
                rdx = int(rdx.split(" ")[-1])

                blah = gdb.execute("c", to_string=True)
            #print(f"Got rdx {rdx}")

            if progress == 0:
                progress = rdx

            if rdx > progress:
                break
            else:
                continue
    print("Finished")
    print(flag)


main()
