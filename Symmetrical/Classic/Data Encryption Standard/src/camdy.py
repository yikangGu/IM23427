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


def main():
    pass

if __name__ == '__main__':
    main()
