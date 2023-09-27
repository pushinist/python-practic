valya_And_Lera = float(input("Сколько килограм кулбники собрали Лера и Валя? "))
Lera = float(input("Сколько из них собрала Лера? "))
Valya = valya_And_Lera - Lera
flag = False
while flag == False:
    if Lera >= valya_And_Lera:
        print("Ошибка, введите корректные данные")
    else:
        flag = True

if Valya > Lera:
    print(f"Валя собрала клубники больше, чем Лера, на {Valya - Lera} кг")
else:
    print(f"Лера собрала клубники больше, чем Валя, на {Lera - Valya} кг")
