import random

key = random.randint(1, 25)
LETTERS = " !@#$%^&*()1234567890QWERTYUIOPASDFGHJKLZXCVBNM \
            qwertyuiopasdfghjklzxcvbnm,./;[]\<>?:|~`.+"


def caesarCipher(sequence, key, mode="encrypt"):
    cipherText = ""
    for symbol in sequence:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode == "encrypt":
                num = num + key
            elif mode == "decrypt":
                num = num - key

            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            cipherText = cipherText + LETTERS[num]
        else:
            cipherText = cipherText + symbol

    return cipherText


def main():
    # local()

    plainText = input("please input your plain text : ")
    key = int(input("please input your key : "))
    print("cipher : ", caesarCipher(plainText, key, mode="encrypt"))


if __name__ == '__main__':
    main()
