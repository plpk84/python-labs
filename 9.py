# Вариант 6. Задание 1

def is_prime_number(n,devisor=2):
    if n<=1:
        return "NO"
    if n==2:
        return "YES"
    if n%devisor==0:
        return "NO"
    if devisor*devisor>n:
        return "YES"
    return is_prime_number(n,devisor+1)

print(is_prime_number(1))
print(is_prime_number(2))
print(is_prime_number(12))
print(is_prime_number(11))

# Вариант 6. Задание 2

def find_max():
    num = int(input())
    
    if num == 0:
        return num
    
    next_max = find_max()
    
    return max(num, next_max)

print(find_max())