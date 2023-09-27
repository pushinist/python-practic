from math import sin, cos
x, y = map(float, ("0.33, 0.02").split(","))
print(f"x = {x}, y = {y}")
print(f"s = {1 + x + x ** 2 / 2 + x ** 3 / 3 + x ** 4 / 4}")
print(f"w = {x * (sin(x) + cos(y))}")
