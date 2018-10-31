import numpy as np
import bitarray as ba

PLAINTEXT = "security"
KEY = "science"
KEYPERMUTATION = np.array([[13, 16, 10, 23,  0,  4],
                           [ 2, 27, 14,  5, 20,  9],
                           [22, 18, 11,  3, 25,  7],
                           [15,  6, 26, 19, 12,  1],
                           [40, 44, 30, 36, 46, 54],
                           [29, 39, 50, 44, 32, 47],
                           [43, 48, 38, 55, 33, 52],
                           [45, 41, 49, 35, 38, 31]])


def init(plain_text, key):
    bits = bin(ord(plain_text[0]))[2:]
    plainText_nparray = np.insert(
        np.fromstring(ba.bitarray(bits).unpack(), dtype=bool), 0, 0)

    for alpha in plain_text[1:]:
        bits = bin(ord(alpha))[2:]
        npbinary = np.insert(
            np.fromstring(ba.bitarray(bits).unpack(), dtype=bool), 0, 0)
        plainText_nparray = np.vstack([plainText_nparray, npbinary])

    bits = bin(ord(key[0]))[2:]
    np.fromstring(ba.bitarray(bits).unpack(), dtype=bool)
    key_nparray = np.insert(
        np.fromstring(ba.bitarray(bits).unpack(), dtype=bool), 0, 0)

    for alpha in key[1:]:
        bits = bin(ord(alpha))[2:]
        npbinary = np.insert(
            np.fromstring(ba.bitarray(bits).unpack(), dtype=bool), 0, 0)
        key_nparray = np.vstack([key_nparray, npbinary])

    return plainText_nparray, key_nparray


def focusOutputFP(arrays):
    # T(n) = O(n)
    finalPermutation = np.zeros((8, 8), np.bool)

    for i in range(8):
        for j in range(4):

            finalPermutation[i, j*2+1] = arrays[j, 7-i]
            finalPermutation[i, j*2] = arrays[j+4, 7-i]

    return finalPermutation


def IP(arrays):
    # T(n) = O(n)
    initialPermutation = np.zeros((8, 8), np.bool)

    for j in range(8):
        for i in range(4):

            initialPermutation[i, 7-j] = arrays[j, i*2+1]
            initialPermutation[i+4, 7-j] = arrays[j, i*2]

    return initialPermutation


def oddCodeCheck(arrays):
    # it is beautiful
    shift = np.zeros((8, 7), np.bool)
    times = 0

    for i in range(7):
        for j in range(8):
            shift[int(times / 7), times % 7] = arrays[i, j]
            times = times + 1

        expansion = np.array([np.append(
            shift[i], not sum(shift[i]) % 2) for i in range(8)])

    return expansion


def KP(arrays):
    # T(n) = O(n)
    keyPermutation = np.zeros((7, 8), np.bool)

    for j in range(8):
        for i in range(7):
            keyPermutation[i, 7-j] = arrays[j, i]

    return keyPermutation


def genKey(key):
    # key = np.arange(1, 65).reshape(8, 8)
    keyPermutation = KP(oddCodeCheck(key))
    shiftKP = np.reshape(keyPermutation, -1)

    upperKP = np.roll(shiftKP[:28], -1)
    lowerKP = np.roll(shiftKP[28:], -1)

    compactPermutation = np.concatenate((upperKP, lowerKP), axis=None)

    ki = np.zeros((8, 6), np.int8)
    for i in range(8):
        for j in range(6):
            ki[i, j] = compactPermutation[KEYPERMUTATION[i, j]]

    return ki


def DES(plain_text, key, mode="encrypt"):
    #
    plainText_nparray, key_nparray = init(plain_text, key)
    initialPermutation = IP(plainText_nparray)

    upper = initialPermutation[:4]
    lower = initialPermutation[4:]

    key1 = genKey(key_nparray)
    print(key1)
    pass


def main():
    # For debug
    # arrays = np.arange(64).reshape(8, 8)
    # plainText_nparray, key_nparray = init(PLAINTEXT, KEY)

    DES(PLAINTEXT, KEY)
    return 0

    plainText = input("please input your plain text : ")
    key = int(input("please input your key : "))
    print("cipher : " + DES(plainText, key))


if __name__ == '__main__':
    main()
