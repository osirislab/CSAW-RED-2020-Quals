# Description

This is a fairly easy forensics challenge provided by Dan Sanner at Pacific Northest 
National Laboratory. It was first used for the Pink Elephant Unicorn CTF held 
in Seattle between two and five years ago. It's an easy but non-trivial
challenge that teaches a practical skill.

This is an image exfiltrated through ICMP traffic, from 10.67.8.102 to 10.15.200.47. 
The trick is to recognize that the first packet containing the actual image is the 
fourth one, since it's the first one that is 540 bytes long. I solved it by 
using Scapy to parse the data sections of each outgoing packet and then 
reassemble the data into the TIFF file. 

The TIFF file is a picture of an octopus with the words "galactic octopus" 
prominently displayed. You get the flag by connecting to the box running
`interception.py` and entering "galactic octopus" in response to the question, 
"who was the admin trying to contact?" I tried to account for a number of 
ways the user could try to enter those words, so the problem is forgiving.

I figure 175 points for this one, since it requires the player to learn Scapy or 
at least review it. It's not hard to solve one you know how to do that, but 
it's probably a new skill for many high school students.

# TODO

Just needs to be tested once it's running in CTFd.