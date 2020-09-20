# Description

This challenge is the next iteration of the spellcoding challenges.
It is much harder than the previous ones. But it's really fun. 
This is an x86-64 challenge (previous levels were 32 bits).
The admin's shellcode jumps the player to exit(0), and the player 
has to turn that shellcode into execve("/bin/sh",0,0) by writing 
only one byte at a time while preserving their access to the
program. Also, with every write there's a check that the code 
does not contain null bytes. I solved it by first changing the 
jump so it looped back and gave multiple writes, then added a short 
jump to the front of the shellcode. That took finesse because a short 
jump requires two writes and I needed to create an innocuous instruction 
to get there. Then I added the execve("/bin/sh",0,0) code to the middle, 
and finally changed the short jump to jump to the shellcode that 
spawns the shell. It was challenging to write and challenging 
to solve. I think people will enjoy it. I'm giving it 400 points.

The challenge is D&D themed because all good challenges are D&D themed. 
The spells are straight out of the Player's Handbook and the puns are 
the best D&D puns ever used in a CSAW RED 2020 CTF 3rd-level shellcoding 
challenge.

# TODO

Just needs to be tested once it's running in CTFd. Also note that I have it running on port 8000, following the example of other challenges waiting to be assigned unique port numbers.

# Glitches

I could not have the user write to the very first byte of the shellcode buffer, 
but that does not impact the solvability of the challenge. It may have been an 
issue with GDB. I couldn't figure out the problem during debugging, everything 
looked fine. In any case, there's enough room in the buffer for that to not be 
a problem for people.
