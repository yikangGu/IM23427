import random

key = random.randint(1, 25)


def caesarCipher(sequence, key, mode="encrypto"):
    # 65 is the acsii code of the char "A"
    # 97 is "a"'s
    text = []
    for i in range(len(sequence)):
        if not sequence[i].isalpha():
            text.append(sequence[i])
        else:
            if ord(sequence[i]) <= 90:
                sub = 65
            else:
                sub = 97
            if mode == "encrypto":
                text.append(chr((ord(sequence[i]) - sub + key) % 26 + sub))
            if mode == "decrypto":
                text.append(chr((ord(sequence[i]) - sub - key) % 26 + sub))
    return "".join(text)


def main():
    text = "E:/Users/DELL/Anaconda3/envs/ame/python.exe\
    f:/Privacy/ProgramFile/Github/Cryptology/Symmetrical/Classic\
    /caesarCipher/src/caesarCipher.py"

    print("key : " + str(key))
    print("plainText : " + text)
    encryptoText = caesarCipher(text, key, mode="encrypto")
    print("encryptoText : " + encryptoText)
    decryptoText = caesarCipher(encryptoText, key, mode="decrypto")
    print("decryptoText : " + decryptoText)


if __name__ == '__main__':
    main()
