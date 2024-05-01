def encrypt(text, key):
    text = text.replace(" ", "")  # Удаляем пробелы из текста
    encrypted_text = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(text):
            encrypted_text[col] += text[pointer]
            pointer += key
    return ''.join(encrypted_text)


def decrypt(text, key):
    decrypted_text = [''] * len(text)
    index = 0
    for col in range(key):
        pointer = col
        while pointer < len(text):
            decrypted_text[pointer] = text[index]
            index += 1
            pointer += key
    return ''.join(decrypted_text)


def main():
    # text = input("Введите текст для шифрования: ")
    # key = int(input("Введите ключ (целое число от 2, но не более длины текста): "))

    test_text = '''АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ__ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789'''
    key = 103
    print(len(test_text))

    encrypted_text = encrypt(test_text, key)
    print(f"Зашифрованный текст: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key)
    print(f"Расшифрованный текст: {decrypted_text}")


if __name__ == "__main__":
    main()