"""
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""

a = input('Введите первую букву алфавита: ')
b = input('Введите вторую букву алфавита: ')

print(f'Первая введеная буква "{a}" занимает {int(ord(a)) - 96} место алфавита.\n'
      f'Первая введеная буква "{b}" занимает {int(ord(b)) - 96} место алфавита.')

if int(ord(a)) < int(ord(b)):
    print(f'Количество букв алфавита между буквами "{a}", "{b}" составляет: {int(ord(b)) - int(ord(a)) - 1}')
else:
    print(f'Количество букв алфавита между буквами "{a}", "{b}" составляет: {int(ord(a)) - int(ord(b)) - 1}')