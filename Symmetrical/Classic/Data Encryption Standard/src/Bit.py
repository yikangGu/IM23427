import bitarray

PLAINTEXT = "security"
bits = bin(ord(PLAINTEXT[0]))
print(bits)
# print(bin(int(bits, 2) >> 1))

bitarray.test()
