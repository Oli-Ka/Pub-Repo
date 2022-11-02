#     12.7 Итоговое задание

money = int(input('Ввведите сумму начального депозита:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent2 = list((per_cent.values()))
inc = [i * money for i in per_cent2]
deposit = [i / 100 for i in inc]

bank = list((per_cent.keys()))
result_deposits = dict(zip(bank, deposit))

print('Накопленные средства за год вклада:')
for key,value in result_deposits.items():
    print(key, ':', value)

print('Максимальная сумма, которую вы можете заработать:', max(deposit))