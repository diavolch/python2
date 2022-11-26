'''Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.'''

n = int(input('Введите число N: '))
lst = []
for i in range(-n,n+1):
    lst.append(i)
print(lst)

lst2 = []
data = open('file.txt', 'r')
for line in data:
    lst2.append(int(line.strip()))
print(lst2)

mult = 1
for i in lst2:
    mult *= lst[i]
print(mult)