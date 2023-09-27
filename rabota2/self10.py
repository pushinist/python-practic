#money = int(input())

for money in range(1, 30):
    if money <= 10 or money >= 20:
        if money % 10 == 1:
            print(f"{money} копейка")
        elif money % 10 >= 2 and money % 10 <= 4:
            print(f"{money} копейки")
        else:
            print(f"{money} копеек")
    else:
        print(f"{money} копеек")
