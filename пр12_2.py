prices = [1500, 500, 2000, 3500, 1000, 4500]

max_price = max(prices)
min_price = min(prices)
sum_price = sum(prices)
average_price = sum_price / len(prices)

print('Самый дорогой товар: ', max_price)
print('Самый дешевый товар: ', min_price)
print('Общая стоимость всех товаров: ', sum_price)
print(f'Средняя цена товара: {average_price:.0f}')