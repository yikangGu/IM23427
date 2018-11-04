import numpy as np


def lazyFP(arrays):

    perRule = np.array([4, 0, 5, 1, 6, 2, 7, 3])
    finalPermutation = np.fliplr(arrays[perRule]).T
    return finalPermutation


def focusInputFP(arrays):
    # T(n) = O(n)
    finalPermutation = np.zeros((8, 8), np.bool)

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


def oddCodeCheck(arrays):
    shift = np.zeros((8, 8), np.int8)
    couter = 0

    for i in range(7):
        for j in range(8):
            shift[int(couter / 7), couter % 7] = arrays[i, j]
            couter = couter + 1

        shift[i, 7] = not (sum(shift[i]) % 2)

    return shift


def main():
    pass

if __name__ == '__main__':
    main()
