# Description

This challenge requires the user to exploit a format string vulnerability to overwrite an integer in the BSS section. 
The integer is small, so it is an easy write to achieve. Source code is provided to make the challenge easier -- this 
is meant to be someone's first format string challenge. For a first challenge it is still kind of difficult because 
the player still has to pull off a write. I chose not to provide compilation instructions in the source code to 
avoid confusion if the player's local binary has the global integer in a different location than the one 
running on the server. The challenge is D&D-themed because why not. That way everyone knows who to ping on the forums 
with questions. Escape from a dungeon.

# TODO

Just needs to be tested once it's running in CTFd. Also note that I have it running on port 8000, following the example of other challenges waiting to be assigned unique port numbers.
