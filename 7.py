#Вариант 6. Задание 1

def gcd(a, b):
    #НОД
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    #НОК
    return a * b // gcd(a, b)

A = int(input("Введите A: "))
B = int(input("Введите B: "))

print("НОД =", gcd(A, B))
print("НОК =", lcm(A, B))

#Вариант 6. Задание 2

import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
d = float(input("Введите сторону d: "))
e = float(input("Введите диагональ e: "))

S1 = triangle_area(a, b, e)
S2 = triangle_area(c, d, e)

S = S1 + S2

print("Площадь четырёхугольника =", S)
