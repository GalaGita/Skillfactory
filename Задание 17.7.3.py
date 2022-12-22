per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
values_List = list(per_cent.values())
deposit = []
money = int(input("Введите сумму (целым числом), которую планируете положить под проценты: "))
for i in values_List:
    deposit.append(int(i*money/100))
print('deposit = ' + str(deposit))
print('Максимальная сумма, которую вы можете заработать — ' + str(max(deposit)))