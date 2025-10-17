import math

# 1.1
a, b, c = map(int, input("Введите 3 целых числа(через пробел) ").split())

if a >= 1 and a <= 3:
    print("Первое число принадлежит промежутку [1, 3]")

if b >= 1 and b <= 3:
    print("Второе число принадлежит промежутку [1, 3]")

if c >= 1 and c <= 3:
    print("Третье число принадлежит промежутку [1, 3]")

# 1.2

x = int(input("Введите двухзначное число "))

first_digit = x//10
second_digit = x%10

if first_digit == second_digit:
    print("Да")
else:
    print("Нет")

# 2 вариант 6

a, b = map(int, input("Введите 2 числа(через пробел) ").split())

if a < b and b > 4:
    x = a + b
elif a > b:
    x = a - b
else:
    x = math.pow(a, 2)

print("x =", x)

# 3 вариант 6

x = int(input("Введите число: "))

if x % 7 == 0:
    print("Число кратно 7")
else:
    print("Число не кратно 7")