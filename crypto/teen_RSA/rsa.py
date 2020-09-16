from Crypto.Util.number import long_to_bytes
'''
flag = "flag{where_did_my_primes_go?}"
p = getPrime(1024)
q = getPrime(1024)
e = 3
m = bytes_to_long(flag.encode("utf-8"))

n = p * q
c = pow(m, e, n)

print("e:" + str(e))
print("c:" + str(c))
'''

e = 3
c = 21054947296948912186250291623999881612177917867294620912940663265128767538390407246183135081940602148334924270226808672133409885425114817372307202073496919198495962536909357503213718449515958555968598380737125

def find_invpow(x, n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1
#https://stackoverflow.com/questions/55436001/cube-root-of-a-very-large-number-using-only-math-library


print(long_to_bytes(find_invpow(c, e)))