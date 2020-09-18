# Description

This challenge requires the player to read from and write to the global offset table to pwn the challenge.
An array of structs containing the members of a D&D party is in the BSS section. The player can specify 
a negative index into the array, therefore viewing the GOT. Similarly, when editing a name the player 
can overwrite the GOT. The exploit works by specifying an index of -4 and overwriting the atoi libc function.
The next time atoi is called, the player sends in "/bin/sh" and calls system("/bin/sh"). It was kind of 
fun to write.

# TODO

Just needs to be tested once it's running in CTFd. Also note that I have it running on port 8000, following the example of other challenges waiting to be assigned unique port numbers.
