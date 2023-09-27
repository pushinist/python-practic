from math import exp, sqrt, sin, cos
a, b, x = map(float, ("-0.5, 1.7, 0.44").split(","))

print(f"a = {a}, b = {b}, x = {x}")

print(f"s = {exp(-b * x) * sin(a * x) - sqrt(abs(b * x - a))}")
print(f"w = {b * sin(a * x ** 2 * cos(a * x)) - 1}")
