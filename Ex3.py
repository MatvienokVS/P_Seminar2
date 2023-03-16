# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


number = int(input('Введите число N:'))
res = 1
while res <= number:
    print(res, end=' ')
    res *= 2
