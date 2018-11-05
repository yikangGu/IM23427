import numpy as np
import bitarray as ba
import time

PLAINTEXT = "security"
KEY = "science"

KEYPC1 = np.array((56, 48, 40, 32, 24, 16,  8,  0, 
                   57, 49, 41, 33, 25, 17,  9,  1, 
                   58, 50, 42, 34, 26, 18, 10,  2, 
                   59, 51, 43, 35, 62, 54, 46, 38, 
                   30, 22, 14,  6, 61, 53, 45, 37, 
                   29, 21, 13,  5, 60, 52, 44, 36, 
                   28, 20, 12,  4, 27, 19, 11,  3))

KEYPC2 = np.array((13, 16, 10, 23,  0,  4,
                    2, 27, 14,  5, 20,  9,
                   22, 18, 11,  3, 25,  7,
                   15,  6, 26, 19, 12,  1,
                   40, 44, 30, 36, 46, 54,
                   29, 39, 50, 44, 32, 47,
                   43, 48, 38, 55, 33, 52,
                   45, 41, 49, 35, 38, 31))

INPUTPERMUTATION = np.array((57, 49, 41, 33, 25, 17,  9,  1,
                             59, 51, 43, 35, 27, 19, 11,  3,
                             61, 53, 45, 37, 29, 21, 13,  5,
                             63, 55, 47, 39, 31, 23, 15,  7,
                             56, 48, 40, 32, 24, 16,  8,  0,
                             58, 50, 42, 34, 26, 18, 10,  2,
                             60, 52, 44, 36, 28, 20, 12,  4,
                             62, 54, 46, 38, 30, 22, 14,  6))

OUTPUTPERMUTATION = np.array((39,  7, 47, 15, 55, 23, 63, 31,
                              38,  6, 46, 14, 54, 22, 62, 30,
                              37,  5, 45, 13, 53, 21, 61, 29,
                              36,  4, 44, 12, 52, 20, 60, 28,
                              35,  3, 43, 11, 51, 19, 59, 27,
                              34,  2, 42, 10, 50, 18, 58, 26,
                              33,  1, 41,  9, 49, 17, 57, 25,
                              32,  0, 40,  8, 48, 16, 56, 24))

EPERMUTATION = np.array((31,  0,  1,  2,  3,  4,
                          3,  4,  5,  6,  7,  8,
                          7,  8,  9, 10, 11, 12,
                         11, 12, 13, 14, 15, 16,
                         15, 16, 17, 18, 19, 20,
                         19, 20, 21, 22, 23, 24,
                         23, 24, 25, 26, 27, 28,
                         27, 28, 29, 30, 31,  0))

PYIELD = np.array((15,  6, 19, 20, 28, 11, 27, 16,
                    0, 14, 22, 25,  4, 17, 30,  9,
                    1,  7, 23, 13, 31, 26,  2,  8,
                   18, 12, 29,  5, 21, 10,  3, 24))

SHIFTS = np.array((-1, -1, -2, -2, -2, -2, -2, -2, -1, -2, -2, -2, -2, -2, -2, -1))

SBOX = np.array((((14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7),
                  ( 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8),
                  ( 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0),
                  (15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13)),
                 ((15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10),
                  ( 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5),
                  ( 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15),
                  (13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9)),
                 ((10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8),
                  (13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1),
                  (13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7),
                  ( 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12)),
                 (( 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15),
                  (13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9),
                  (10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4),
                  ( 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14)),
                 (( 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9),
                  (14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6),
                  ( 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14),
                  (11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3)),
                 ((12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11),
                  (10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8),
                  ( 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6),
                  ( 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13)),
                 (( 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1),
                  (13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6),
                  ( 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2),
                  ( 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12)),
                 ((13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7),
                  ( 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2),
                  ( 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8),
                  ( 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11))))


def init(plain_text, key):

    plainTextBits = ''.join(
        list(('0'+bin(ord(alpha))[2:] for alpha in plain_text)))
    plainText_nparray = np.fromstring(ba.bitarray(plainTextBits).unpack(), dtype=bool)

    keyBits = ''.join(
        list(('0'+bin(ord(alpha))[2:] for alpha in key)))
    key_nparray = np.fromstring(ba.bitarray(keyBits).unpack(), dtype=bool)

    return plainText_nparray, key_nparray


