"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter

org_count = int(input('Введите количество организаций: '))
coll_count = Counter()
for el in range(org_count):
    org_name = input('Введите название организации: ')
    for quarter in range(1, 5):
        coll_count.update({org_name: round(float(input(f'Введите прибыль за {quarter}-й квартал: ')), 2)})  # округление
        # до второго знака после запятой, 0.999999 у.е. не бывает
print(f'Средняя прыбыль организаций: {round(sum(coll_count.values())/org_count, 2)}')
max_org = []
min_org = []
for org, count in coll_count.items():
    if count >= sum(coll_count.values())/org_count:
        max_org.append(org)
    else:
        min_org.append(org)
print(f'Организации, чья прибыль выше среднеего значения: {max_org}\n'
      f'Организации, чья прибыль ниже среднеего значения: {min_org}')
