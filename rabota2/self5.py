t = int(input("Какое сейчас время в часах? "))
dt = int(input("Сколько будет длиться разговор в минутах? "))
s = float(input("Сколько стоит минута разговора?"))
d = input("Какой сейчас день недели? ")

if d.lower() == "суббота" or d.lower() == "воскресенье":
    if t >= 22 or t <= 8:
        print(f"Разговор длиной в {dt} минут обойдется вам в {dt * s * 0.9 * 0.95}")
    else:
        print(f"Разговор длиной в {dt} минут обойдется вам в {dt * s * 0.95}")
else:
    if t >= 22 or t <= 8:
        print(f"Разговор длиной в {dt} минут обойдется вам в {dt * s * 0.9}")
    else:
        print(f"Разговор длиной в {dt} минут обойдется вам в {dt * s}")    
