#Вариант 6

#Задание 1
n = 10
count_max = count_min = 0
x = []

for i in range(n):
    a = int(input("Введите элемент: "))
    if i == 0 or max < a:
        max = a
    x.append(a)

for i in range(n):
    if x[i] < max:
        count_min += 1
    else:
        count_max += 1

print(f"Максимальный элемент: {max}")
print(f"Количество элементов меньше максимального {count_min}")
print(f"Количество элементов равных максимальному {count_max - 1}") #элемент взятый максимумом не берем в выборку

#Задание 2

sum = 0
for i in range(n):
    if x[i] > 5:
        sum += x[i]

print(f"Сумма элементов больше 5: {sum}")