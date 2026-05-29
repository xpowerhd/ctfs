import string
import random

cipher_text = open('flag.txt','r').read().strip()

while True:
	xored = ""

	res = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
	rand_str = str(res) * 16
	print("Random string: " + rand_str)
	
	for i in range(0,len(cipher_text)):
		xored += chr(ord(cipher_text[i]) ^ ord(rand_str[i%len(rand_str)]))

	if "THM{" in xored:
		print("xored: " + xored)
		answear = input("Is that right: ")
		read
		break


print("The result of encrypting: " + cipher_text)
print("Leght: " + str(len(cipher_text)))
