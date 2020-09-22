The comparison code is virtualized. An mmap'd memory section contains both the (encoded) flag and user input.

A useless function must be patched out (it's return value is written to a negative offset from iterator).

Instead of failing immediately on mismatch, a variable holds success/fail state. Teams will have to notice this (it's the return value so pretty straightforward) then figure out which input keeps it at 1. You can bruteforce characters with a gdb script or just use angr.

Also note only 37 characters are compared. The rest are ignored.

2 solvers included.
`$ python3 angry.py`
`$ echo "source solve2.py" | stdbuf -i 0 -o 0 -e 0 gdb cracked | grep "Flag\|Trying"`
