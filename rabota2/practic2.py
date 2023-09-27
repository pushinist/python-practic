r1, s1 = map(float, input("Введите сопротивление и площадь сечения цилиндрического проводника 1 : ").split())
r2, s2 = map(float, input("Введите сопротивление и площадь сечения цилиндрического проводника 2 : ").split())
r3, s3 = map(float, input("Введите сопротивление и площадь сечения цилиндрического проводника 3 : ").split())
l = 1

def Resistance(r, s):
    return r / s

if Resistance(r1, s1) > Resistance(r2, s2) and Resistance(r1, s1) > Resistance(r3, s3):
    print("Проводник 1 имеет самое сильное сопротивление")
elif Resistance(r1, s1) < Resistance(r2, s2) and Resistance(r2, s2) > Resistance(r3, s3):
    print("Проводник 2 имеет самое сильное сопротивление")
elif Resistance(r3, s3) > Resistance(r1, s1) and Resistance(r3, s3) > Resistance(r2, s2):
    print("Проводник 3 имеет самое сильное сопротивление")
else:
    print("Проводники имеют равное сопротивление")

