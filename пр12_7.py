numbers = [10, 20, 30, 40, 50]

goal = int(input('Введите число для поиска индекса: '))

for i in range(len(numbers)):
    if numbers[i] == goal:
        print(f'Индекс искомого числа: {i}')
        break
else:
    print('Нет такого числа')

