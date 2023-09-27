from math import exp, tan
def sinh(x):
    return (exp(x) - exp(-x)) / 2

def y(x):
    return sinh(x) * tan(x + 1) - tan(2 + sinh(x - 1)) ** 2

x = float(input())
print(f"y({x}) = {y(x)}")

