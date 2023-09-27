wind_Speed = int(input("Какова скорость ветра? "))

if wind_Speed >= 1 and wind_Speed <= 4:
    print("Ветер слабый")
elif wind_Speed >= 5 and wind_Speed <= 9:
    print("Ветер умеренный")
elif wind_Speed >= 10 and wind_Speed <= 18:
    print("Ветер сильный")
elif wind_Speed >= 19:
    print("Ураган!")
else:
    print("Ветер отсутствует")

