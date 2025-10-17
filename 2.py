import math

#вариант 6

x = 16.55*math.pow(10, -3)
y = -2.75
z = 0.15

s = math.sqrt(10*(math.pow(x, 1/3)+ math.pow(x, y + 2))) * (math.pow(math.asin(z), 2) - math.fabs(x - y))

print("s = {0:.4f}".format(s))