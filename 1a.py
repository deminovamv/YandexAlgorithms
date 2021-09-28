'''
Толя-Карп запросил для себя n посылок с «Аллигатор-экспресс».
Посылка представляет из себя ящик. Внутри ящика лежит целое число ai. Номер на ящике di указывает на цвет числа, лежащего внутри.
Толю-Карпа интересует, чему будут равны значения чисел, если сложить между собой все те, что имеют одинаковый цвет.
Напишите, пожалуйста, программу, которая выводит результат.
'''

n = int(input())
color_dict = {}
for _ in range(n):
    color_number, value_number = input().split()
    color_number = int(color_number)
    if color_number in color_dict:
        color_dict[color_number] += int(value_number)
    else:
        color_dict[color_number] = int(value_number)
list_color = list(color_dict.keys())
list_color.sort()
for i in list_color:
    print(i, color_dict[i])
