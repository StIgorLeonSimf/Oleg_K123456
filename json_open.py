import json

# d = {'green': 'зеленый',
#      'black': 'черный'}
#


with open('dict.json', encoding='utf-8') as file:
    d = json.load(file)

print(d)
while True:
    word = input('ВВедите слово для перевода: ')
    if word in d:
        print(f'{word} - {d[word]}')
    elif word == 'exit':
        break
    else:
        translate = input(f'ВВедите перевод для слова {word} ')
        d[word] = translate
        with open('dict.json', 'w', encoding='utf-8') as file:
            json.dump(d, file)