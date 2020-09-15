# Traverse 1

> Category: web
> Suggested Points: 50
> Distribute: index.js

# Description
> Detailed description as it would need to be explained to other lab members

Super simple directory traversal via get paramaters.

# Deployment
> Any special information about the deployment if there is a server component

Koajs app that listens on port 5000

# Flag

`flag{wow_you_got_it!_lets_see_if_you_can_get_the_next_one...}`

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

They are given source, and they'll be able to see that they can just read a file through the filepath get param.

The solution is very simple here. You just need to provide `/flag.txt` to the filepath get param.

`curl 'http://localhost:5000/?filepath=/flag.txt'`


# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

