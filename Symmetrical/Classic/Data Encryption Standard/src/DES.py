import numpy as np

PLAINTEXT = "security"
KEY = "science"


def lazyFP(arrays):
    # Debug
    # arrays = np.arange(64).reshape(8, 8)

    perRule = np.array([4, 0, 5, 1, 6, 2, 7, 3])
    finalPermutation = np.fliplr(arrays[perRule]).T
    return finalPermutation


def FP(arrays):
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


def IP(arrays):
    # T(n) = O(n)
    initialPermutation = np.zeros((8, 8), np.int8)

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
    return initialPermutation


def DES(arrays, key, mode="encrypt"):
    pass


def main():
    arrays = np.arange(1, 65).reshape(8, 8)
    finalPermutation = FP(arrays)
    print(arrays)
    print(finalPermutation)

    return 0

    plainText = input("please input your plain text : ")
    key = int(input("please input your key : "))
    print("cipher : " + DES(plainText, key))


if __name__ == '__main__':
    main()
