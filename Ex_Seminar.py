'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
'''

numm = int(input('Введите натуральное число больше 1: '))

fib1 = 0
fib2 = 1

count = 0

while fib1 != numm:
    summ = fib1 + fib2
    fib1 = fib2
    fib2 = summ
    count += 1
    if fib1 > numm:
        print('-1')
        break
else:
    print(count)
