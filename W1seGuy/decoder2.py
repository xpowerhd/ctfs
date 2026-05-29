import string
import random
import itertools

cipher_text = open('flag.txt','r').read().strip()
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits


for combo in itertools.product(charset, repeat=2):
    xored = ""

    # Create 80-char pseudo-key by repeating the combo
    rand_str = (''.join(combo) + "bfz") * 16  # 5 * 16 = 80

    # XOR each char of the ciphertext with key
    for i in range(len(cipher_text)):
        xored += chr(ord(cipher_text[i]) ^ ord(rand_str[i % len(rand_str)]))

    print(str(combo) + ":" + rand_str + "\n")
    # Check for THM{...}
    if "THM{" in xored and "}" in xored:
        print("xored: " + xored)
        answear = input("Is that right? ")
        if answear.upper() == "YES":
            break


print("The result of encrypting: " + cipher_text)
print("Leght: " + str(len(cipher_text)))
