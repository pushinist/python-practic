experience = int(input("Какой ваш стаж работы по специальности? "))
if experience < 2:
    print("Ваш коэффициент равен 11")
elif experience >= 2 and experience < 5:
    print("Ваш коэффициент равен 12")
else:
    print("Ваш коэффициент равен 13")

