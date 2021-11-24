"""
Формат ввода
В первой строке записано два целых числа n и q- размер массива и количество запросов.
Во второй строке записаны n целых чисел - сам массив.
Далее в q строках описаны запросы к массиву. Каждый запрос описывается двумя числами
- левой и правой границей отрезка, на котором нужно найти сумму.
Формат вывода
Для каждого запроса в отдельной строке выведите единственное число - сумму на соответствующем отрезке.
"""


n, q = map(int, input().split())
array_n = [int(elem) for elem in input().split()]
pref_sum = [0] * (n + 1)
# for _ in range(q):                 #долго работает
#    left, right = input().split()
#    print(sum(array_n[int(left) - 1: int(right)]))

for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + array_n[i - 1]

for _ in range(q):
    left, right = input().split()
    print(pref_sum[int(right)] - pref_sum[int(left) - 1])
