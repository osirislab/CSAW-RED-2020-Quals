# Super Secret 2

> Category: crypto
> Suggested Points: 100
> Distribute: challenge.txt

# Description
> Detailed description as it would need to be explained to other lab members

Basic XOR of 'noway' to get obfuscated text. Builds off previous challenge. Could be difficult if you don't do the previous challenge.
Could be really easy if you guess the initial plaintext is the same as the previous challenge.

# Deployment
> Any special information about the deployment if there is a server component

All information included in challenge.txt.

# Flag

`flag{S3curity_Thr0ugh_0bscur1ty}`

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

Use python locally or an online solver like https://www.browserling.com/tools/xor-decrypt (outputs plain text instead of hex)
Must try using the plaintext solution from the previous challenge to find the repeating key 'noway'. Possibly can find the answer brute force or with
frequency analysis but likely difficult that way.

SECRET username: ceaser password: flag{S3curity_Thr0ugh_0bscur1ty}

# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

If using md5crypt.com will get hex values of ASCII instead of actual text when 'decrypting'.
Challenge text should hint that only the key was changed and not all of the plain text - if this is not clear to someone can be very tricky.
