from Crypto.Util.number import bytes_to_long, getPrime, inverse, long_to_bytes

f = open("output.txt", "r")
p = int(f.readline()[2:])
q = int(f.readline()[2:])
e = int(f.readline()[2:])
c = int(f.readline()[2:])
n = p * q
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(long_to_bytes(pow(c, d, n)))