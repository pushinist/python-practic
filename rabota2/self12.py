from math import sqrt
leg1, hypotenusis = map(float, input("Enter lenght of leg 1 and hypotenusis: ").split())
leg2 = sqrt(hypotenusis ** 2 - leg1 ** 2)
print(f"Lenght of leg2 is {leg2}, Square of this triangle is {(leg1 * leg2) / 2}")

