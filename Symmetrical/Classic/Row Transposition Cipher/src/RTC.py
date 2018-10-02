import numpy as np


def RTC(tx, key):
    keyStr = str(key)
    keyLenth = len(keyStr)
    splitTx = [tx[n * 5: (n + 1) * 5] for n in range(int(len(tx) / keyLenth))]
    cipherTx = ''.join([j[int(i) - 1] for i in keyStr for j in splitTx])
    return cipherTx


def main():
    plainText = 'attackpostponed'
    key = 41532
    RTC(plainText, key)

if __name__ == '__main__':
    main()