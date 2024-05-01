# шифр Цезаря

alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
           'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input("Сообщение для шифровки: ").upper()  # создаем переменнную, куда запишем наше сообщение
step = int(input('Шаг шифровки: '))  # Создаем переменную с шагом шифровки

encryptMessage = ''  # создаем переменную для вывода итогового сообщения

for i in message:
    place = alfavit.find(i)    #Вычисляем места символов в списке
    new_place = place + step    #Сдвигаем символы на указанный в переменной smeshenie шаг
    if i in alfavit:
        encryptMessage += alfavit[new_place]  # Задаем значения в итог
    else:
        encryptMessage += i

result_encrypt = encryptMessage.replace(' ', '')
print(result_encrypt)


result_decrypt = ''

for i in result_encrypt:
    place = alfavit.find(i)
    new_place = place - step    # Меняем знак + на знак -
    if i in alfavit:
        result_decrypt += alfavit[new_place]
    else:
        result_decrypt += i

print(result_decrypt)



if __name__ == '__main__':
    pass
