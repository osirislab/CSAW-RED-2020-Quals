# Traverse 2

> Category: web
> Suggested Points: 75
> Distribute: index.js

# Description
> Detailed description as it would need to be explained to other lab members

Super simple directory traversal via get paramaters.

# Deployment
> Any special information about the deployment if there is a server component

Koajs app that listens on port 5000

# Flag

`flag{that_one_was_a_bit_harder_but_there_is_one_more...}`

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

They are given source, and they'll be able to see that they can just read a file through the filepath get param.

The twist here is that they cant start the filepath with `/`. The solution to that is to use `../`

The solution is very simple here. You just need to provide `../../../flag.txt` to the filepath get param.

`curl 'http://localhost:5000/?filepath=../../../flag.txt'`


# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

