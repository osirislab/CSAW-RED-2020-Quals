# Description

This challenge involves a chosen plaintext attack on AES running in Output Feedback (OFB) Mode. The problem with the 
`server.py` code is that the server keeps reusing the same IV every time a block of text is encrypted. Under OFB mode,
that means that the same output stream is XORed with the plaintext every time to get the ciphertext. So, an attacker
who can choose the plaintext to encrypt can get the output stream by XORing the chosen plaintext with the resulting
ciphertext, and then decrypt any ciphertext by XORing it with the output stream. The solver takes this approach.

# TODO

Just needs to be tested once it's running in CTFd.
