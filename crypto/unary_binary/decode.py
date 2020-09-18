
#code = "10210|11000|10121|10211|11120|11002|1211|10200|122"

ct = "10210|11000|10121|10211|11120|11002|1211|10200|1220|10112|10001|2222|10002|10112|11021|10222|1211|11000|11000|11112|11122"

ct_letters = ct.split("|")
print(ct_letters)

def base3tobase10(x):
    index = 0
    x=x[::-1]
    #print(x)
    #print(str(digits))
    #digits.reverse()
    #print(str(digits))
    output = 0
    for digit in x:
    	#print("digit = " + str(digit))
    	#print("adding " + str(int(digit)*pow(3,index)))
    	output+=int(digit)*pow(3,index)
    	index += 1
    return output

print(base3tobase10("10210"))

m = ""
for letter in ct_letters:
	m += chr(base3tobase10(letter))

print("m = " + str(m))
