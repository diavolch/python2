'''Напишите программу, которая принимает на вход 
вещественное число и показывает сумму его цифр.

    *Пример:*
    - 6782 -> 23
    - 0.56 -> 11'''

# num = input('Введите число: ')
# num = num.replace('.','0')
# sum = 0
# for i in num:
#     sum += int(i)
# print(sum)

from decimal import Decimal

num = Decimal(input('Введите число: '))
sum = 0
while num % 1 != 0:
    num *= 10
while num >= 1:
    sum += num % 10
    num //= 10
print(int(sum))