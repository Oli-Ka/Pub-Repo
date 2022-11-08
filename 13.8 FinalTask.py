amount_tickets = int(input('Введите количество билетов '))
min = 0
mid = 0
max = 0
for i in range(1, amount_tickets + 1):
        age = int(input('Введите возраст участника '))
        if age < 18:
                min += 1
        if 18 <= age < 25:
                mid += 1
        if 25 <= age:
                max += 1
if amount_tickets <= 3:
        print('Общая сумма билетов: ', mid * 990 + max * 1390)
if amount_tickets > 3:
        print('Общая сумма билетов: ', (mid * 990 + max * 1390) * 0.9, ', с учетом скидки 10% !')