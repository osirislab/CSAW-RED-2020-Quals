# Eating Healthy

> Category: crypto
> Suggested Points: 50
> Distribute: challenge.txt (or challenge_less_dramatic.txt if the first is too much...)

# Description
> Detailed description as it would need to be explained to other lab members

Simple Caesar cipher using a key of 19, based off an alphanumeric set "abcdefghijklmnopqrstuvwxyz0123456789" for shifting.

# Deployment
> Any special information about the deployment if there is a server component

All information included in challenge.txt. Can paste into a .py or other file if that is preferred.  

# Flag

`flag{ca35ar_5alad_w1th_cr0ut0ns}`

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

Use a solver such as https://planetcalc.com/8572/ using alphanumeric set "abcdefghijklmnopqrstuvwxyz0123456789" and pass in the ciphered text, shift = 19


# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

Contestants might not get the correct response if they do not preserve the case or if they use a solver that does not include numeric values in the set.
