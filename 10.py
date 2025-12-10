# Вариант 6. Задание 1

file = open("chpa_um-252_vvod.txt",'r')
output_file = open("chpa_um-252_vivod.txt",'w')

n = int(file.readline())

matrix = []
for i in range(n):
    row = list(map(int, file.readline().split()))
    matrix.append(row)

row_max = [max(row) for row in matrix]

col_min = []
for j in range(n):
    column = [matrix[i][j] for i in range(n)]
    col_min.append(min(column))

output_file.write("Наибольшие элементы в строках:\n")
for value in row_max:
    output_file.write(str(value)+'\n')

output_file.write("Наименьшие элементы в столбцах:\n")
for value in col_min:
    output_file.write(str(value)+'\n')

# Вариант 6. Задание 2

n = int(file.readline())

matrix = []
for i in range(n):
    row = list(map(float, file.readline().split()))
    matrix.append(row)

diag_elements = []

for i in range(n):
    diag_elements.append((matrix[i][i], i, i))
    diag_elements.append((matrix[i][n - 1 - i], i, n - 1 - i))

max_value, max_i, max_j = max(diag_elements, key=lambda x: x[0]) #ищем элемент с максимальным значением (оно стоит под 0 индексом)

center = n // 2

matrix[max_i][max_j], matrix[center][center] = matrix[center][center], matrix[max_i][max_j]

output_file.write("Матрица после замены:\n")
for row in matrix:
    for column in row:
        output_file.write(str(column)+' ')
    output_file.write('\n')
    
file.close()
output_file.close()