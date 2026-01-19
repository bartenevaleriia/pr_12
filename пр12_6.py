word = input('Введите слово: ')

word_list = list(word)
reverse = word_list[::-1]

if word_list == reverse:
    print('Это палиндром')
else:
    print('Не палиндром')