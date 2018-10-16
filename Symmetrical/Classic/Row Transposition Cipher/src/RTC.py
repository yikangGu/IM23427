import numpy as np

# OMG! it's hard to read.


def RTC(sequence, key):
    keyStr = str(key)
    keyLenth = len(keyStr)

    mod = -1
    while(True):
        mod = len(sequence) % keyLenth
        if not mod == 0:
            sequence = sequence + " "
        else:
            break

    # print(len(sequence), keyLenth, mod)
    # print("[" + sequence + "]")
    # print(int(len(sequence) / keyLenth))

    splitText = [
        sequence
        [
            n * keyLenth: (n + 1) * keyLenth
        ]
        for n in range
        (
            int(len(sequence) / keyLenth)
        )
    ]

    cipherText = ''.join(
        [
            j[int(i) - 1]
            for i in keyStr
            for j in splitText
            if j[int(i) - 1].isalpha()
        ]
    )
    return cipherText


def local():
    plainText = 'attackpostponed'
    key = 4
    print(RTC(plainText, key))


def main():

    plainText = input("please input your plain text : ")
    key = int(input("please input your key : "))
    print("cipher : " + RTC(plainText, key))

if __name__ == '__main__':
    main()
