def month_to_season(month):
    if 1 <= month <= 3:
        return "весна"
    elif 4 <= month <= 6:
        return "лето"
    elif 7 <= month <= 9:
        return "осень"
    elif 10 <= month <= 12:
        return "зима"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца (1-12): "))

    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
