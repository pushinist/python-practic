from math import sqrt
a, b, c = map(float, input("Введите стороны треугольника: ").split())
p = (a + b + c) / 2
print(f"Площадь треугольника со сторонами {a}, {b}, {c} равна {sqrt(p * (p - a) * (p - b) * (p - c))}")
