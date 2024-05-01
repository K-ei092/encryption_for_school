'''
Модуль представляет 3 класса для шифрования строковых значений
шифрами Цезаря, Виженера и простой табличной перестановкой
'''


from abc import ABCMeta, abstractmethod


class Cryptography(metaclass=ABCMeta):

    LETTERS_CEASER_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    LETTERS_CEASER_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_CEASER_SPECIAL = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789'''
    LETTERS_VIGENERE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass



class CeaserCipher(Cryptography):

    def __init__(self, message: str, step: int):
        self.__message = message.upper().replace(' ', '')
        self.__step = step
        self.__result_encrypt = ''
        self.__result_decrypt = ''

    def encrypt(self) -> str:
        for letter in self.__message:
            if letter in self.LETTERS_CEASER_RU:
                place = self.LETTERS_CEASER_RU.find(letter)
                new_place = place + self.__step
                if new_place < 33:
                    self.__result_encrypt += self.LETTERS_CEASER_RU[new_place]
                else:
                    new_place = new_place % 33
                    self.__result_encrypt += self.LETTERS_CEASER_RU[new_place]
            elif letter in self.LETTERS_CEASER_EU:
                place = self.LETTERS_CEASER_EU.find(letter)
                new_place = place + self.__step
                if new_place < 26:
                    self.__result_encrypt += self.LETTERS_CEASER_EU[new_place]
                else:
                    new_place = new_place % 26
                    self.__result_encrypt += self.LETTERS_CEASER_EU[new_place]
            elif letter in self.LETTERS_CEASER_SPECIAL:
                place = self.LETTERS_CEASER_SPECIAL.find(letter)
                new_place = place + self.__step
                if new_place < 42:
                    self.__result_encrypt += self.LETTERS_CEASER_SPECIAL[new_place]
                else:
                    new_place = new_place % 42
                    self.__result_encrypt += self.LETTERS_CEASER_SPECIAL[new_place]
            else:
                self.__result_encrypt += letter

        return self.__result_encrypt

    def decrypt(self) -> str:
        for letter in self.__message:
            if letter in self.LETTERS_CEASER_RU:
                place = self.LETTERS_CEASER_RU.find(letter)
                new_place = place - self.__step
                if new_place >= 0:
                    self.__result_decrypt += self.LETTERS_CEASER_RU[new_place]
                else:
                    new_place = (33 - (abs(new_place) % 33)) % 33
                    self.__result_decrypt += self.LETTERS_CEASER_RU[new_place]
            elif letter in self.LETTERS_CEASER_EU:
                place = self.LETTERS_CEASER_EU.find(letter)
                new_place = place - self.__step
                if new_place >= 0:
                    self.__result_decrypt += self.LETTERS_CEASER_EU[new_place]
                else:
                    new_place = (26 - (abs(new_place) % 26)) % 26
                    self.__result_decrypt += self.LETTERS_CEASER_EU[new_place]
            elif letter in self.LETTERS_CEASER_SPECIAL:
                place = self.LETTERS_CEASER_SPECIAL.find(letter)
                new_place = place - self.__step
                if new_place >= 0:
                    self.__result_decrypt += self.LETTERS_CEASER_SPECIAL[new_place]
                else:
                    new_place = (42 - (abs(new_place) % 42)) % 42
                    self.__result_decrypt += self.LETTERS_CEASER_SPECIAL[new_place]
            else:
                self.__result_decrypt += letter

        return self.__result_decrypt



class VigenereCipher(Cryptography):

    def __init__(self, message: str, key: str):
        self.__message = message.upper().replace(' ', '')
        self.__key = key.upper()
        self.__result_encrypt = []
        self.__result_decrypt = []
        self.__keyIndex = 0

    def encrypt(self) -> str:
        for letter in self.__message:
            num = self.LETTERS_VIGENERE.find(letter.upper())
            if num != -1:
                num += self.LETTERS_VIGENERE.find(self.__key[self.__keyIndex])
                num %= len(self.LETTERS_VIGENERE)
                if letter.isupper():
                    self.__result_encrypt.append(self.LETTERS_VIGENERE[num])
                elif letter.islower():
                    self.__result_encrypt.append(self.LETTERS_VIGENERE[num].lower())
                self.__keyIndex += 1
                if self.__keyIndex == len(self.__key):
                    self.__keyIndex = 0
            else:
                self.__result_encrypt.append(letter)

        return ''.join(self.__result_encrypt).replace(' ', '').upper()

    def decrypt(self) -> str:
        for letter in self.__message:
            num = self.LETTERS_VIGENERE.find(letter.upper())
            if num != -1:
                num -= self.LETTERS_VIGENERE.find(self.__key[self.__keyIndex])
                num %= len(self.LETTERS_VIGENERE)
                if letter.isupper():
                    self.__result_decrypt.append(self.LETTERS_VIGENERE[num])
                elif letter.islower():
                    self.__result_decrypt.append(self.LETTERS_VIGENERE[num].lower())
                self.__keyIndex += 1
                if self.__keyIndex == len(self.__key):
                    self.__keyIndex = 0
            else:
                self.__result_decrypt.append(letter)

        return ''.join(self.__result_decrypt).replace(' ', '').upper()



class TablePermutation(Cryptography):

    def __init__(self, message: str, key: int):
        self.__message = message.upper().replace(' ', '')
        self.__key = key
        if key > len(self.__message):
            self.__key = len(self.__message) // 2
        self.__result_encrypt = [''] * self.__key
        self.__result_decrypt = [''] * len(self.__message)
        self.__index = 0

    def encrypt(self):
        for col in range(self.__key):
            pointer = col
            while pointer < len(self.__message):
                self.__result_encrypt[col] += self.__message[pointer]
                pointer += self.__key

        return ''.join(self.__result_encrypt)

    def decrypt(self):
        for col in range(self.__key):
            pointer = col
            while pointer < len(self.__message):
                self.__result_decrypt[pointer] = self.__message[self.__index]
                self.__index += 1
                pointer += self.__key

        return ''.join(self.__result_decrypt)



if __name__ == '__main__':

    test = '''АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ__ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789'''

    ceaser = CeaserCipher(message=test, step=53)
    encrypt_text = ceaser.encrypt()
    print(encrypt_text)
    ceaser = CeaserCipher(encrypt_text, 53)
    decrypt_text = ceaser.decrypt()
    print(decrypt_text)
    print()

    vigenere = VigenereCipher(message=test, key='Mariya')
    encrypt_text = vigenere.encrypt()
    print(encrypt_text)
    vigenere = VigenereCipher(encrypt_text, 'Mariya')
    decrypt_text = vigenere.decrypt()
    print(decrypt_text)
    print()

    tab = TablePermutation(message=test, key=28)
    encrypt_text = tab.encrypt()
    print(encrypt_text)
    tab = TablePermutation(encrypt_text, 28)
    decrypt_text = tab.decrypt()
    print(decrypt_text)


