# Super Secret 1

> Category: crypto
> Suggested Points: 50
> Distribute: challenge.txt

# Description
> Detailed description as it would need to be explained to other lab members

Basic XOR of 'secret' to get obfuscated text. Next challenge builds on this one.

# Deployment
> Any special information about the deployment if there is a server component

All information included in challenge.txt.

# Flag

`flag{C@nt_Bre@k_Th1$}``

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

Use python locally or an online solver like https://www.browserling.com/tools/xor-decrypt (outputs plain text instead of hex)
Must guess 'secret' is the key, although the first 6 cipher characters being the same should be a clue as well as SECRET in caps.

SECRET username: ceaser password: flag{C@nt_Bre@k_Th1$}

# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

Might be a stretch to guess XOR, but if its at 50 pts hopefully people will go with simple first.
If using md5crypt.com will get hex values of ASCII instead of actual text when 'decrypting'.
