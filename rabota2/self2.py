age = int(input("Каков ваш стаж? "))
salary = int(input("Какова ваша зарплата? "))
if age >= 5 and age < 10:
    print(f"Надбавка за стаж в {age} лет - 2%, новая зарплата - {salary * 1.02}")
elif age >= 10 and age < 20:
    print(f"Надбавка за стаж в {age} лет - 10%, новая зарплата - {salary * 1.1}")
elif age >= 20:
    print(f"Надбавка за стаж в {age} лет - 15%, новая зарплата - {salary * 1.15}")
else:
    print(f"Надавка за стаж в {age} лет не предусмотрена")
