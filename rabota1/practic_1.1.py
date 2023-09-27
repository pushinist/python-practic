from math import sqrt
x, y = map(float, ("1.82, 18").split(","))
print(f"x = {x}, y = {y}")
print(f"s = {abs(x ** (y/x) - (sqrt(y/x)) )} ")
print(f"w = {(y - x) * y / (1 + (y - x) ** 2)}")

