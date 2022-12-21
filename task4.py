# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

num = int(input('Введите число: '))

for _ in range(num):
    print(random.randrange(-num, num), end=" ")

mult = 1
file = open('text.txt', 'r')
for line in file:
    mult *= num[int(line)]
    
file.close()


# 2 вариант

# def get_list(num_f):  # Функция заполнения списка
#     my_list_f = []
#     for i in range(num_f):
#         my_list_f.append(random.randint(-num_f, num_f))
#     return my_list_f


# flag = True  # Ввод числа N от пользователя и проверка на корректность
# while flag:
#     num = input('Введите число N>6: ')
#     if num.isdigit() and int(num) > 6:
#         num = int(num)
#         flag = False
#     else:
#         print('Введено не корректное значение ! Попробуйте еще раз!')

# my_list = get_list(num)
# print(my_list)
# Работа с файлом проверка с исключением (открытие, присваивание переменным значений хранящихся в файле, закрытие файла)
# try:
    # file = open('file.txt', 'r')
    # first_index = int(file.readline())
    # second_index = int(file.readline())
    # third_index = int(file.readline())
    # four_index = int(file.readline())
    # file.close()
# except FileNotFoundError:
#     print('Файл не найден!')
#     exit()  # В случае обнаружения исключения прерываем выполнение программы

# # Перемножение данных хранящихся в листе согласно полученным индексам
# product_1 = my_list[first_index] * my_list[second_index]
# product_2 = my_list[third_index] * my_list[four_index]

# print(f'first_index - {first_index}, second_index - {second_index},'
#       f' third_index - {third_index}, four_index - {four_index}')
# print(f'{my_list[first_index]}*{my_list[second_index]} = {product_1}')
# print(f'{my_list[third_index]}*{my_list[four_index]} = {product_2}')
