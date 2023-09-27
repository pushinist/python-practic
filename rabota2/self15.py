def equation(a, b):
    return 12 * a - a * b

a, b = map(float, input("Enter number a and b: ").split())
if a == 0:
    print("Cannot divide into zero, try another number a")
else:
    print(f"{equation(a, b)}")

