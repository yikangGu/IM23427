import bitarray as ba
import numpy
import time

PLAINTEXT = "security"

start_timer1 = time.time()
for i in range(1000000):
    bin(ord(PLAINTEXT[0]))[2:]
print(bin(ord(PLAINTEXT[0]))[2:])
elapsed_timer1 = time.time() - start_timer1
print("elapsed time 1 : " + str(elapsed_timer1))

start_timer2 = time.time()
for i in range(1000000):
    "{0:b}".format(ord(PLAINTEXT[0]))
print("{0:b}".format(ord(PLAINTEXT[0])))
elapsed_timer2 = time.time() - start_timer2
print("elapsed time 2 : " + str(elapsed_timer2))

start_timer3 = time.time()
for i in range(1000000):
    str(bin(ord(PLAINTEXT[0])))[2:]
print(str(bin(ord(PLAINTEXT[0])))[2:])
elapsed_timer3 = time.time() - start_timer3
print("elapsed time 3 : " + str(elapsed_timer3))

start_timer4 = time.time()
for i in range(1000000):
    str(bin(ord(PLAINTEXT[0]))[2:])
print(str(bin(ord(PLAINTEXT[0]))[2:]))
elapsed_timer4 = time.time() - start_timer4
print("elapsed time 4 : " + str(elapsed_timer4))
