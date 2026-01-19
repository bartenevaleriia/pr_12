n = int(input('Введите число n '))

odd = []
for i in range(1,n+1):
    if i % 2 != 0:
        odd.append(i)

print(f'Нечетные числа в промежутке от 1 до {n}: ', *odd)
