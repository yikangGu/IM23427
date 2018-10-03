import numpy as np


def RTC(tx, key):
    keyStr = str(key)
    keyLenth = len(keyStr)
    splitTx = [tx[n * keyLenth: (n + 1) * keyLenth] for n in range(
        int(len(tx) / keyLenth))]
    cipherTx = ''.join([j[int(i) - 1] for i in keyStr for j in splitTx])
    return cipherTx


def main():
    plainText = 'attackpostponed'
    key = 213
    print(RTC(plainText, key))

if __name__ == '__main__':
    main()
