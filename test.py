import crypto.alphabets
import crypto.ciphers

a = crypto.alphabets.EnglishAlphabet()

print(a)

c = crypto.ciphers.CaesarShift(a)

ciphertext = c.encrypt(10, 'Hello, world!')
print(ciphertext)
print(c.decrypt(10, ciphertext))