def IP(array):

    ip = np.zeros(64, np.int8)
    for i in range(64):
        ip[i] = array[INPUTPERMUTATION[i]]

    return ip


def FP(array):

    fp = np.zeros(64, np.int8)
    for i in range(64):
        fp[i] = array[OUTPUTPERMUTATION[i]]

    return fp


def oddCodeCheck(array):

    shift = np.zeros(64, np.int8)
    sumCol = 0

    for i in range(64):
        if i % 8 == 7:
            shift[i] = not (sumCol % 2)
            sumCol = 0
        else:
            bit = array[i - int(i / 8)]
            shift[i] = bit
            sumCol = sumCol + bit

    return shift


def KP(array):

    kp = np.zeros(56, np.int8)
    for i in range(56):
        kp[i] = array[KEYPC1[i]]

    return kp


def genKey(key):

    kp = KP(oddCodeCheck(key))
    keyTable = np.zeros(16, dtype=object)

    upperKP = kp[:28]
    lowerKP = kp[28:]

    for i in range(16):
        upperKP = np.roll(upperKP, SHIFTS[i])
        lowerKP = np.roll(lowerKP, SHIFTS[i])

        cp = np.concatenate((upperKP, lowerKP), axis=None)

        ki = np.zeros(48, np.int8)
        for j in range(48):
            ki[j] = cp[KEYPC2[j]]

        keyTable[i] = ki

    return keyTable


def EP(array):

    ep = np.zeros(48, np.int8)
    for i in range(48):
        ep[i] = array[EPERMUTATION[i]]

    return ep


def sbox(i, j, sboxi):
    return SBOX[sboxi][i][j]


def PP(array):
    """
    P permutaion

    """

    pp = np.zeros(32, np.int8)
    for i in range(32):
        pp[i] = array[PYIELD[i]]

    return pp


def feistel(array, ki):

    p = np.zeros(32, np.int8)
    ep = EP(array)
    xor = np.logical_xor(ep, ki)

    for index in range(8):
        bits = xor[index*6: index*6+6]

        # e.g 110011
        # i = 1    1 = 1*2 + 1 = 3
        # j =  1001  = 1*8 + 0*4 + 0*2 + 1 = 9
        i = bits[0]*2 + bits[5]
        j = bits[1]*8 + bits[2]*4 + bits[3]*2 + bits[4]

        num = sbox(i, j, index)

        # 13 = 1101
        #      1    = int(13 / 8) % 2
        #       1   = int(13 / 4) % 2
        #        0  = int(13 / 2) % 2
        #         1 = 13 % 2
        p[index*4] = int(num / 8) % 2
        p[index*4+1] = int(num / 4) % 2
        p[index*4+2] = int(num / 2) % 2
        p[index*4+3] = num % 2

    f = PP(p)

    return f


def DES(text, key, mode="encrypt"):
    '''
    Data Encryption Standard

    '''
    # global L, R

    plainArray, keyArray = init(text, key)
    ip = IP(plainArray)
    keyTable = genKey(keyArray)

    L = ip[:32]  # half of initial permutation
    R = ip[32:]
    print(np.where(L, 1, 0).reshape(4, 8))
    print(np.where(R, 1, 0).reshape(4, 8))

    for i in range(16):
        R_ = R
        R = np.logical_xor(L, feistel(R, keyTable[i]))
        L = R_

        print(np.where(L, 1, 0).reshape(4, 8))
        print(np.where(R, 1, 0).reshape(4, 8))

    c = np.concatenate((L, R), axis=None)
    fp = FP(c)

    return fp


def main():
    # For debug
    start_timer = time.time()
    # times = 1000
    times = 1
    for loop in range(times):

        # array = np.arange(16)
        chiper = DES(PLAINTEXT, KEY).reshape(8, 8)
        print(np.where(chiper, 1, 0))

    elapsed_timer = time.time() - start_timer
    print("elapsed time : " + str(elapsed_timer))
    return 0

    plainText = input("please input your plain text : ")
    key = int(input("please input your key : "))
    print("cipher : " + DES(plainText, key))


if __name__ == '__main__':
    main()
