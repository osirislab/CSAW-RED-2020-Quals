# Description

This is an easy forensics challenge provided by Dan Sanner at Pacific Northest 
National Laboratory. It was first used for the Pink Elephant Unicorn CTF held 
in Seattle between two and five years ago. 

Just extract the JPEG image from the packet capture using Wireshark. I think 
TCPDump might work too. Then connect to the challenge server and say what 
kind of animal is next to Domo. I think it's a chipmunk, but I allowed for
people to say "squirrel", "mouse", "dormouse" (provided by Google's reverse
image search) and "rodent."

Ideally we'd put the flag text on the actual image, but I was too lazy to set up 
the packet capture again so I created the extra step.

People can theoretically guess the flag by guessing "mouse", but it's only 50 points.

# TODO

Just needs to be tested once it's running in CTFd. Be sure to make sure the hint is working.
