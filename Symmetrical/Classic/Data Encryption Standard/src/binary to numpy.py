import numpy as np
import bitarray as ba
import time

PLAINTEXT = "security"


def toByte(bin_string):
    byte_string = b''
    for i in bin_string:
        if i == "1":
            byte_string += b"\xff"
        else:
            byte_string += b"\x00"
    return byte_string

start_timer1 = time.time()
binary = bin(ord(PLAINTEXT[0]))[2:]
for i in range(100000):
    npbinary = np.fromstring(ba.bitarray(binary).unpack(), dtype=bool)
elapsed_timer1 = time.time() - start_timer1
print("elapsed time 1 : " + str(elapsed_timer1))
print(repr(npbinary))

start_timer2 = time.time()
binary = bin(ord(PLAINTEXT[0]))[2:]
for i in range(100000):
    npbinary = np.fromstring(toByte(binary), dtype=bool)
elapsed_timer2 = time.time() - start_timer2
print("elapsed time 2 : " + str(elapsed_timer2))
print(repr(npbinary))
