"""Вариант 6. Задание 1

Готовый пример матрицы для вставки в консоль:
4 2 7
9 1 5
6 8 3
"""
n = int(input("Введите размер матрицы n: "))

matrix = []
print("Введите матрицу построчно:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

row_max = [max(row) for row in matrix]

col_min = []
for j in range(n):
    column = [matrix[i][j] for i in range(n)]
    col_min.append(min(column))

print("Наибольшие элементы в строках:")
for value in row_max:
    print(value)

print("Наименьшие элементы в столбцах:")
for value in col_min:
    print(value)

"""Вариант 6. Задание 2

Готовый пример матрицы для вставки в консоль:
4 9 6
3 5 1
8 7 2
"""

n = int(input("Введите размер матрицы n: "))

matrix = []
print("Введите матрицу построчно:")
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

diag_elements = []

#СОздаем массивы диагоналей записывая туда (значение, индекс i, индекс j)
for i in range(n):
    diag_elements.append((matrix[i][i], i, i))                  # главная диагональ
    diag_elements.append((matrix[i][n - 1 - i], i, n - 1 - i))  # побочная

max_value, max_i, max_j = max(diag_elements, key=lambda x: x[0]) #ищем элемент с максимальным значением (оно стоит под 0 индексом)

center = n // 2

matrix[max_i][max_j], matrix[center][center] = matrix[center][center], matrix[max_i][max_j] # меняем

print("\nМатрица после замены:")
for row in matrix:
    print(*row)
