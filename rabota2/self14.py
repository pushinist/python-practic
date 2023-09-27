from math import sqrt
flag = False
while flag == False:
    leg1, hypotenusis = map(float, input("Enter lenght of leg 1 and hypotenusis: ").split())
    if leg1 <= 0 or hypotenusis <= 0:
        print("Lenght of triangle's legs should be more than zero, try another numbers.")
    elif hypotenusis ** 2 - leg1 ** 2 <= 0:
        print("Unexistable triangle, try another numbers.")
    else:
        flag = True
leg2 = sqrt(hypotenusis ** 2 - leg1 ** 2)
print(f"Lenght of leg2 is {leg2}, Square of this triangle is {(leg1 * leg2) / 2}")

