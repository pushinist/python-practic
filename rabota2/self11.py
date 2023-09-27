def S(t):
    return t ** 3 - 3 * t ** 2 + 2 / t

flag = False
while flag == False:
    time = int(input("Enter the time: "))
    if time == 0:
        print("Cannot divide into zero, use another time ")
    else:
        print(f"Velocity in {time} sec is {S(time)}")
        flag = True
