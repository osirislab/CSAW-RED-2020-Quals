jwt

> Category: web 
> Suggested Points: 200 
> Distribute: src/app.py

# Description

Start the challenge by vewing the web portal which has a form and a set of links. The links are to files, but access tokens (jwt's) are required to view the files. The form is used to request access tokens for files. However, if people try to request access to flag.txt the server will not allow them. By reading the source people will realize that they can request access to a file called secret.txt. The secret.txt file is used to hold the secret key used to encode the jwt's.

Once they have the secret key, they can encode their own jwt's and create one for accessing flag.txt. Once they create a jwt they can set it as their cookie and access /flag.txt

# Deployment

docker build -t <name> .
docker run -p <external_port>:5000 <name>

# Flag

`flag{jwt_t0o0oo00ooo000ookens}`

# Solution
Read source and notice that jwt's are being encoded using the key in secret.txt. Also realize that you can request a token for any file except flag.txt, meaning you can request access to secret.txt.

Requesting access to a file can is done using the form on the web portal. However it can also be done programtically by sending a post request to '/' with the payload being {'filename': 'secret.txt'}

Requesting access to secret.txt will set a cookie called jwt containing a jwt allowing access to secret.txt. You can then navigate to secret.txt using the url bar or a simple get request to '/secret.txt'

Now that you have the secret, you must encode your own jwt. Because you have source you can simply copy paste how the encoding is done (make sure to supply the correct secret and filename you wish to access). The code looks like: `jwt.encode({'filename': 'flag.txt'}, 'super_secret_k3y', algorithm='HS256')`. This is the only step that must be done programatically and can't be done though the web portal.

Once you have the jwt you can make a get request to '/flag.txt', just make sure the jwt is set as a cookie named jwt. This can be done all through the browser or programatically. 

# Potential Breakage
challenge getting hit too hard. fix: increase gunicorn workers in Dockerfile
