from Crypto.Util.number import bytes_to_long, getPrime, inverse, long_to_bytes

flag = "flag{really_s1ck_algor1thm}"
p = getPrime(1024)
q = getPrime(1024)
e = 65537
m = bytes_to_long(flag.encode("utf-8"))

n = p * q
c = pow(m, e, n)

print("p:" + str(p))
print("q:" + str(q))
print("e:" + str(e))
print("c:" + str(c))

#phi = (p - 1) * (q - 1)
#d = inverse(e, phi)
#print(long_to_bytes(pow(c, d, n)))