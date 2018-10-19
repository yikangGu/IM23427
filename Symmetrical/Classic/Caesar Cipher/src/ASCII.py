import random

key = random.randint(1, 25)


def caesarCipher(sequence, key, mode="encrypt"):
    # 65 is the acsii code of the char "A"
    # 97 is "a"'s

    cipherText = ""
    for i in range(len(sequence)):
        if not sequence[i].isalpha():
            cipherText = cipherText + sequence[i]
        else:
            if ord(sequence[i]) <= 90:
                sub = 65
            else:
                sub = 97

            if mode == "encrypt":
                cipherText = cipherText + chr((
                    ord(sequence[i]) - sub + key) % 26 + sub)

            if mode == "decrypt":
                cipherText = cipherText + chr((
                    ord(sequence[i]) - sub - key) % 26 + sub)

    return cipherText


def local():
    text = "E:/Users/DELL/Anaconda3/envs/ame/python.exe\
    f:/Privacy/ProgramFile/Github/Cryptology/Symmetrical/Classic\
    /caesarCipher/src/caesarCipher.py"

    print("key : " + str(key))
    print("plainText : " + text)
    encryptoText = caesarCipher(text, key, mode="encrypt")
    print("encryptoText : " + encryptoText)
    decryptoText = caesarCipher(encryptoText, key, mode="decrypt")
    print("decryptoText : " + decryptoText)


def main():
    # local()

    plainText = input("please input your plain text : ")
    key = int(input("please input your key : "))
    print("cipher : ", caesarCipher(plainText, key, mode="encrypt"))


if __name__ == '__main__':
    main()
