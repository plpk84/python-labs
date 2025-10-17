# вариант 6
n = int(input("Введите число N "))
sum = 1 #начальная сумма

for i in range(1, n + 1):
    sum *= i

print("n! =", sum)

