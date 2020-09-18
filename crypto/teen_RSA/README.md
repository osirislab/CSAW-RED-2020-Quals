# teen RSA

> Category: crypto
> Suggested Points: 200

# Description
> Detailed description as it would need to be explained to other lab members

RSA challenge with small e, given e and c

# Deployment
> Any special information about the deployment if there is a server component

Release teenrsa.py and output.txt

# Flag

flag{where_did_my_primes_go?}

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

Because e is very small, you can use Hastad's attack and simply take eth root of c to find m.
Use rsa.py to decrypt

# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

