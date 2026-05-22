#Substitution cipher encryption program:

import random
import string

chars= " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

# print(f"chars: {chars}")
# print(f"keys: {keys}")

#ENCRYPTION:
plain_text= input("Enter the text you want to encrypt:")
cipher_text = ""

for letter in plain_text:
    index= chars.index(letter)
    cipher_text += keys[index]

print(f"Plain text: {plain_text}")
print(f"Cipher text: {cipher_text}")

#DECRYPTION:
cipher_text = input("Enter the message you want to decrypt:")
plain_text = ""

for letter in cipher_text:
    index= keys.index(letter)
    plain_text += chars[index]

print(f"Cipher text: {cipher_text}")
print(f"Plain text: {plain_text}")