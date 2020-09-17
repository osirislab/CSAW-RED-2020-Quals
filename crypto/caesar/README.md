# Caesar, GoT edition

> Category: crypto
> Suggested Points: 50
> Distribute: challenge.txt (or challenge_less_dramatic.txt if the first is too much...)

# Description
> Detailed description as it would need to be explained to other lab members

Simple Caesar cipher using a key of 19, based off an alphanumeric set "abcdefghijklmnopqrstuvwxyz0123456789" for shifting.

# Deployment
> Any special information about the deployment if there is a server component

Included a dramatic version (Game of Thrones themed) and less dramatic version, defer to lab member's preference for which to deploy. Trying to spice up these easy 50 pointers...

# Flag

`flag{0lly_1s_th3_W3st3rosi_Brutu5}` (dramatic)
`flag{tak3_c4re_w1tH_fR13nD5_Nam3D_bRUTU5}` (less dramatic)

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

Use a solver such as https://planetcalc.com/8572/ using alphanumeric set "abcdefghijklmnopqrstuvwxyz0123456789" and pass in the ciphered text, shift = 19


# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

Contestants might not get the correct response if they do not preserve the case or if they use a solver that does not include numeric values in the set.
