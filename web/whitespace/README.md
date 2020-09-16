# Flask-Caching

> Category: web
> Suggested Points: 200
> Distribute: app.py

# Description
> Detailed description as it would need to be explained to other lab members

This is influenced by the CTFd authentication bug from a while back. It all comes down to 
not stripping whitespace from the username.

[cve](https://nvd.nist.gov/vuln/detail/CVE-2020-7245)

# Deployment
> Any special information about the deployment if there is a server component

Just a flask app that runs on 5000. We're going to restart the app and reset the database every 60s in the container.

# Flag

`flag{gotta_make_sure_you_handle_the_whitespace!}`

# Solution
> As detailed as possible description of the solution. Not just the solver script. As full a description as possible of the solution for the challenge.

When you register a user, the whitespace is not trimmed from the username. When you are logged in, the username does have the whitespace trimmed.

We want to log in as `"admin"`, so we'll register a user `"admin "` with a space. When we log in, the whitespace from our username will be
trimmed, and we'll be logged in as `"admin"` without the space. 


# Potential Breakage
> Potential places the challenge could break (not applicable to all challenges)

There are only so many varitions on the admin username that will work, so we're going to reset the database every 60s. This should 
make it so that teams should have no problems solving.
