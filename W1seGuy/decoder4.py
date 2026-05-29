import string
import random

cipher_text = open('flag.txt','r').read().strip()


xored = ""

rand_str = "THM{" * 20
print("Random string: " + rand_str)

for i in range(0,len(cipher_text)):
	xored += chr(ord(cipher_text[i]) ^ ord(rand_str[i%len(rand_str)]))

print("xored: " + xored)

chunks = []
i = 0
while i < len(xored):
    chunks.append(xored[i:i+4])
    i += 4
print(chunks)

for i in range(0,len(cipher_text),4):
	print("xored: " + xored[i] + xored[i+1] + xored[i+2] + xored[i+3])
print("The result of encrypting: " + cipher_text)
print("Leght: " + str(len(cipher_text)))
