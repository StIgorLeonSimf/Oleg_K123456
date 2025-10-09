with open('text1.txt', encoding='utf-8') as f:
    s = f.read()
    key = input('Введите ключ шифрования: ')
    secret = ''
    for i in s:
        code = ord(i) + int(key)
        symbol = chr(code)
        secret += symbol
    print('Текст зашифрован!!')
with open('code.txt', 'w', encoding='utf-8') as f:
    f.write(secret)
print('Файл для отправки "code.txt" сформирован')