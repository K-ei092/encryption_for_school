LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()
    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0

        else:
            translated.append(symbol)

    result = ''.join(translated).replace(' ', '').upper()


    return result

def main(myMode):

    if myMode == 'encrypt':
        return encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        return decryptMessage(myKey, myMessage)


if __name__ == "__main__":

    myMessage = input("Введите текст для шифрования (русские или английские буквы: ")
    myKey = input("Введите ключ (слово): ")

    myMode = 'encrypt'

    myMessage_encrypt = main(myMode)
    print(myMessage_encrypt)

    myMessage = myMessage_encrypt
    myMode = 'decrypt'

    myMessage_decrypt = main(myMode)
    print(myMessage_decrypt)