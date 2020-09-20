# Super Secret 3

> Category: crypto
> Suggested Points: 150
> Distribute: challenge.txt

# Description
> Detailed description as it would need to be explained to other lab members

Slightly complicated XOR of 'guess' to get obfuscated text. Increments final character instead of repeating 'guess' only.
Builds off previous challenge. Could be difficult if you don't do the previous challenges.
Still possible to complete as 'guess' is in the challenge description.

# Deployment
> Any special information about the deployment if there is a server component

All information included in challenge.txt.

# Flag

`flag{A1m0st_G00d_S3kur1ty}`

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

Use python locally or an online solver like https://www.browserling.com/tools/xor-decrypt (outputs plain text instead of hex)
Must try using the plaintext solution from the previous challenge to find the repeating/incrementing key 'guess'. Possibly can find the answer brute force or with
frequency analysis but likely difficult that way.

SECRET username: ceaser password: flag{A1m0st_G00d_S3kur1ty}

# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

If using md5crypt.com will get hex values of ASCII instead of actual text when 'decrypting'.
Challenge text should hint that only the key was changed and not all of the plain text - if this is not clear to someone can be very tricky.
