# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
from random import randint as rnd

value_maney = int(input('Введите количество монет: '))

number = []

for i in range(value_maney):
    number.append(rnd(0, 1))
print(number)
