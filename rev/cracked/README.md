The comparison code is virtualized. An mmap'd memory section contains both the (encoded) flag and user input.

This can be made significantly easier by removing -O3 assuming the teams are trying to reverse the vm. Observing the memory region and figuring out what's going on is easier, specially given that they'll probably try the flag format.

Instead of failing immediately on mismatch, a variable holds success/fail state (to avoid instruction counting). Teams will have to notice this and either figure out the relation between the numbers or do something like a gdb script to bruteforce one character at a time.

Also note only 37 characters are compared. The rest are ignored.
