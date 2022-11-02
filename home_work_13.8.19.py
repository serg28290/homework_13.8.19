num = int(input('Количество билетов: '))
price = 0
for i in range(num):
    age = int(input('Возраст посетителя: '))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    else:
        price += 1390
if num > 3:
    price *= 0.9
print('Сумма к оплате:', str(round(price)), 'рублей')
