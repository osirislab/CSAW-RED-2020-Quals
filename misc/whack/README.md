# Description

This is a scripting challenge authored by Dan Best at Pacific Northest National Laboratory
for the Pink Elephant Unicorn CTF held in Seattle between two and five years ago. 
The Python script is his original script, as is the Perl solver which is buggy and 
does not catch all cases. I was concerned that the problem might be with the 
challenge itself and not the solver, so I wrote a Python solver based on Dan's 
Perl script which is not buggy and gets the flag every time. I'm giving this 
250 points. It might only be 200 but I want to reward people for being good
programmers.

Basically, it's whack-a-mole. To solve it you have to find the correct row and 
column where the mole is hiding. Every ten whacks you go up a level and the 
board gets larger, the borders for the holes change a bit, and smileys start
popping up that you lose if you whack. You also get less time to whack the 
mole. By level 10 you only have 0.6 seconds to pull it off (that still should 
be slow enough for connections from Dubai to work.)

We should give credit to Dan, but I want to do so in an announcement after 
the competition closes just in case a write-up is on the web somewhere.
Note that I could not find any Pink Elephant Unicorn CTF write-ups online.
The CTFs were all held in person, and not linked to CTF Time. So I think 
we should be pretty safe from cheating.

# TODO

Just needs to be tested once it's running in CTFd.
