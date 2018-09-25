import random

key = random.randint(1, 25)
alphabet = "abcdefghijklmnopqrstuvwxyz"
symbolIdx = []


def isAlphabet(squence):
    symbolIdx = [i for i in range(len(squence))]


def Encrypto(sequence, key):
    cryptotext = [ord(i) + key for i in sequence]


def main():
    k = "a"
    print(ord("a"), ord("A"), ord("z"), ord("Z"))
    print()

if __name__ == '__main__':
    main()
