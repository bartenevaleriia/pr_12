data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]
last_three = data[-3:]
reverse = data[::-1]
odd_index = data[1::2]

print('Первая тройка: ', *first_three)
print('Последняя тройка: ', *last_three)
print('В обратном порядке: ', *reverse)
print('С нечетными индексами: ', *odd_index)