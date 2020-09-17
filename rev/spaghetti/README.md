# spaghetti

__Category__: Reversing

This is a reversing challenge that instead of trying to reverse a black-box binary, the player has to break source-level obfuscation and recover the original source. Then, given knowledge with how `cpuid` works from the source, the user crafts a string that contains the host's processor vendor name. Even if they don't know what it is, the `cpuid` manual lists all options of vendors available (approx 20, most of them obscure) that they can bruteforce with.
