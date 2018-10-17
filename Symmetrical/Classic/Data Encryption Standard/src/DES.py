import numpy as np

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


def lazyFP(arrays):
    # Debug
    # arrays = np.arange(64).reshape(8, 8)

    perRule = np.array([4, 0, 5, 1, 6, 2, 7, 3])
    finalPermutation = np.fliplr(arrays[perRule]).T
    return finalPermutation


def focusInputFP(arrays):
    # T(n) = O(n)
    finalPermutation = np.zeros((8, 8), np.int8)

    j = -1
    for row in arrays[:4]:
        i = 7
        j = j + 2
        for bit in row:
            finalPermutation[i, j] = bit
            i = i - 1

    j = -2
    for row in arrays[4:]:
        i = 7
        j = j + 2
        for bit in row:
            finalPermutation[i, j] = bit
            i = i - 1
    return finalPermutation


def focusOutputFP(arrays):
    # T(n) = O(n)
    finalPermutation = np.zeros((8, 8), np.int8)

    for i in range(8):
        for j in range(4):

            finalPermutation[i, j*2+1] = arrays[j, 7-i]
            finalPermutation[i, j*2] = arrays[j+4, 7-i]

    return finalPermutation


def IP(arrays):
    # T(n) = O(n)
    initialPermutation = np.zeros((8, 8), np.int8)

    for j in range(8):
        for i in range(4):

            initialPermutation[i, 7-j] = arrays[j, i*2+1]
            initialPermutation[i+4, 7-j] = arrays[j, i*2]

    return initialPermutation


def KP(arrays):
    # T(n) = O(n)
    keyPermutation = np.zeros((7, 8), np.int8)

    for j in range(8):
        for i in range(7):
            keyPermutation[i, 7-j] = arrays[j, i]

    return keyPermutation


def genKey(key):
    # key = np.arange(1, 65).reshape(8, 8)
    keyPermutation = KP(key)
    shiftKP = np.reshape(keyPermutation, -1)

    upperKP = np.roll(shiftKP[:28], -1)
    lowerKP = np.roll(shiftKP[28:], -1)

    compactPermutation = np.concatenate((upperKP, lowerKP), axis=None)

    ki = np.zeros((8, 6), np.int8)
    for i in range(8):
        for j in range(6):
            ki[i, j] = compactPermutation[KEYPERMUTATION[i, j]]

    return ki


def DES(arrays, key, mode="encrypt"):
    #
    null = np.arange(1, 65).reshape(8, 8)
    initialPermutation = IP(null)

    upper = initialPermutation[:4]
    lower = initialPermutation[4:]

    genKey(lower)
    pass


def main():
    arrays = np.arange(1, 65).reshape(8, 8)
    print(genKey(arrays))
    return 0

    plainText = input("please input your plain text : ")
    key = int(input("please input your key : "))
    print("cipher : " + DES(plainText, key))


if __name__ == '__main__':
    main()
