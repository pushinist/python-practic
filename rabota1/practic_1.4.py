from math import sqrt, cos
a, b, x = map(float, ("-0.5, 15.5, -2.9").split(","))

print(f"a = {a}, b = {b}, x = {x}")

print(f"s = {sqrt(x**2 + b) - (b**2 - 2 * a) / x}")
print(f"w = {cos(x ** 3) - x / sqrt(a**2 + b**2)}")

