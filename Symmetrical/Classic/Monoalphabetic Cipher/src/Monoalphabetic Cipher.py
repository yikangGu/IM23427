from random import shuffle
randalpha  = [x for x in range(26)]
shuffle(randalpha)


def txwrite(texts, name, key=''):
    txout = ''
    for text in texts:
        txout = txout + str(text) + key + '\n'

    with open(name, 'w') as file_object:
        file_object.write(txout)
        file_object.close()


def txread(fileName):
    tx = []
    with open(fileName) as file_object:
        for line in file_object:
            tx.append(line.rstrip())
    return tx


def without_frequency():
    alphabetCounter = [0]*26

    # terminal path set to Monoalphaberic Cipher
    words = txread("data/words.txt")
    wordStr = "".join(words)
    for alphabet in wordStr:
        alphabetCounter[
            ord(alphabet)-97] = alphabetCounter[ord(alphabet)-97] + 1

    alphabetSum = sum(alphabetCounter)
    alphabetFrequency = list(map(lambda x: x/alphabetSum, alphabetCounter))
    txwrite(alphabetFrequency, 'data/alphabetFrequency.txt')


def main():
    text = "E:/Users/DELL/Anaconda3/envs/ame/python.exe\
    f:/Privacy/ProgramFile/Github/Cryptology/Symmetrical/Classic\
    /Monoalphabetic\ Cipher/src/Monoalphabetic\ Cipher.py"

    # without_frequency()

    txAlphaCounter = [0]*26
    alphabetFrequency = txread("data/alphabetFrequency.txt")
    newtx = "".join(list(filter(lambda x: x.isalpha(), text.lower())))

    encryptoText = ''
    for alphabet in newtx:
        ordAlpha = ord(alphabet)
        txAlphaCounter[
            ordAlpha-97] = txAlphaCounter[ordAlpha-97] + 1
        encryptoText = encryptoText + chr(97 + ((ordAlpha + randalpha[ordAlpha-97]) % 26))

    txAlphaSum = sum(txAlphaCounter)
    txAlphaFrequency = list(map(lambda x: x/txAlphaSum, txAlphaCounter))

    encryptoCounter = [0]*26
    for alphabet in encryptoText:
        ordAlpha = ord(alphabet)
        encryptoCounter[
            ordAlpha-97] = encryptoCounter[ordAlpha-97] + 1
    
    encryptoAlphaSum = sum(encryptoCounter)
    encryptoAlphaFrequency = list(map(lambda x: x/encryptoAlphaSum, encryptoCounter))

    print(randalpha)
    print(encryptoText)
    print(alphabetFrequency)
    print(txAlphaFrequency)
    print(encryptoAlphaFrequency)


if __name__ == '__main__':
    main()
