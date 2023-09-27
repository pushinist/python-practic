dt = int(input("Сколько продлится разговор в минутах? "))
flag = False
while flag == False:
    region = input("Введите регион, в котором осуществляется звонок. (РФ, ЕАЭС, ЕС): ")
    if region.lower() == "рф":
        s = 0.35
        flag = True
    elif region.lower() == "еаэс":
        s = 0.9
        flag = True
    elif region.lower() = "ес":
        s = 1.5
        flag = True
    else:
        print("Регион не обнаружен, попробуйте повторить попытку ввода.")

d = int(input("Какой сейчас день недели от 1 до 7? "))

if d == 6 or d == 7:
    print(f"Разговор длиной в {dt} минут в {region.upper()} обойдется вам в {dt * s * 0.9} рублей")
else:
    print(f"Разговор длиной в {dt} минут в {region.upper()} обойдется вам в {dt * s} рублей")
    
