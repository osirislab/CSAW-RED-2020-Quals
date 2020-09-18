
# Paper scissors rock cipher
# 1) Convert flag to ASCII numbers
# 2) Convert ASCII numbers to base 3
# 3) Put a separator between each number


import os

directory_stem = "~/Documents/NYU/CSAW2020/RED/crypto/RPS/images"


def base10to3(x):
    digits = []
    while x:
        digits.append(int(x % 3))
        x = int(x / 3)
    #print(str(digits))
    digits.reverse()
    #print(str(digits))
    output = ''
    for digit in digits:
    	output+=str(digit)
    return output

#flag = "flag{r0ck_p4p3r_5c1550r5_FTW}"
# Keeping the flag short because parsing the symbols in the PDF could otherwise be frustrating
flag = "flag{n1c3_RPS_sk1llz}"

code = []
for letter in flag:
	code += base10to3(ord(letter))
	code += '|'

#print(base10to3(1))
#print(base10to3(5))
#print(base10to3(20))
print(''.join(code))
print(str(len(code)))
for index in range(len(code)):
	letter = code[index]
	if letter == "0":
		cmdstring = "cp " + directory_stem +"/icons/rock.jpg" + " " + directory_stem + "/codeimages/" + str(index) + ".jpg"
		print(cmdstring)
		os.system(cmdstring)
		#print(str("Rock " + str(index) + " "))
	elif letter == "1":
		cmdstring = "cp " + directory_stem +"/icons/paper.jpg" + " " + directory_stem + "/codeimages/" + str(index) + ".jpg"
		print(cmdstring)
		os.system(cmdstring)
		#os.system("cp " + directory_stem +"/icons/paper.jpg" + " " + directory_stem + "/codeimages" + str(index) + ".jpg")
		#print(str("Paper " + str(index) + " "))
	elif letter == "2":
		cmdstring = "cp " + directory_stem +"/icons/scissors.jpg" + " " + directory_stem + "/codeimages/" + str(index) + ".jpg"
		print(cmdstring)
		os.system(cmdstring)
		#os.system("cp " + directory_stem +"/icons/scissors.jpg" + " " + directory_stem + "/codeimages" + str(index) + ".jpg")
		#print(str("Scissors " + str(index) + " "))
	else:
		cmdstring = "cp " + directory_stem +"/icons/stop.jpg" + " " + directory_stem + "/codeimages/" + str(index) + ".jpg"
		print(cmdstring)
		os.system(cmdstring)
		#os.system("cp " + directory_stem +"/icons/stop.jpg" + " " + directory_stem + "/codeimages" + str(index) + ".jpg")
		#print(str("Stop " + str(index) + " "))

#os.system("ls -ld /home")
# Test run: make a pdf with paper, scissors, rock, thumbs-up, twice. See what it looks like. 

